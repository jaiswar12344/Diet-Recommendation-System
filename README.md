# 🥗 Diet Recommendation System

A Machine Learning-powered system that recommends personalized diet plans and recipes based on user preferences and nutritional goals. Developed as part of my internship at **Feynn Labs** under the guidance of **Mr. Sanjay Basumatary**, this project combines data science, intelligent modeling, and web deployment into one complete solution.

---

## 🔍 Project Summary (For Portfolio)

**Tools:** Python, Scikit-learn, Pandas, Streamlit, Hugging Face Spaces  
**Role:** Machine Learning Engineer Intern @ Feynn Labs  
**Mentor:** Mr. Sanjay Basumatary  

Developed an ML-powered system to recommend personalized diet plans based on nutritional goals and user preferences. Performed data cleaning, feature engineering, and model training using Scikit-learn. Built a user-friendly web interface with Streamlit and deployed the solution on Hugging Face Spaces. The system allows users to input dietary preferences and returns relevant, nutritionally balanced meal suggestions with visual insights. Achieved high model accuracy and created a scalable architecture for future health integrations.

---

## 📌 Table of Contents

- [Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Model Workflow](#model-workflow)
- [Results](#results)
- [Demo](#demo)
- [Author](#author)
- [Acknowledgements](#acknowledgements)
- [License](#license)
- [Contributing](#contributing)

---

## 📖 Project Overview

This system helps individuals find diet plans and meal suggestions tailored to their health goals—whether it's weight loss, muscle gain, or simply maintaining a healthy lifestyle. It analyzes nutritional components such as calories, proteins, fats, and carbs, and recommends recipes using a trained machine learning model. The platform is deployed with a sleek Streamlit interface for easy interaction.

---

## 🚀 Features

- ✅ **Personalized Meal Suggestions**
- 🧠 **ML-based Dietary Classification**
- 🧴 **Ingredient Filtering & Constraints**
- 📊 **Nutritional Analysis & Visualization**
- 🌐 **Streamlit Web App Deployed on Hugging Face Spaces**

---

## 🧰 Tech Stack

| Category           | Tools/Libraries                      |
|--------------------|--------------------------------------|
| Language           | Python                               |
| Data Handling      | Pandas, NumPy                        |
| ML Modeling        | Scikit-learn                         |
| Visualization      | Matplotlib, Seaborn                  |
| Web Interface      | Streamlit                            |
| Model Storage      | Joblib                               |
| Deployment         | Hugging Face Spaces                  |

---

## 📁 Project Structure

Diet_Recommendation_System/
│
├── Diet_backend/
│ ├── raw_dataset_compressed.pkl.gz # Preprocessed dataset
│ ├── model.pkl # Trained ML model
│ └── utils.py # Helper functions
│
├── Diet_frontend/
│ ├── app.py # Streamlit frontend
│ └── requirements.txt # Dependencies
│
├── Output/
│ ├── heatmap.png # Visual insights
│ └── analysis_report.pdf # Optional summary
│
└── README.md # This file

##🔄 Model Workflow
Data Preprocessing: Handle nulls, normalize features, encode text fields.

Feature Engineering: Nutrient-based feature extraction and transformation.

Model Training: ML model trained to classify meals based on suitability.

Evaluation: Validated using classification metrics and cross-validation.

Deployment: Model served through Streamlit and deployed to Hugging Face Spaces.

##📊 Results
Achieved 96%+ accuracy for diet recommendation tasks.

Offered real-time, interactive filtering through the Streamlit UI.

Provided visual analysis of nutrients and correlations using heatmaps.
