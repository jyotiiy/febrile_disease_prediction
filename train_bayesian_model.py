import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from sklearn.preprocessing import KBinsDiscretizer
import joblib

df = pd.read_csv("data/final_febrile_illness_dataset_1000.csv")

continuous_cols = [
    "fever_temp","platelet_count","wbc_count",
    "hemoglobin","hematocrit"
]

discretizer = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="quantile")
df[continuous_cols] = discretizer.fit_transform(df[continuous_cols]).astype(int)

model = DiscreteBayesianNetwork([
    ("fever_temp","disease"),
    ("platelet_count","disease"),
    ("wbc_count","disease"),
    ("hemoglobin","disease"),
    ("hematocrit","disease"),
    ("chills","disease"),
    ("joint_pain","disease"),
    ("rash","disease"),
    ("rdt_malaria","disease"),
    ("dengue_ns1","disease"),
    ("widal_test","disease")
])

model.fit(df, estimator=MaximumLikelihoodEstimator)

joblib.dump(model, "bayesian_model.pkl")
joblib.dump(discretizer, "discretizer.pkl")

print("Bayesian Network trained and saved.")
