from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    probability = data.get("probability", 0.0)

    # Simple threshold evaluation
    if probability >= 0.5:
        result = "High Risk"
    else:
        result = "Low Risk"

    return jsonify({
        "probability": probability,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
