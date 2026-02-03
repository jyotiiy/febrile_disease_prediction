import joblib
import numpy as np
from pgmpy.inference import VariableElimination

model = joblib.load("bayesian_model.pkl")
discretizer = joblib.load("discretizer.pkl")

inference = VariableElimination(model)

def predict_disease(input_dict):
    query = inference.query(
        variables=["disease"],
        evidence=input_dict
    )

    probs = query.values
    diseases = query.state_names["disease"]

    idx = np.argmax(probs)
    return diseases[idx], probs[idx]
