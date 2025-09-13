# Capital Bikeshare Demand Forecasting (Washington, DC)

**What:** Forecast pickups (`PU_ct`) and dropoffs (`DO_ct`) for a specific Capital Bikeshare station using weather + calendar features.  
**Why:** Better rebalancing, staffing, and fewer stockouts at high-variance stations.

---

## Data

- **Scope:** Focused on **GWSB station “22nd & H St NW”**; merged time-indexed station counts with weather features.
- **Tables:** Pickup and dropoff aggregates → merged into a single fact table; external **weather** features added.
- **Fields (examples):** `PU_ct`, `DO_ct`, weather PCA components, date/time parts (derived).
- **Note:** Raw/full data is **not** committed. A tiny sample (for dev) can live under `data/` (gitignored).

---

## Questions

1) How well can we predict **pickups** and **dropoffs** from weather/time features?
2) Which models perform best on this station?
3) What’s the error range we should expect operationally?

---

## Pipeline

**A. Prep**
- Clean/aggregate **PU/DO** station counts
- Join with **weather** features
- Drop low-value columns, handle NAs

**B. Feature work**
- Calendar/time extractions
- **Dimensionality reduction** (PCA on weather-type features)
- Train/test split

**C. Modeling**
- Linear, **Lasso**, **Ridge**, **ElasticNet**
- **kNN**
- **Decision Tree**, **Random Forest**, **Gradient Boosting**
- **Neural Network** (shallow MLP)

**D. Eval**
- Compare **MSE** on test set (PU/DO separately)
- Report leaderboard + quick plots

---

## Repo layout

```bash
bikeshare-forecast/
README.md
requirements.txt
.gitignore
data/ # gitignored (put full/raw here locally)
src/
data_loader.py # robust pathing to sample/real data
... # helpers (features, models, metrics) if you add them
notebooks/
01_eda.ipynb
Assignment 3.ipynb # final analysis (rename if you prefer)
models/ # optional, gitignored
figures/ # optional, exported charts for README
```
---

## Quickstart
```bash
create env

python -m venv .venv

Git Bash:

source .venv/Scripts/activate

PowerShell:
.venv\Scripts\Activate.ps1
install deps

python -m pip install --upgrade pip
pip install -r requirements.txt

run notebooks

jupyter notebook

open notebooks/01_eda.ipynb (sanity) then Assignment 3.ipynb (full flow)

> Data goes under `data/` (gitignored). Keep raw CSVs out of git.
```
---

## Methods (nutshell)

- **Wrangling:** PU/DO merge → weather join → NA handling → drop leaky/low-signal columns
- **Feature engineering:** calendar/time parts; **PCA** on related weather features
- **Models:** Linear/Lasso/Ridge/**ElasticNet**, **kNN**, **Decision Tree**, **Random Forest**, **Gradient Boosting**, **Neural Net**
- **Metrics:** Test **MSE** per target (reporting both PU and DO)

---

## Results — model leaderboard (from notebook)

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

**Takeaways:**
- **ElasticNet** is best overall on both targets (lowest MSE on PU and DO).
- Linear/Ridge/ElasticNet cluster tightly → stable linear relationships + regularization helps a bit.
- Tree ensembles underperform here (likely limited station-level data + simple feature interactions).
- NN doesn’t beat linear baselines on this feature set/size.

> Source: `notebooks/Assignment 3.ipynb`.

---

## Reproducibility

- Pinned `requirements.txt`
- Numbered notebooks; run top-to-bottom
- `data/` kept local; loader resolves repo-relative paths

---


