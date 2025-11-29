import streamlit as st
import pandas as pd
import json
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Load dataset and explanation file
fertilizer_df = pd.read_csv("Fertilizer.csv")
with open("crop_explanations.json", "r") as f:
    crop_explanations = json.load(f)

# Dummy model training (for crop recommendation)
def train_model():
    df = pd.read_csv("Crop_recommendation.csv")
    X = df.drop('label', axis=1)
    y = df['label']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = train_model()

# Nutrient thresholds for suggestions
ideal_npk = {
    'N': 90,
    'P': 40,
    'K': 40
}

def suggest_fertilizer(n, p, k):
    suggestions = []
    for nutrient, ideal in ideal_npk.items():
        current = {'N': n, 'P': p, 'K': k}[nutrient]
        diff = current - ideal
        if diff > 5:
            suggestions.append(f"Reduce {nutrient} (Excess by {diff:.1f} units)")
        elif diff < -5:
            suggestions.append(f"Increase {nutrient} (Deficit by {abs(diff):.1f} units)")
    return suggestions if suggestions else ["NPK levels are optimal."]

def main():
    st.set_page_config(page_title="FarmMate", page_icon="🌾")
    st.title(" FarmMate: Smart Crop & Fertilizer Suggestor")

    st.header("Enter Soil Parameters")
    n = st.number_input("Nitrogen (N)", 0, 200, step=1)
    p = st.number_input("Phosphorus (P)", 0, 200, step=1)
    k = st.number_input("Potassium (K)", 0, 200, step=1)
    temperature = st.slider("Temperature (°C)", 0.0, 50.0, step=0.1)
    humidity = st.slider("Humidity (%)", 0.0, 100.0, step=0.1)
    ph = st.slider("pH value", 0.0, 14.0, step=0.1)
    rainfall = st.slider("Rainfall (mm)", 0.0, 400.0, step=1.0)

    if st.button("Get Recommendation"):
        features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
        crop = model.predict(features)[0]
        crop_info = crop_explanations.get(crop.lower(), "No explanation available for this crop.")

        st.success(f" Recommended Crop: **{crop.upper()}**")
        st.markdown(f" **Explanation**: {crop_info}")

        st.divider()

        st.header(" Fertilizer Suggestion")
        fert_suggestions = suggest_fertilizer(n, p, k)
        for fs in fert_suggestions:
            st.info(fs)

if __name__ == "__main__":
    main() 
