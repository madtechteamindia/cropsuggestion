# FarmMate – Smart Crop & Fertilizer Recommender

FarmMate is a machine learning-powered agriculture assistant that helps users determine the most suitable crop to grow based on soil and environmental conditions. It also recommends fertilizer corrections and provides detailed, human-like crop care tips including soil suggestions and cultivation advice.

---

## Features

- Crop recommendation based on soil nutrients (N, P, K), temperature, humidity, pH, and rainfall.
- Fertilizer suggestions based on nutrient deviations from ideal NPK values.
- GenAI-style JSON-based crop explanations with care tips and best practices.
- Simple and interactive web interface built using Streamlit.

---

## Tech Stack

| Component        | Tools and Technologies                          |
|------------------|--------------------------------------------------|
| Programming      | Python 3                                         |
| Data Handling    | Pandas, NumPy                                    |
| Machine Learning | Scikit-learn (Random Forest Classifier)         |
| Web Interface    | Streamlit                                       |
| Explanation Data | JSON (for static GenAI-style explanations)       |

---

## Dataset Overview

- Crop dataset includes:
  - Features: Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall
  - Target: Crop label
- Fertilizer dataset includes:
  - Ideal NPK values for each crop
  - Suggestion logic for nutrient excess or deficiency

---

## Model

- Algorithm: Random Forest Classifier
- Dataset: `Crop_recommendation.csv`
- Accuracy: ~98% on internal testing
- Training handled dynamically within the app (no separate pickle file needed)

---



