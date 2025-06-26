import joblib
import numpy as np

# Load the model once
model = joblib.load("backend/ml_model/model.pkl")

# Required feature order depends on the trained model


def predict_risk(features_dict):
    # Example expected inputs: age, sex, bp, cholesterol, sugar, etc.
    # NOTE: Match exact order and scale used in training
    input_features = [
        features_dict.get("age", 50),
        features_dict.get("sex", 1),
        features_dict.get("bp", 120),
        features_dict.get("cholesterol", 200),
        features_dict.get("sugar", 0),
        features_dict.get("ecg", 0),
        features_dict.get("max_hr", 150),
        features_dict.get("exercise_angina", 0)
    ]

    input_array = np.array([input_features])
    result = model.predict(input_array)[0]

    return "RISK_HIGH" if result == 1 else "RISK_LOW"
