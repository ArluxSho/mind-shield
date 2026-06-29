import joblib
import os

BASE_DIR = os.path.dirname(__file__)

MODEL = joblib.load(
    os.path.join(BASE_DIR, "model", "random_forest.pkl")
)

ENCODERS = joblib.load(
    os.path.join(BASE_DIR, "model", "encoders.pkl")
)

FEATURE_COLUMNS = joblib.load(
    os.path.join(BASE_DIR, "model", "feature_columns.pkl")
)