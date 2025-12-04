import joblib
from pathlib import Path
import numpy as np

MODEL_PATH = Path(__file__).parent / "model.joblib"
MODEL = joblib.load(MODEL_PATH)

TARGET_NAMES = np.array(['setosa', 'versicolor', 'virginica'])

def predict(features: list[float]) -> str:

    prediction_raw = MODEL.predict([features])

    prediction_index = prediction_raw[0]

    predicted_species = TARGET_NAMES[prediction_index]
    
    return predicted_species