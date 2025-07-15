from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the trained model
model = load("house_price_model.pkl")

@app.route("/")
def home():
    return "🏠 House Price Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    area = data.get("area")
    bedrooms = data.get("bedrooms")
    age = data.get("age")

    # Make prediction
    features = np.array([[area, bedrooms, age]])
    prediction = model.predict(features)

    return jsonify({
        "predicted_price": round(prediction[0], 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
