# src/data_loader.py
from pathlib import Path
import pandas as pd

# repo root = parent of src/
REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SAMPLE = REPO_ROOT / "data" / "sample_bikeshare.csv"

def load_local_sample(path: str | Path = DEFAULT_SAMPLE) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Missing sample data at {p.resolve()}")
    return pd.read_csv(p, parse_dates=["date"])

if __name__ == "__main__":
    df = load_local_sample()
    print(df.head())


