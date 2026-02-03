from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# -----------------------------
# Utility: Simple Clinical Logic
# (Replace with Bayesian inference later)
# -----------------------------
def bayesian_inference(data):
    factors = []
    confidence = 70
    illness = "Viral Fever"

    temp = data["temperature"]
    platelet = data["platelet"]
    wbc = data["wbc"]
    hb = data["hemoglobin"]

    symptoms = data["symptoms"]
    tests = data["tests"]

    # Dengue
    if tests["dengueNS1"] or (platelet is not None and platelet < 100):
        illness = "Dengue Fever"
        confidence = 90
        if tests["dengueNS1"]:
            factors.append("Dengue NS1 test positive")
        if platelet and platelet < 100:
            factors.append(f"Low platelet count ({platelet} ×10³/μL)")
        if symptoms["jointPain"]:
            factors.append("Joint pain present")
        if temp >= 102:
            factors.append(f"High fever ({temp}°F)")

    # Malaria
    elif tests["malariaRDT"] or (hb is not None and hb < 10):
        illness = "Malaria"
        confidence = 88
        if tests["malariaRDT"]:
            factors.append("Malaria RDT positive")
        if hb and hb < 10:
            factors.append(f"Low hemoglobin ({hb} g/dL)")
        if symptoms["chills"]:
            factors.append("Chills present")

    # Typhoid
    elif tests["widalTest"]:
        illness = "Typhoid Fever"
        confidence = 85
        factors.append("Widal test positive")
        if symptoms["bodyPain"]:
            factors.append("Body pain present")

    # Viral fever
    else:
        if temp >= 100.4:
            factors.append(f"Fever present ({temp}°F)")
        if symptoms["headache"]:
            factors.append("Headache present")
        if symptoms["bodyPain"]:
            factors.append("Body pain present")
        if wbc and 4 <= wbc <= 11:
            factors.append("Normal WBC count")

    if not factors:
        factors.append("General febrile symptoms")

    return illness, confidence, factors


# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    illness, confidence, factors = bayesian_inference(data)

    return jsonify({
        "illness": illness,
        "confidence": confidence,
        "factors": factors
    })


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
