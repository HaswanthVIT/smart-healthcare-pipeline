from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Service URLs (later these will be Kubernetes service names, for now localhost + ports)
PREPROCESSOR_URL = "http://localhost:5000/predict"
CLASSIFIER_URL = "http://localhost:5001/predict"
EVALUATOR_URL = "http://localhost:5002/predict"

@app.route("/predict", methods=["POST"])
def predict():
    # Step 1: Get raw patient input
    data = request.get_json()

    # Step 2: Send to Preprocessor
    preprocessed = requests.post(PREPROCESSOR_URL, json=data).json()

    # Step 3: Send features to Classifier
    classified = requests.post(CLASSIFIER_URL, json=preprocessed).json()

    # Step 4: Send probability to Evaluator
    evaluated = requests.post(EVALUATOR_URL, json=classified).json()

    # Step 5: Return final result
    return jsonify({
        "input": data,
        "normalized_features": preprocessed,
        "probability": classified,
        "final_decision": evaluated
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
