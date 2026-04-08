import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
import joblib
import os
import logging
import sys

# -------------------------------
# Setup logging
# -------------------------------
logging.basicConfig(
    filename="../train.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# -------------------------------
# Fix import path
# -------------------------------
sys.path.append(os.path.abspath(".."))
from config import *

# -------------------------------
# Paths
# -------------------------------
DATA_PATH = f"../{DATA_PATH}"
MODEL_PATH = "../models/anomaly_model_v1.pkl"
SCALER_PATH = "../models/anomaly_scaler_v1.pkl"

os.makedirs("../models", exist_ok=True)

# -------------------------------
# Load data
# -------------------------------
try:
    data = pd.read_csv(DATA_PATH)
    logging.info("Data loaded successfully")
except Exception as e:
    logging.error(f"Error loading data: {e}")
    raise

# -------------------------------
# Preprocessing
# -------------------------------
data = data.drop(columns=["UDI", "Product ID"], errors="ignore")
data["Type"] = data["Type"].map({"L": 0, "M": 1, "H": 2})

X = data.drop(
    columns=["Machine failure", "TWF", "HDF", "PWF", "OSF", "RNF"],
    errors="ignore"
)

# Validate
if X.isnull().any().any():
    logging.warning("Missing values found in dataset")

# -------------------------------
# Scaling
# -------------------------------
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------------
# Train anomaly model
# -------------------------------

model = IsolationForest(        
    contamination=CONTAMINATION,   # from config
    random_state=42,
    n_jobs=-1                      # use all CPU cores
)

model.fit(X_scaled)

# -------------------------------
# Basic training metrics
# -------------------------------
scores = model.decision_function(X_scaled)
avg_score = scores.mean()

logging.info(f"Training completed | Avg Score: {avg_score:.4f}")

# -------------------------------
# Save model
# -------------------------------
joblib.dump(model, MODEL_PATH)
joblib.dump(scaler, SCALER_PATH)

print("✅ Anomaly model trained and saved!")
logging.info("Model and scaler saved successfully")