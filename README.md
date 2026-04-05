# Predictive Maintenance PoC

## Overview
This is a PoC simulating sensor ingestion every few seconds. The model evaluates failure probability and categorizes risk levels, enabling proactive maintenance decisions.

## Setup

1. Install dependencies:
pip install -r requirements.txt

2. Train model:
cd src
python train.py

3. Run live prediction:
python predict.py