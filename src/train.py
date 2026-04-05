import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import joblib
import os
from sklearn.metrics import classification_report, confusion_matrix

# Paths
DATA_PATH = r"..\data\ai4i2020.csv"


MODEL_PATH = "../models/model.pkl"
SCALER_PATH = "../models/scaler.pkl"

# Ensure models folder exists
os.makedirs("../models", exist_ok=True)

# Load data
data = pd.read_csv(DATA_PATH)

# Drop useless columns
data = data.drop(columns=["UDI", "Product ID"])

# Encode categorical column
data["Type"] = data["Type"].map({"L": 0, "M": 1, "H": 2})

# Target
y = data["Machine failure"]

# Features (drop target + extra failure types)
X = data.drop(columns=["Machine failure", "TWF", "HDF", "PWF", "OSF", "RNF"])

# Normalize
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_scaled, y)

# Save model and scaler
joblib.dump(model, MODEL_PATH)
joblib.dump(scaler, SCALER_PATH)

print("✅ Model trained and saved successfully!")


y_pred = model.predict(X_scaled)

print("\n📊 Model Evaluation:")
print(confusion_matrix(y, y_pred))
print(classification_report(y, y_pred))