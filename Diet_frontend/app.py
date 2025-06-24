import streamlit as st
import joblib
import numpy as np
import pandas as pd
import requests

st.set_page_config(page_title="Diet Recommendation System")
st.title("🥗 Diet Recommendation System")
st.markdown("Get healthy recipe recommendations based on your dietary goals.")

# Load dataset and max nutrition list from the backend folder
dataset = joblib.load("../Diet_backend/raw_dataset.pkl")
max_list = joblib.load("../Diet_backend/max_nutrition.pkl")

# --- User Profile Form ---
st.subheader("Modify the values and click the Generate button to use")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
    weight = st.number_input("Weight (kg)", min_value=10, max_value=300, value=65)

with col2:
    gender = st.radio("Gender", options=["Male", "Female"])
    activity = st.selectbox("Activity Level", [
        "Little/no exercise",
        "Light exercise (1-3 days/week)",
        "Moderate exercise (3-5 days/week)",
        "Hard exercise (6-7 days/week)",
        "Extra active (very active & physical job)"
    ])

with col3:
    goal = st.selectbox("Choose your weight loss plan:", ["Maintain weight", "Lose weight", "Gain weight"])
    meals_per_day = st.slider("Meals per day", 1, 6, value=3)

# --- Calorie Calculation ---
def calculate_bmr(age, height, weight, gender):
    if gender == "Male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def activity_multiplier(level):
    mapping = {
        "Little/no exercise": 1.2,
        "Light exercise (1-3 days/week)": 1.375,
        "Moderate exercise (3-5 days/week)": 1.55,
        "Hard exercise (6-7 days/week)": 1.725,
        "Extra active (very active & physical job)": 1.9
    }
    return mapping.get(level, 1.2)

bmr = calculate_bmr(age, height, weight, gender)
tdee = bmr * activity_multiplier(activity)

if goal == "Lose weight":
    tdee -= 500
elif goal == "Gain weight":
    tdee += 500

st.markdown(f"### 🧮 Estimated Daily Calories: `{int(tdee)} kcal`")

# --- Nutrition Sliders ---
st.subheader("Adjust Nutritional Limits")
cols = dataset.columns[6:15]
user_inputs = []

for col, max_val in zip(cols, max_list):
    default = int(tdee * (max_val / 2000)) if col == "Calories" else int(max_val * 0.5)
    val = st.slider(f"{col}", min_value=0, max_value=int(max_val), value=default)
    user_inputs.append(val)

# --- Ingredient Filter ---
st.subheader("Optional: Add Ingredients You Prefer")
ingredient_filter = st.text_input("Type comma-separated ingredients (e.g., egg, milk)")
ingredient_list = [i.strip() for i in ingredient_filter.split(",") if i.strip()] if ingredient_filter else []

# --- Recommend Recipes ---
if st.button("Recommend Recipes"):
    try:
        api_url = "http://127.0.0.1:8000/recommend"
        payload = {
            "calories": user_inputs[0],
            "fat": user_inputs[1],
            "saturated_fat": user_inputs[2],
            "cholesterol": user_inputs[3],
            "sodium": user_inputs[4],
            "carbs": user_inputs[5],
            "fiber": user_inputs[6],
            "sugar": user_inputs[7],
            "protein": user_inputs[8],
            "ingredients": ingredient_list
        }

        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            recipes = response.json()["recipes"]
            results = pd.DataFrame(recipes)
            if results.empty:
                st.warning("No matching recipes found. Try relaxing your filters.")
            else:
                st.success(f"Found {len(results)} matching recipes:")
                st.dataframe(results[['Name', 'Calories', 'RecipeIngredientParts']])
        else:
            st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
