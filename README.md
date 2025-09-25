Vault Health & Reserve Monitoring

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/05771e1a-ebcf-4d67-ab60-2ff9cbf4d3fe" />


An AI-powered system to monitor vault health, predict redemption surges, detect liquidity gaps, and assess partner performance with dashboards, alerts, and automated retraining.

Project Description

This project simulates a real-world vault monitoring system. It generates synthetic vault transaction data, trains machine learning models, forecasts liquidity, scores vault partners, and provides predictions and visualizations via a dashboard.

It is designed to help admins make informed decisions, predict high redemptions, detect gaps in vault reserves, and monitor partner vaults.

Key Features

Redemption Surge Prediction: Predict upcoming redemption amounts using RandomForest regression.

Liquidity Gap Detection: Detect potential liquidity gaps with time-series forecasts (Prophet).

Partner Vault Scoring: Evaluate vault partners based on redemption/refill patterns.

Automated Alerts: Send Slack/email alerts if thresholds are exceeded.

Interactive Dashboard: Streamlit dashboard for admins to visualize metrics and predictions.

Retraining Pipeline: Periodic retraining updates models with latest data.

Technology Stack
Component	Technology / Library
ML/AI	Python, scikit-learn, Prophet, XGBoost
Data	Pandas, NumPy, SQLAlchemy, MySQL
API	FastAPI
Dashboard	Streamlit
Notifications	Slack API, SMTP (email alerts)
Deployment	CMD/Terminal, Docker (optional)
Environment	Python virtualenv (.venv)
Project Structure
Vault Health & Reserve Monitoring/
Vault Health & Reserve Monitoring

An AI-powered system to monitor vault health, predict redemption surges, detect liquidity gaps, and assess partner performance with dashboards, alerts, and automated retraining.

Project Description

This project simulates a real-world vault monitoring system. It generates synthetic vault transaction data, trains machine learning models, forecasts liquidity, scores vault partners, and provides predictions and visualizations via a dashboard.

It is designed to help admins make informed decisions, predict high redemptions, detect gaps in vault reserves, and monitor partner vaults.

Key Features

Redemption Surge Prediction: Predict upcoming redemption amounts using RandomForest regression.

Liquidity Gap Detection: Detect potential liquidity gaps with time-series forecasts (Prophet).

Partner Vault Scoring: Evaluate vault partners based on redemption/refill patterns.

Automated Alerts: Send Slack/email alerts if thresholds are exceeded.

Interactive Dashboard: Streamlit dashboard for admins to visualize metrics and predictions.

Retraining Pipeline: Periodic retraining updates models with latest data.

Technology Stack
Component	Technology / Library
ML/AI	Python, scikit-learn, Prophet, XGBoost
Data	Pandas, NumPy, SQLAlchemy, MySQL
API	FastAPI
Dashboard	Streamlit
Notifications	Slack API, SMTP (email alerts)
Deployment	CMD/Terminal, Docker (optional)
Environment	Python virtualenv (.venv)
Project Structure
Vault Health & Reserve Monitoring/


<img width="1184" height="864" alt="aifiesta-download-1758790012596" src="https://github.com/user-attachments/assets/0db8e290-cac0-4609-8d34-943a116d752b" />

Step-by-Step Implementation (What i Did)
1. Project Setup

Created main project folder: Vault Health & Reserve Monitoring.

Virtual environment .venv created for dependency management.

Installed Python packages: pandas, numpy, scikit-learn, prophet, xgboost, fastapi, uvicorn, streamlit, joblib.

2. Data Generation

Generated synthetic vault transaction data:

Columns: date, vault_id, partner_id, redemption_amount, refill_amount.

Stored in data/vault_transactions.csv.

3. Database Integration

Connected to MySQL to store and query transactions.

Used SQLAlchemy for safe database connection.

Loaded synthetic data automatically into MySQL tables.

4. Data Preprocessing & Feature Engineering

Processed transaction data for:

Redemption prediction.

Partner performance scoring.

Time-series forecasting.

5. ML Model Training

RandomForest Regression trained to predict redemption surges.

Prophet model trained for liquidity/forecasting.

Models saved in models/ folder (redemption_model.pkl).

Example predictions performed to verify model performance.

6. Retraining & Alerts

retrain.py script:

Retrains models periodically.

Sends Slack/email alerts if thresholds exceeded.

Stores updated models and forecasts.

7. Deployment & Visualization

FastAPI (deploy/api.py)

Endpoints for predictions, partner scores, and vault forecasts.

Streamlit Dashboard (deploy/dashboard.py)

Interactive admin dashboard.

Partner performance table and chart.

Redemption prediction input & result.

Vault forecast visualization.

CMD/Terminal

FastAPI server: uvicorn deploy.api:app --reload.

Streamlit dashboard: streamlit run deploy/dashboard.py.

Commands executed separately for API and dashboard.

Optional / Next Steps (Production-Ready)

API Enhancements: Serve all predictions and forecasts through REST endpoints.

Dashboard Improvements: Add filtering, historical charts, and more visual insights.

Alerts / Notifications: Advanced alert logic for multiple thresholds.

Model Evaluation: Store metrics (R², MAE, RMSE) and automated model comparison.

Automated Retraining & CI/CD: Dockerize API/dashboard, schedule retraining.

Monitoring: Integrate Grafana/Prometheus for model and system metrics.

Usage Instructions

Clone the repository.

Create a virtual environment and install dependencies:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt


Generate or load synthetic data in data/.

Run Jupyter notebook notebooks/setupOfProject.ipynb to train models and visualize results.

Start FastAPI server:

uvicorn deploy.api:app --reload


Open Streamlit dashboard:

streamlit run deploy/dashboard.py


Interact with the dashboard and API.

Project Overview (Detailed)

Vault Health & Reserve Monitoring is a full-stack AI project designed to simulate real-time vault management:

Synthetic Data Simulation – We generate realistic transactions for multiple vaults and partners.

Database Management – MySQL stores data for querying, analysis, and feeding ML models.

Machine Learning – RandomForest predicts redemptions; Prophet forecasts liquidity gaps.

Automated Retraining – retrain.py updates models with new data and triggers alerts.

REST API – FastAPI exposes endpoints for integration with apps or dashboards.

Interactive Visualization – Streamlit provides a friendly admin interface.

Deployment – CMD/terminal commands launch both API and dashboard, ensuring modularity.

Optional production-ready steps like Dockerization, CI/CD, monitoring, and advanced alerting are also included for future scaling.

Outcome / Deliverables

Trained models (redemption_model.pkl).

Synthetic dataset (vault_transactions.csv).

Jupyter notebook (setupOfProject.ipynb) with full ML pipeline.

REST API for predictions.

Interactive Streamlit dashboard.

Alerts via Slack/email.

Deployment-ready structure for future production.

Step-by-Step Implementation (What We Did)
1. Project Setup

Created main project folder: Vault Health & Reserve Monitoring.

Virtual environment .venv created for dependency management.

Installed Python packages: pandas, numpy, scikit-learn, prophet, xgboost, fastapi, uvicorn, streamlit, joblib.

2. Data Generation

Generated synthetic vault transaction data:

Columns: date, vault_id, partner_id, redemption_amount, refill_amount.

Stored in data/vault_transactions.csv.

3. Database Integration

Connected to MySQL to store and query transactions.

Used SQLAlchemy for safe database connection.

Loaded synthetic data automatically into MySQL tables.

4. Data Preprocessing & Feature Engineering

Processed transaction data for:

Redemption prediction.

Partner performance scoring.

Time-series forecasting.

5. ML Model Training

RandomForest Regression trained to predict redemption surges.

Prophet model trained for liquidity/forecasting.

Models saved in models/ folder (redemption_model.pkl).

Example predictions performed to verify model performance.

6. Retraining & Alerts

retrain.py script:

Retrains models periodically.

Sends Slack/email alerts if thresholds exceeded.

Stores updated models and forecasts.

7. Deployment & Visualization

FastAPI (deploy/api.py)

Endpoints for predictions, partner scores, and vault forecasts.

Streamlit Dashboard (deploy/dashboard.py)

Interactive admin dashboard.

Partner performance table and chart.

Redemption prediction input & result.

Vault forecast visualization.

CMD/Terminal

FastAPI server: uvicorn deploy.api:app --reload.

Streamlit dashboard: streamlit run deploy/dashboard.py.

Commands executed separately for API and dashboard.

Optional / Next Steps (Production-Ready)

API Enhancements: Serve all predictions and forecasts through REST endpoints.

Dashboard Improvements: Add filtering, historical charts, and more visual insights.

Alerts / Notifications: Advanced alert logic for multiple thresholds.

Model Evaluation: Store metrics (R², MAE, RMSE) and automated model comparison.

Automated Retraining & CI/CD: Dockerize API/dashboard, schedule retraining.

Monitoring: Integrate Grafana/Prometheus for model and system metrics.

Usage Instructions

Clone the repository.

Create a virtual environment and install dependencies:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt


Generate or load synthetic data in data/.

Run Jupyter notebook notebooks/setupOfProject.ipynb to train models and visualize results.

Start FastAPI server:

uvicorn deploy.api:app --reload


Open Streamlit dashboard:

streamlit run deploy/dashboard.py


Interact with the dashboard and API.

Project Overview (Detailed)

Vault Health & Reserve Monitoring is a full-stack AI project designed to simulate real-time vault management:

Synthetic Data Simulation – We generate realistic transactions for multiple vaults and partners.

Database Management – MySQL stores data for querying, analysis, and feeding ML models.

Machine Learning – RandomForest predicts redemptions; Prophet forecasts liquidity gaps.

Automated Retraining – retrain.py updates models with new data and triggers alerts.

REST API – FastAPI exposes endpoints for integration with apps or dashboards.

Interactive Visualization – Streamlit provides a friendly admin interface.

Deployment – CMD/terminal commands launch both API and dashboard, ensuring modularity.

Optional production-ready steps like Dockerization, CI/CD, monitoring, and advanced alerting are also included for future scaling.

Outcome / Deliverables

Trained models (redemption_model.pkl).

Synthetic dataset (vault_transactions.csv).

Jupyter notebook (setupOfProject.ipynb) with full ML pipeline.

REST API for predictions.

Interactive Streamlit dashboard.

Alerts via Slack/email.

Deployment-ready structure for future production.
