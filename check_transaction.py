import joblib
import pandas as pd
import sys

# --- 1. Load the "brain" and "scaler" files ---
try:
    # This now loads your smart 'model_v3' brain
    model = joblib.load('fraud_detector_brain.joblib') 
    scaler = joblib.load('scaler.joblib')
except FileNotFoundError:
    print("\n--- ERROR ---")
    print("Could not find 'fraud_detector_brain.joblib' or 'scaler.joblib'.")
    print("Make sure they are in the same folder as this script.")
    sys.exit()

print("✅ Fraud detector (Smart Version) is armed and ready.\n")


# --- 2. Define the sample FRAUDULENT transaction ---
# This is the one our first model got wrong
raw_fraud_transaction = {
    'Time': 406.0,
    'V1': -2.312226542,
    'V2': 1.951992011,
    'V3': -1.609850732,
    'V4': 3.997905588,
    'V5': -0.522187865,
    'V6': -1.426545319,
    'V7': -2.537387306,
    'V8': 1.391657248,
    'V9': -2.770089273,
    'V10': -2.772272145,
    'V11': 3.202033207,
    'V12': -2.899907388,
    'V13': -0.595221881,
    'V14': -4.289253782,
    'V15': 0.38972412,
    'V16': -1.14074718,
    'V17': -2.830055675,
    'V18': -0.016822468,
    'V19': 0.416955705,
    'V20': 0.126910559,
    'V21': 0.517232371,
    'V22': -0.035049369,
    'V23': -0.465211076,
    'V24': 0.320198199,
    'V25': 0.044519167,
    'V26': 0.177839798,
    'V27': 0.261145003,
    'V28': -0.143275875,
    'Amount': 0.00
}


# --- 3. PREPARE the data just like we did in the notebook ---
df = pd.DataFrame([raw_fraud_transaction])

# Use our loaded 'scaler' to transform 'Amount' and 'Time'
df[['scaled_Amount', 'scaled_Time']] = scaler.transform(df[['Amount', 'Time']])

# Get the list of feature columns in the exact order the model expects
features_for_model = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28',
    'scaled_Amount', 'scaled_Time'
]

# Create the final DataFrame for the model
df_final = df[features_for_model]


# --- 4. Get the prediction ---
# The new model (Random Forest) outputs 0 (Normal) or 1 (Fraud)
prediction = model.predict(df_final)

# --- 5. Print the user-friendly result ---
print("--- Analyzing New Transaction ---")
print(f"Transaction Amount: ${raw_fraud_transaction['Amount']}")

if prediction[0] == 1: # 1 means Fraud for this new model
    print("\n***********************************")
    print(">>> 🚨 ALERT: FRAUD DETECTED! 🚨 <<<")
    print("***********************************")
else:
    print("\n=================================")
    print(">>> ✅ Transaction OK (Normal) ✅ <<<")
    print("=================================")