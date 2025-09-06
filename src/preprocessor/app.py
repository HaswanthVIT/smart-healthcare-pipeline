from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Example features: age, blood_pressure, glucose
    age = data.get("age", 0)
    bp = data.get("blood_pressure", 0)
    glucose = data.get("glucose", 0)

    # Simple normalization (0-1 scaling, demo only)
    normalized = [
        age / 100.0,
        bp / 200.0,
        glucose / 300.0
    ]

    return jsonify({"features": normalized})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
