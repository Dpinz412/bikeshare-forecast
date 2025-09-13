\# Capital Bikeshare Demand Forecasting (Washington, DC)



\*\*What:\*\* Forecast daily pickups/dropoffs using weather + calendar features.

\*\*Why:\*\* Better staffing/rebalancing decisions; fewer stockouts.



\## Data

\- Capital Bikeshare rides (Feb–Apr 2024) + DC weather.

\- No raw data committed; use a small sample or a fetch script if needed.



\## Method

\- Feature engineering (weather, calendar, lags).

\- Models: regularized linear regression, kNN, decision tree, random forest, gradient boosting, simple NN.

\- Metrics: RMSE / MAE vs. baseline.



\## Quickstart

```bash

python -m venv .venv

\\# Windows PowerShell: .venv\\\\Scripts\\\\Activate.ps1

\\# Git Bash: source .venv/Scripts/activate

pip install -r requirements.txt

jupyter notebook notebooks/




