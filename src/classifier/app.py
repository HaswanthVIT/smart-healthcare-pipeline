from flask import Flask, request, jsonify
import joblib
import os
import numpy as np
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

MODEL_FILE = "model.pkl"

# Create and save a simple model if it doesn't exist
if not os.path.exists(MODEL_FILE):
    X = np.array([
        [0.4, 0.6, 0.5],  # normalized features: age, bp, glucose
        [0.2, 0.3, 0.2],
        [0.8, 0.9, 0.7]
    ])
    y = [1, 0, 1]  # 1 = diabetes risk, 0 = no risk
    clf = LogisticRegression()
    clf.fit(X, y)
    joblib.dump(clf, MODEL_FILE)

model = joblib.load(MODEL_FILE)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data.get("features")).reshape(1, -1)
    prob = model.predict_proba(features)[0][1]
    return jsonify({"probability": float(prob)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
