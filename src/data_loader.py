import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")

def load_movies():
    return pd.read_csv(DATA_DIR / "movies.csv")

def load_ratings():
    return pd.read_csv("data/raw/ratings_reduced.csv")
