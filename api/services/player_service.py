from core.data_loader import load_players_df
from models.players import Player

def get_player_by_id(player_id: int) -> Player | None:
    df = load_players_df()
    row = df[df["ID"] == player_id]
    if row.empty:
        return None
    player_data = row.iloc[0].to_dict()
    return Player(**player_data)
