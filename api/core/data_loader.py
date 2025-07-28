import pandas as pd
from pathlib import Path

def load_players_df(path="../data/processed/cleaned_data.csv") -> pd.DataFrame:
    return pd.read_csv(path)
