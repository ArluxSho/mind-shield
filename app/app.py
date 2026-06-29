import streamlit as st

from views.home import home_page
from views.dashboard import dashboard_page
from views.eda import eda_page
from views.prediction import prediction_page
from views.shap import shap_page
from views.about import about_page


st.set_page_config(
    page_title="Student Depression Prediction",
    page_icon="🧠",
    layout="wide"
)


st.sidebar.title("🧠 Student Depression")

menu = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "📊 Dashboard",

        "📈 EDA",

        "⭐ Feature Importance",

        "🤖 Prediction",

        "📖 About"

    ]

)


if menu == "🏠 Home":

    home_page()

elif menu == "📊 Dashboard":

    dashboard_page()

elif menu == "📈 EDA":

    eda_page()

elif menu == "⭐ Feature Importance":

    shap_page()

elif menu == "🤖 Prediction":

    prediction_page()

elif menu == "📖 About":

    about_page()