import streamlit as st

st.title("ℹ️ About")

st.write("### Student Depression Prediction")

st.write("""
This application predicts the possibility of student depression
using Machine Learning.

Model :
- Random Forest

Feature Selection :
- SHAP

Backend :
- FastAPI

Frontend :
- Streamlit
""")

st.divider()

st.caption(
    "Student Depression Prediction © 2026"
)