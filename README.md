# 🚀 Predictive Maintenance PoC

## 📌 Overview

This project demonstrates a **Predictive Maintenance System** that analyzes machine sensor data to estimate failure risk and generate proactive alerts.

The system simulates real-time data ingestion and uses a machine learning model to classify machine health into actionable risk levels.

---

## 🎯 Objective

To validate whether sensor data (temperature, torque, wear, etc.) can be used to:

* Predict potential machine failures
* Enable proactive maintenance
* Reduce unplanned downtime

---

## ⚙️ Key Features

* 🔍 **Failure Prediction** using machine learning
* 📊 **Risk Classification** (Normal / Medium / High)
* ⏱️ **Simulated Real-Time Monitoring**
* 📈 **Trend Analysis** using recent risk history
* ⚠️ **Automated Alert Logging**
* ⚙️ **Configurable Thresholds & Settings**

---

## 🧠 How It Works

1. Historical sensor data is used to train a classification model
2. The model learns patterns associated with machine failure
3. Incoming data is processed in a simulated real-time loop
4. The system predicts failure probability for each data point
5. Risk levels are assigned and alerts are generated

---

## 🧱 Project Structure

```
predictive-maintenance-poc/
│
├── data/
│   └── ai4i2020.csv
│
├── models/
│   ├── model.pkl
│   └── scaler.pkl
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── config.py
├── requirements.txt
├── alerts.log
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

### 1. Train the Model

```bash
cd src
python train.py
```

### 2. Run Real-Time Simulation

```bash
python predict.py
```

---

## 📊 Sample Output

```
[12] 🟢 NORMAL | Current: 0.12 | Avg: 0.15
[13] 🟠 MEDIUM RISK | Current: 0.67 | Avg: 0.52
[14] 🔴 HIGH RISK | Current: 0.91 | Avg: 0.73
```

---

## ⚙️ Configuration

All configurable parameters are defined in `config.py`:

* Risk thresholds
* File paths
* Simulation interval

This allows easy tuning without modifying core logic.

---

## 🧾 Logging

Alerts are stored in `alerts.log` with timestamps:

```
2026-04-05 12:30:21 | ALERT at row 25 | risk=0.82
```

---

## 📈 Model Details

* Algorithm: Random Forest Classifier
* Input Features:

  * Air temperature
  * Process temperature
  * Rotational speed
  * Torque
  * Tool wear
* Output: Probability of machine failure

---

## ⚠️ Limitations

* Simulated real-time data (not live sensor feed)
* Basic model without hyperparameter tuning
* No deployment pipeline (PoC stage only)

---

## 🔮 Future Improvements

* Real-time streaming integration (Kafka / MQTT)
* API deployment using FastAPI
* Interactive dashboard (Streamlit)
* Advanced anomaly detection (no-label scenario)
* Model optimization and tuning

---

## 🧠 Use Cases

* Manufacturing equipment monitoring
* CNC machines / motors / engines
* Industrial IoT predictive systems

---

## 📬 Conclusion

This PoC demonstrates how machine learning can transform raw sensor data into actionable insights, enabling **predictive and proactive maintenance strategies**.

---

## 👨‍💻 Author

Siva Sai
