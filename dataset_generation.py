import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

DISEASES = ["Dengue", "Malaria", "Typhoid", "Viral Fever", "Chikungunya"]
SAMPLES_PER_DISEASE = 200

data = []

for disease in DISEASES:
    for _ in range(SAMPLES_PER_DISEASE):

        fever_temp = round(np.random.uniform(38.0, 40.8), 1)
        headache = 1
        body_pain = 1
        chills = 0
        joint_pain = 0
        rash = 0
        nausea = np.random.randint(0, 2)

        platelet_count = np.random.randint(150000, 450000)
        wbc_count = np.random.randint(4000, 11000)
        hemoglobin = round(np.random.uniform(11, 16), 1)
        hematocrit = round(np.random.uniform(35, 50), 1)

        rdt_malaria = 0
        dengue_ns1 = 0
        widal_test = 0

        if disease == "Dengue":
            platelet_count = np.random.randint(30000, 100000)
            rash = 1
            dengue_ns1 = 1

        elif disease == "Malaria":
            chills = 1
            rdt_malaria = 1
            hemoglobin = round(np.random.uniform(8, 12), 1)

        elif disease == "Typhoid":
            widal_test = 1

        elif disease == "Chikungunya":
            joint_pain = 1

        data.append([
            fever_temp, headache, chills, body_pain, joint_pain,
            nausea, rash, platelet_count, wbc_count,
            hemoglobin, hematocrit,
            rdt_malaria, dengue_ns1, widal_test, disease
        ])

columns = [
    "fever_temp","headache","chills","body_pain","joint_pain",
    "nausea","rash","platelet_count","wbc_count",
    "hemoglobin","hematocrit",
    "rdt_malaria","dengue_ns1","widal_test","disease"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("data/final_febrile_illness_dataset_1000.csv", index=False)

print("Dataset generated successfully.")
