# diet_backend/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from model_utils import recommend

# Initialize app
app = FastAPI(title="Diet Recommendation API")

# Load dataset and max values
dataset = joblib.load("raw_dataset.pkl")
max_nutrition = joblib.load("max_nutrition.pkl")

# Request format
class NutritionInput(BaseModel):
    calories: float
    fat: float
    saturated_fat: float
    cholesterol: float
    sodium: float
    carbs: float
    fiber: float
    sugar: float
    protein: float
    ingredients: list[str] = []  # Optional ingredient filters

@app.get("/")
def root():
    return {"message": "Diet Recommendation API is running!"}

@app.post("/recommend")
def get_recommendations(input_data: NutritionInput):
    try:
        input_array = [[
            input_data.calories,
            input_data.fat,
            input_data.saturated_fat,
            input_data.cholesterol,
            input_data.sodium,
            input_data.carbs,
            input_data.fiber,
            input_data.sugar,
            input_data.protein
        ]]

        results = recommend(
            dataframe=dataset,
            _input=input_array,
            max_nutritional_values=[
                input_data.calories,
                input_data.fat,
                input_data.saturated_fat,
                input_data.cholesterol,
                input_data.sodium,
                input_data.carbs,
                input_data.fiber,
                input_data.sugar,
                input_data.protein
            ],
            ingredient_filter=input_data.ingredients
        )

        if results.empty:
            return {"recipes": []}

        return {
            "recipes": results[['Name', 'Calories', 'RecipeIngredientParts']].to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
