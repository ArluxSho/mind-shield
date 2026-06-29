from fastapi import FastAPI

from app.schemas import StudentData

from app.model_loader import (
    MODEL,
    ENCODERS,
    FEATURE_COLUMNS
)

import pandas as pd

app = FastAPI(
    title="Student Depression Prediction API",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Student Depression Prediction API is running!"
    }


@app.post("/predict")
def predict(data: StudentData):

    input_data = {

        "Gender": data.gender,

        "Age": data.age,

        "Academic Pressure": data.academic_pressure,

        "Study Satisfaction": data.study_satisfaction,

        "Sleep Duration": data.sleep_duration,

        "Dietary Habits": data.dietary_habits,

        "Have you ever had suicidal thoughts ?": data.suicidal_thoughts,

        "Study Hours": data.study_hours,

        "Financial Stress": data.financial_stress,

        "Family History of Mental Illness": data.family_history

    }

    df = pd.DataFrame([input_data])

    print("========== INPUT ==========")
    print(df)

    print("\n========== FEATURE COLUMNS ==========")
    print(FEATURE_COLUMNS)

    print("\n========== ENCODERS ==========")
    print(list(ENCODERS.keys()))

    for col, encoder in ENCODERS.items():
        if col in df.columns:
            df[col] = encoder.transform(df[col])

    df = df[FEATURE_COLUMNS]

    prediction = MODEL.predict(df)[0]

    probability = MODEL.predict_proba(df)[0]

    confidence = max(probability)

    prediction = "Yes" if prediction == 1 else "No"

    return {
        "prediction": prediction,
        "confidence": round(float(confidence * 100), 2)
    }