import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Exploratory Data Analysis")

df = pd.read_csv("dataset/Depression Student Dataset.csv")

st.subheader("Age Distribution")

fig = px.histogram(
    df,
    x="Age",
    color="Depression",
    barmode="overlay"
)

st.plotly_chart(fig, width="stretch")

st.subheader("Study Hours")

fig = px.histogram(
    df,
    x="Study Hours",
    color="Depression"
)

st.plotly_chart(fig, width="stretch")

st.subheader("Sleep Duration")

fig = px.histogram(
    df,
    x="Sleep Duration",
    color="Depression"
)

st.plotly_chart(fig, width="stretch")

st.subheader("Dietary Habits")

fig = px.histogram(
    df,
    x="Dietary Habits",
    color="Depression"
)

st.plotly_chart(fig, width="stretch")

st.caption(
    "Student Depression Prediction © 2026"
)