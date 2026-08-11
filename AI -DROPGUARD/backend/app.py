from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load trained model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "water_model.pkl"
)

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# Home / API status
@app.route("/")
def home():
    return "🚰 AI DropGuard API is Running Successfully!"


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    flow = float(data["Flow_Rate"])
    duration = float(data["Duration"])
    presence = int(data["Presence"])

    input_data = pd.DataFrame(
        [[flow, duration, presence]],
        columns=["Flow_Rate", "Duration", "Presence"]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        result = "⚠️ Water Wastage Detected!"
    else:
        result = "✅ Water Usage is Normal."

    return jsonify({"Prediction": result})


if __name__ == "__main__":
    app.run(debug=True)