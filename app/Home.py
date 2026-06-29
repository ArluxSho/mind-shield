import streamlit as st

st.set_page_config(
    page_title="Student Depression Prediction",
    page_icon="🧠",
    layout="wide"
)

st.sidebar.success("Student Depression Prediction")

st.sidebar.info(
    """
    Machine Learning Project

    Random Forest

    SHAP Feature Selection

    FastAPI + Streamlit
    """
)

st.title("🧠 Student Depression Prediction")

st.markdown("---")

st.markdown("""
## Welcome 👋

Aplikasi ini merupakan implementasi penelitian klasifikasi depresi mahasiswa
menggunakan **Random Forest** dengan **SHAP Feature Importance**.

Melalui dashboard ini pengguna dapat:

- 📊 Melihat statistik dataset
- 📈 Melihat hasil Exploratory Data Analysis
- ⭐ Melihat Feature Importance
- 🤖 Melakukan prediksi depresi mahasiswa
- 📖 Membaca informasi penelitian
""")

st.info("Pilih menu di sidebar untuk memulai.")