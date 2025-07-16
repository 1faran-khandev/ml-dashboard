from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load("house_price_model.pkl")

@app.route("/")
def home():
    return "🏠 House Price API is Live"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    area = data.get("area")
    bedrooms = data.get("bedrooms")
    age = data.get("age")

    features = np.array([[area, bedrooms, age]])
    prediction = model.predict(features)
    return jsonify({"predicted_price": round(prediction[0], 2)})

if __name__ == "__main__":
    app.run(debug=True)
