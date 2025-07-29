from core.data_loader import load_players_df
from models.players import Player
import numpy as np


def get_all_players() -> list[Player]:
    df = load_players_df()
    df = df.head(500)
    players = [Player(**row.to_dict()) for _, row in df.iterrows()]
    return players

def get_player_by_id(player_id: int) -> Player | None:
    df = load_players_df()
    row = df[df["ID"] == player_id]
    if row.empty:
        return None
    player_data = row.iloc[0].to_dict()
    return Player(**player_data)


def search_players(
        club: str = None,
        position: str = None,
        name: str = None,
        nationality: str = None,
        min_age: int = None,
        max_age: int = None,
        min_value: float = None,
        max_value: float = None,
    ) -> list[Player]:

    df = load_players_df()
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.fillna(0) 
    if club:
        df = df[df["Club"].str.contains(club, case=False, na=False)]
    if position:
        df = df[df["Position"].str.contains(position, case=False, na=False)]
    if name:
        df = df[df["Name"].str.contains(name, case=False, na=False)]
    if nationality:
        df = df[df["Nationality"].str.contains(nationality, case=False, na=False)]
    if min_age is not None:
        df = df[df["Age"] >= min_age]
    if max_age is not None:
        df = df[df["Age"] <= max_age]
    if min_value is not None:
        df = df[df["Value"] >= min_value]
    if max_value is not None:
        df = df[df["Value"] <= max_value]
    
    df = df.head(500)  
    players = [Player(**row.to_dict()) for _, row in df.iterrows()]
    return players
