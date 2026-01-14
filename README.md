# Bike Share Demand Forecasting (Washington, DC)

Forecast station-level pickups and dropoffs to support rebalancing and operational planning.

**Project focus:** Capital Bikeshare station **“22nd & H St NW”** (Washington, DC)  
**Targets:** pickups (`PU_ct`) and dropoffs (`DO_ct`)  
**Inputs:** weather + calendar/time features

---

## Why this matters (decision context)

Bike share operations depend on having bikes and docks available when demand spikes. When demand is hard to predict, teams over-correct (extra truck routes, overtime) or under-serve (stockouts, empty docks).

This project builds a forecasting baseline that can be used to:
- anticipate high-demand windows at a specific station
- inform rebalancing plans and staffing
- reduce stockouts and missed trips at high-variance locations

---

## What I built

An end-to-end modeling pipeline that:
1. merges station counts with weather signals and calendar features  
2. engineers features and reduces weather dimensionality (PCA)  
3. trains multiple supervised models for both pickups and dropoffs  
4. evaluates performance using a consistent test split and error metrics

Deliverable: a reproducible notebook workflow with a model leaderboard and clear operational error ranges.

---

## Data

- **Scope:** One station (“22nd & H St NW”) with time-indexed pickup/dropoff counts
- **Join:** station counts merged with weather features
- **Feature examples:** calendar/time parts (hour, day-of-week, month), weather PCA components
- **Note on availability:** Full raw datasets are not committed to GitHub. Place local data files under `data/` (gitignored).

---

## Approach

### Feature engineering
- calendar/time extraction
- weather feature cleanup + PCA to capture correlated weather signals compactly
- handling missing values and removing low-signal columns

### Models tested
- Linear Regression, Lasso, Ridge, ElasticNet
- kNN
- Decision Tree, Random Forest, Gradient Boosting
- Shallow Neural Network (MLP)

### Evaluation
- Separate models for `PU_ct` and `DO_ct`
- Test-set MSE and RMSE reported for operational interpretability

---

## Results (model leaderboard)

| Model | MSE (PU_ct) | RMSE (PU_ct) | MSE (DO_ct) | RMSE (DO_ct) |
|---|---:|---:|---:|---:|
| Linear Regression | 55.58 | 7.46 | 69.55 | 8.34 |
| Lasso | 57.83 | 7.60 | 71.31 | 8.44 |
| Ridge | 55.57 | 7.45 | 69.54 | 8.34 |
| **ElasticNet** | **55.26** | **7.43** | **67.89** | **8.24** |
| kNN | 66.51 | 8.16 | 72.63 | 8.52 |
| Decision Tree | 133.40 | 11.55 | 95.93 | 9.79 |
| Random Forest | 73.24 | 8.56 | 89.88 | 9.48 |
| Gradient Boosting | 92.25 | 9.60 | 103.12 | 10.15 |
| Neural Network | 81.91 | 9.05 | 117.72 | 10.85 |

**Key takeaways**
- **ElasticNet** performed best overall for both pickups and dropoffs.
- Linear baselines were strong and stable, suggesting demand is largely explained by time and weather signals in a mostly linear way.
- Tree ensembles and the neural network did not outperform regularized linear models on this dataset and feature set.

> Source: `notebooks/Capital Bikeshare Analysis.ipynb`

---

## Repo structure

```bash
bikeshare-forecast/
  README.md
  requirements.txt
  .gitignore
  data/                # gitignored (place raw/full data here locally)
  notebooks/
    01_eda.ipynb
    Capital Bikeshare Analysis.ipynb
  src/                 # optional utilities if you extend the repo
    data_loader.py
  figures/             # optional (exported charts for README)
  models/              # optional (saved models; usually gitignored)
