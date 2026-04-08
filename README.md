# 🚀 Predictive Maintenance (Anomaly Detection PoC)

## 📌 Overview

This project demonstrates a **Predictive Maintenance System using Anomaly Detection**.

Instead of relying on historical failure labels, the system learns **normal machine behavior** from sensor data and detects **abnormal patterns** that may indicate potential issues.

---

## 🎯 Objective

To validate whether machine sensor data can be used to:

* Detect abnormal behavior without labeled failures
* Provide early warning signals
* Enable proactive maintenance
* Reduce unplanned downtime

---

## 🧠 Approach

### 🔄 Traditional Approach (Not Used Here)

* Requires labeled failure data
* Predicts failure probability

### ✅ Current Approach (Used)

* No labels required
* Learns normal behavior
* Detects anomalies

---

## ⚙️ Key Features

* 🔍 **Anomaly Detection using Isolation Forest**
* 📊 **Risk Classification (Normal / Medium / High)**
* ⏱️ **Simulated Real-Time Monitoring**
* 📈 **Trend-Based Analysis (sliding window)**
* ⚠️ **Configurable Alert System**
* 🪵 **Structured Logging + CSV Output**
* 🧠 **Completely Label-Free System**

---

## 🧱 Project Structure

```text
predictive-maintenance-poc/
│
├── data/
│   └── ai4i2020.csv
│
├── models/
│   ├── anomaly_model_v1.pkl
│   └── anomaly_scaler_v1.pkl
│
├── src/
│   ├── train_anomaly.py
│   └── predict_anomaly.py
│
├── config.py
├── system.log
├── alerts.log
├── output.csv
└── README.md
```

---

## 📦 Installation

```bash
git clone https://github.com/your-username/predictive-maintenance-poc.git
cd predictive-maintenance-poc
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Train the Anomaly Model

```bash
cd src
python train_anomaly.py
```

---

### 2. Run Real-Time Monitoring

```bash
python predict_anomaly.py
```

---

## 📊 Sample Output

```text
[50] 🔴 HIGH RISK | Score: -0.245 | Avg: -0.180
[51] 🟠 MEDIUM RISK | Score: -0.030 | Avg: -0.090
[52] 🟢 NORMAL | Score: 0.120 | Avg: 0.050
```

---

## 🧠 How It Works

1. Sensor data is preprocessed and normalized
2. Model learns baseline (normal) behavior
3. Incoming data is evaluated using anomaly score
4. Risk levels are assigned based on thresholds
5. Alerts are generated for abnormal conditions

---

## ⚙️ Configuration (`config.py`)

All system behavior is configurable:

* Data paths
* Simulation speed
* Anomaly thresholds
* Trend window size
* Alert cooldown

Example:

```python
ANOMALY_THRESHOLD = -0.1
MEDIUM_THRESHOLD = 0.0
WINDOW_SIZE = 5
ALERT_COOLDOWN = 10
```

---

## 🧾 Logging & Outputs

### 📁 Logs

* `system.log` → system events
* `alerts.log` → anomaly alerts

### 📊 CSV Output

* `output.csv` → structured predictions for analysis

---

## 📈 Model Details

* Algorithm: Isolation Forest
* Input Features:

  * Air temperature
  * Process temperature
  * Rotational speed
  * Torque
  * Tool wear
  * Machine type
* Output:

  * Anomaly score
  * Risk classification

---

## ⚠️ Important Notes

* This system detects **abnormal behavior**, not guaranteed failures
* Works without labeled failure data
* Suitable for early-stage monitoring systems

---

## 🔮 Future Improvements

* Real-time streaming integration (Kafka / MQTT)
* API deployment using FastAPI
* Interactive dashboard (Streamlit)
* Time-series anomaly models (LSTM / Autoencoder)
* Drift detection and retraining

---

## 🧠 Use Cases

* Industrial IoT monitoring
* CNC machines / motors / engines
* Manufacturing predictive maintenance
* Systems without labeled failure data

---

## 📬 Conclusion

This PoC demonstrates how anomaly detection can be used to transform raw sensor data into actionable insights, enabling **proactive monitoring without requiring historical failure labels**.

---

## 👨‍💻 Author

Siva Sai
