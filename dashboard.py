# deploy/dashboard.py
import streamlit as st
import requests
import pandas as pd
import os

API_BASE = st.sidebar.text_input("API base URL", "http://127.0.0.1:8000")

st.title("Vault Health & Reserve Monitoring — Admin Dashboard")

# Partner scores
st.header("Partner Performance Scores")
try:
    r = requests.get(f"{API_BASE}/partner_score", timeout=10)
    ps = pd.DataFrame(r.json())
    st.dataframe(ps)
    st.bar_chart(ps.set_index("partner_id")["score"])
except Exception as e:
    st.error(f"Could not fetch partner scores: {e}")

# Redemption prediction example
st.header("Redemption Prediction (sample)")
refill = st.number_input("Refill amount", value=1500)
net_change = st.number_input("Net change (refill - redemption)", value=-500)
if st.button("Predict Redemption"):
    payload = {"refill_amount": float(refill), "net_change": float(net_change)}
    try:
        r = requests.post(f"{API_BASE}/predict_redemption", json=payload, timeout=10)
        st.success(f"Predicted redemption: {r.json()['predicted_redemption_amount']:.2f}")
    except Exception as e:
        st.error(f"Error calling API: {e}")

# Forecast viewer
st.header("Vault Forecast")
vault_id = st.selectbox("Select vault", options=["V100","V101","V102","V103","V104"])
if st.button("Load Forecast"):
    try:
        r = requests.get(f"{API_BASE}/forecast/{vault_id}", timeout=10)
        forecast = pd.DataFrame(r.json())
        forecast['ds'] = pd.to_datetime(forecast['ds'])
        st.line_chart(forecast.set_index('ds')['yhat'])
    except Exception as e:
        st.error(f"Could not load forecast: {e}")
