import pandas as pd
import joblib
import time
from config import *
import datetime

# Paths
DATA_PATH = f"../{DATA_PATH}"
MODEL_PATH = f"../{MODEL_PATH}"
SCALER_PATH = f"../{SCALER_PATH}"
LOG_PATH = f"../{LOG_PATH}"

# Load model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Load data
data = pd.read_csv(DATA_PATH)

# Preprocess
data = data.drop(columns=["UDI", "Product ID"])
data["Type"] = data["Type"].map({"L": 0, "M": 1, "H": 2})

X = data.drop(columns=["Machine failure", "TWF", "HDF", "PWF", "OSF", "RNF"])
X_scaled = scaler.transform(X)

# For trend tracking
recent_probs = []

print("🚀 Starting simulated real-time monitoring...\n")

# Open log file once
with open(LOG_PATH, "a") as log_file:  

    for i in range(len(X_scaled)):
        row = X_scaled[i].reshape(1, -1)

        prob = model.predict_proba(row)[0][1]

        # Track recent trend
        recent_probs.append(prob)
        if len(recent_probs) > 5:
            recent_probs.pop(0)

        avg_risk = sum(recent_probs) / len(recent_probs)

        # Risk classification
        if prob > THRESHOLD_HIGH:
            status = "🔴 HIGH RISK"
        elif prob > THRESHOLD_MEDIUM:
            status = "🟠 MEDIUM RISK"
        else:
            status = "🟢 NORMAL"

        print(f"[{i}] {status} | Current: {prob:.2f} | Avg: {avg_risk:.2f}")

        # Log alerts
        if prob > THRESHOLD_MEDIUM:
            log_file.write(f"{datetime.datetime.now()} | ALERT at row {i} | risk={prob:.2f}\n")


        time.sleep(SLEEP_TIME)