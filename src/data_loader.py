# src/data_loader.py
import os
import pandas as pd

def load_local_sample(path: str = "data/sample_bikeshare.csv") -> pd.DataFrame:
    """Load the tiny sample CSV (used for dev/testing)."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing sample data at {path}.")
    df = pd.read_csv(path, parse_dates=["date"])
    return df

if __name__ == "__main__":
    df = load_local_sample()
    print(df.head())
