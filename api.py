# deploy/api.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import sqlite3
import json
from typing import List
from fastapi import FastAPI, HTTPException
import os, pandas as pd, joblib

app = FastAPI(title="Vault Health & Reserve Monitoring API")

# Model and data paths (project root)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODELS_DIR = os.path.join(BASE_DIR, "models")
DATA_DIR = os.path.join(BASE_DIR, "data")

RED_MODEL = os.path.join(MODELS_DIR, "redemption_model.pkl")
if not os.path.exists(RED_MODEL):
    raise FileNotFoundError(f"Model not found: {RED_MODEL}")
model = joblib.load(RED_MODEL)


# Load dataset (for partner scoring & forecast access)
CSV_PATH = os.path.join(DATA_DIR, "vault_transactions.csv")
if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH, parse_dates=["date"])
else:
    df = pd.DataFrame()

class PredictRequest(BaseModel):
    refill_amount: float
    net_change: float

@app.post("/predict_redemption")
def predict_redemption(req: PredictRequest):
    X = pd.DataFrame([req.dict()])
    pred = model.predict(X)[0]
    return {"predicted_redemption_amount": float(pred)}

@app.get("/partner_score")
def partner_scores():
    if df.empty:
        raise HTTPException(status_code=404, detail="Data not found")
    ps = df.groupby("partner_id").agg(
        total_redemption=("redemption_amount","sum"),
        total_refill=("refill_amount","sum"),
        avg_redemption=("redemption_amount","mean"),
        redemption_std=("redemption_amount","std")
    ).reset_index()
    # Simple normalized score
    ps['score'] = (ps['avg_redemption'] / ps['avg_redemption'].max()) - (ps['redemption_std'] / ps['redemption_std'].max())
    ps['score'] = ps['score'].fillna(0).round(3)
    return ps.to_dict(orient="records")

@app.get("/forecast/{vault_id}")
def get_forecast(vault_id: str):
    # try to load forecast file saved by retrain job
    fpath = os.path.join(MODELS_DIR, f"forecast_{vault_id}.parquet")
    if not os.path.exists(fpath):
        raise HTTPException(status_code=404, detail="Forecast not available. Run retrain/forecast job.")
    forecast = pd.read_parquet(fpath)
    return forecast.to_dict(orient="records")
