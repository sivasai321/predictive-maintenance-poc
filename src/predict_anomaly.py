import pandas as pd
import joblib
import time
import datetime
import os
import sys
import logging
import csv

# -------------------------------
# Setup logging
# -------------------------------
logging.basicConfig(
    filename="../system.log",
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
MODEL_PATH = f"../{MODEL_PATH}"
SCALER_PATH = f"../{SCALER_PATH}"
LOG_PATH = f"../{LOG_PATH}"
OUTPUT_CSV = "../output.csv"

# -------------------------------
# Load model & scaler
# -------------------------------
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    logging.info("Model and scaler loaded successfully")
except Exception as e:
    logging.error(f"Error loading model/scaler: {e}")
    raise

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

# Validate data
if X.isnull().any().any():
    logging.warning("Missing values detected in input data")

# Scale
X_scaled = scaler.transform(X)

# -------------------------------
# Metrics tracking
# -------------------------------
total = 0
anomalies = 0

# -------------------------------
# Trend tracking
# -------------------------------
recent_scores = []

# Cooldown control
last_alert_time = 0
ALERT_COOLDOWN = 10

print("🚀 Starting anomaly detection...\n")

# -------------------------------
# CSV Output setup
# -------------------------------
with open(OUTPUT_CSV, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["timestamp", "row", "score", "avg_score", "status"])

    # -------------------------------
    # Logging file
    # -------------------------------
    with open(LOG_PATH, "a") as log_file:

        for i in range(len(X_scaled)):
            row = X_scaled[i].reshape(1, -1)

            try:
                # -------------------------------
                # Prediction
                # -------------------------------
                score = model.decision_function(row)[0]

                # -------------------------------
                # Trend tracking
                # -------------------------------
                recent_scores.append(score)
                if len(recent_scores) > WINDOW_SIZE:
                    recent_scores.pop(0)

                avg_score = sum(recent_scores) / len(recent_scores)

                # -------------------------------
                # Risk classification
                # -------------------------------
                if score < ANOMALY_THRESHOLD or avg_score < ANOMALY_THRESHOLD:
                    status = "HIGH RISK"
                    anomalies += 1
                elif score < MEDIUM_THRESHOLD:
                    status = "MEDIUM RISK"
                else:
                    status = "NORMAL"

                total += 1

                # -------------------------------
                # Console output
                # -------------------------------
                print(f"[{i}] {status} | Score: {score:.3f} | Avg: {avg_score:.3f}")

                # -------------------------------
                # CSV output 
                # -------------------------------
                timestamp = datetime.datetime.now()
                writer.writerow([timestamp, i, score, avg_score, status])

                # -------------------------------
                # Alert logic with cooldown
                # -------------------------------
                current_time = time.time()

                if (
                    status == "HIGH RISK"
                    and (current_time - last_alert_time > ALERT_COOLDOWN)
                ):
                    log_file.write(
                        f"{timestamp} | ALERT | row={i} | score={score:.3f} | avg={avg_score:.3f}\n"
                    )
                    log_file.flush()
                    logging.warning(f"High risk detected at row {i}")
                    last_alert_time = current_time

            except Exception as e:
                logging.error(f"Error processing row {i}: {e}")

            time.sleep(SLEEP_TIME)
# final metrics
if total > 0:
    anomaly_rate = anomalies / total
    print(f"\n📊 Total Processed: {total}")
    print(f"⚠️ Anomalies Detected: {anomalies}")
    print(f"📉 Anomaly Rate: {anomaly_rate:.2%}")

    logging.info(f"Run completed | Total={total} | Anomalies={anomalies} | Rate={anomaly_rate:.2%}")