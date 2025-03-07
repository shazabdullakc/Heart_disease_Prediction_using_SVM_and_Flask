from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("svm_model.pkl")
scaler = joblib.load("svm_scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html",prediction_text="")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        print(request.form)  # Debugging: Check what data is being received

        data = [float(request.form[key]) for key in [
            "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
            "thalach", "exang", "oldpeak", "slope", "ca", "thal"
        ]]

        data_scaled = scaler.transform([data])
        prediction = model.predict(data_scaled)[0]
        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

        return render_template("index.html", prediction_text=f"Prediction: {result}")

    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging: Log errors
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
