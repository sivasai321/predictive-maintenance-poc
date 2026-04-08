# -------------------------------
# Paths
# -------------------------------
DATA_PATH = "data/ai4i2020.csv"
MODEL_PATH = "models/anomaly_model_v1.pkl"
SCALER_PATH = "models/anomaly_scaler_v1.pkl"
LOG_PATH = "alerts.log"

# -------------------------------
# Simulation settings
# -------------------------------
SLEEP_TIME = 2   # seconds between data points

# -------------------------------
# Anomaly detection settings
# -------------------------------
CONTAMINATION = 0.05   # expected % anomalies

# Score thresholds (tune if needed)
ANOMALY_THRESHOLD = -0.1
MEDIUM_THRESHOLD = 0.0
# -------------------------------
# Trend settings
# -------------------------------
WINDOW_SIZE = 5