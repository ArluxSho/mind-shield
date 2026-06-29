import streamlit as st

from services.api_service import predict

st.title("🤖 Student Depression Prediction")

st.write("Masukkan data mahasiswa.")

gender = st.selectbox(
    "Gender",
    ["Male","Female"]
)

age = st.number_input(
    "Age",
    18,
    35,
    22
)

academic_pressure = st.slider(
    "Academic Pressure",
    1,
    5,
    3
)

study_satisfaction = st.slider(
    "Study Satisfaction",
    1,
    5,
    3
)

sleep_duration = st.selectbox(
    "Sleep Duration",
    [
        "Less than 5 hours",
        "5-6 hours",
        "7-8 hours",
        "More than 8 hours"
    ]
)

dietary_habits = st.selectbox(
    "Dietary Habits",
    [
        "Healthy",
        "Moderate",
        "Unhealthy"
    ]
)

suicidal = st.selectbox(
    "Suicidal Thoughts",
    [
        "Yes",
        "No"
    ]
)

study_hours = st.slider(
    "Study Hours",
    0,
    12,
    6
)

financial = st.slider(
    "Financial Stress",
    1,
    5,
    3
)

family = st.selectbox(
    "Family History",
    [
        "Yes",
        "No"
    ]
)

if st.button("Predict"):

    data = {
        "gender": gender,
        "age": age,
        "academic_pressure": academic_pressure,
        "study_satisfaction": study_satisfaction,
        "sleep_duration": sleep_duration,
        "dietary_habits": dietary_habits,
        "suicidal_thoughts": suicidal,
        "study_hours": study_hours,
        "financial_stress": financial,
        "family_history": family
    }

    result = predict(data)

    st.write(result)

    st.divider()

st.caption(
    "Student Depression Prediction © 2026"
)