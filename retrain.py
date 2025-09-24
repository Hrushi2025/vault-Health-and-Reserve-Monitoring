# deploy/retrain.py
import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from deploy.alerts import send_slack, send_email


# Directories
BASE_DIR = os.path.abspath(os.path.join(os.getcwd()))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODELS_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODELS_DIR, exist_ok=True)

# Load dataset
DATA_PATH = os.path.join(DATA_DIR, "vault_transactions.csv")
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Data file not found: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

# Simple feature engineering
df['net_change'] = df['refill_amount'] - df['redemption_amount']

X = df[['refill_amount', 'net_change']]
y = df['redemption_amount']

# Train RandomForest model
model = RandomForestRegressor(n_estimators=50, random_state=42)
model.fit(X, y)

# Save model
MODEL_PATH = os.path.join(MODELS_DIR, "redemption_model.pkl")
joblib.dump(model, MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")

# Example alert logic
avg_redemption = df['redemption_amount'].mean()
if avg_redemption > 1000:  # Threshold example
    send_slack(f"Average redemption high: {avg_redemption:.2f}")
    send_email(
        subject="Vault Alert: High Redemption",
        body=f"The average redemption amount is {avg_redemption:.2f}",
        to="admin@example.com"
    )

print("Retraining and alert process complete.")
