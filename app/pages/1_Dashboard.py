import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Student Depression Dashboard")

# =========================
# Load Dataset
# =========================

df = pd.read_csv("dataset/Depression Student Dataset.csv")

# =========================
# Metrics
# =========================

st.subheader("Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Student",
    len(df)
)

c2.metric(
    "Depression",
    (df["Depression"] == "Yes").sum()
)

c3.metric(
    "No Depression",
    (df["Depression"] == "No").sum()
)

c4.metric(
    "Features",
    len(df.columns)-1
)

st.divider()

# =========================
# Pie Chart
# =========================

left, right = st.columns(2)

with left:

    fig = px.pie(
        df,
        names="Depression",
        title="Depression Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

with right:

    gender_df = (
        df["Gender"]
        .value_counts()
        .rename_axis("Gender")
        .reset_index(name="Count")
    )

    fig = px.bar(
        gender_df,
        x="Gender",
        y="Count",
        title="Gender Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

st.divider()

# =========================
# Academic Pressure
# =========================

fig = px.histogram(
    df,
    x="Academic Pressure",
    title="Academic Pressure Distribution"
)

st.plotly_chart(
    fig,
    width="stretch"
)

# =========================
# Study Satisfaction
# =========================

fig = px.histogram(
    df,
    x="Study Satisfaction",
    title="Study Satisfaction Distribution"
)

st.plotly_chart(
    fig,
    width="stretch"
)

# =========================
# Financial Stress
# =========================

fig = px.histogram(
    df,
    x="Financial Stress",
    title="Financial Stress Distribution"
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.divider()

st.subheader("Dataset")

st.dataframe(
    df,
    width="stretch"
)