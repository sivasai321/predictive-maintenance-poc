# 🚀 Predictive Maintenance System (PoC)

> Transforming raw machine sensor data into **actionable insights** for proactive maintenance.

---

## 🧠 Overview

This project demonstrates a **Predictive Maintenance System** that monitors machine sensor data and identifies potential failures **before they occur**.

It supports two approaches:

* ✅ **Supervised Learning** → Predict failure (when labels exist)
* ⚡ **Anomaly Detection** → Detect abnormal behavior (no labels required)

---

## 🎯 Problem Statement

Machines generate continuous sensor data (temperature, torque, speed, etc.), but without predictive insights:

* ❌ Maintenance is reactive
* ❌ Downtime is unpredictable
* ❌ Costs increase

👉 This system enables **early detection of risk** using machine learning.

---

## ⚙️ Features

✨ Real-time risk monitoring (simulated)
📊 Failure probability prediction
🚨 Anomaly detection (no labels required)
📈 Trend-based risk analysis
🧾 Alert logging with timestamps
⚙️ Configurable thresholds

---

## 🧱 Architecture

```text
Sensors/Data → Preprocessing → Model → Risk Engine → Alerts/Logs
```

---

## 🔄 System Flow

```text
Historical Data
     ↓
Model Training
     ↓
Saved Model (model.pkl)
     ↓
Incoming Sensor Data (simulated)
     ↓
Prediction / Anomaly Detection
     ↓
Risk Classification
     ↓
Alerts + Logs
```

---

## 📂 Project Structure

```bash
predictive-maintenance-poc/
│
├── data/
│   └── ai4i2020.csv
│
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── anomaly_model.pkl
│   └── anomaly_scaler.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── train_anomaly.py
│   └── predict_anomaly.py
│
├── config.py
├── requirements.txt
├── alerts.log
└── README.md
```

---

## 🧠 Models Used

### 🌳 Random Forest (Supervised)

* Predicts machine failure probability
* Works well with tabular sensor data

---

### 🌲 Isolation Forest (Unsupervised)

* Detects anomalies without labels
* Flags unusual machine behavior

---

## ▶️ Getting Started

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Train model

```bash
cd src
python train.py
```

---

### 3️⃣ Run real-time monitoring

```bash
python predict.py
```

---

### 4️⃣ Run anomaly detection

```bash
python predict_anomaly.py
```

---

## 📊 Sample Output

```text
[50] 🔴 HIGH RISK | Current: 0.98 | Avg: 0.20
[51] 🟢 NORMAL | Current: 0.00 | Avg: 0.20
[52] 🟠 MEDIUM RISK | Current: 0.65 | Avg: 0.40
```

---

## ⚙️ Configuration

Modify `config.py`:

* Risk thresholds
* File paths
* Simulation interval

---

## 🧾 Logging

Alerts are stored in:

```text
alerts.log
```

Example:

```text
2026-04-10 12:30:21 | ALERT at row 50 | risk=0.98
```

---

## 📈 Key Concepts

* **Predictive Maintenance** → Predict failures before they occur
* **Anomaly Detection** → Identify unusual patterns
* **Trend Analysis** → Capture gradual degradation

---

## ⚖️ Why This Approach?

✔ Lightweight & fast
✔ Works on standard machines
✔ Easy to scale
✔ No dependency on deep learning

---

## 🚀 Future Improvements

* 🌐 API deployment using FastAPI
* 📊 Dashboard using Streamlit
* 📡 Real-time streaming (Kafka/MQTT)
* 🧠 Advanced models (Autoencoders, LSTM)
* 📈 Visualization of risk trends

---

## 🧠 Key Insight

> “Start simple, validate the concept, then scale the system.”

---

## 👨‍💻 Author

Siva Sai

---

## ⭐ If you found this useful

Give it a star on GitHub ⭐
