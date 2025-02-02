import pandas as pd
import numpy as np

np.random.seed(42)  # For reproducibility
n_patients = 10000

data = {
    'patient_id': range(1, n_patients+1),
    'age': np.random.normal(58, 15, n_patients).astype(int),  # Typical chronic care population
    'days_supply': np.random.choice([30, 60, 90, 100], n_patients, p=[0.6, 0.05, 0.3, 0.05]),  #observed_patterns
    'refill_gap_days': np.abs(np.round(np.random.normal(3, 2.5, n_patients))),
    'comorbidities': np.random.choice(
        ['N/A', 'I10.', 'E11.', 'E78.', 'ALL'], 
        n_patients, 
        p=[0.05, 0.15, 0.15, 0.15, 0.5]  #observed_diagnoses
    ),
    'prior_adherence': np.random.binomial(1, 0.65, n_patients),  #65%_baseline
    'sdoh_score': np.random.randint(1, 6, n_patients),  #social_determinates_scale
    'pharmacy_visits': np.random.poisson(4.2, n_patients),
    'insurance_type': np.random.choice(
        ['Commercial', 'Medicare', 'Medicaid', 'Cash'], 
        n_patients, 
        p=[0.40, 0.32, 0.20, 0.08 #payer_mix_percent
    )
}

df = pd.DataFrame(data)
df.to_csv('data/synthetic_patients.csv', index=False)
