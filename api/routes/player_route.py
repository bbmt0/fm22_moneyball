from fastapi import APIRouter, HTTPException
from services.player_service import get_player_by_id
from models.players import Player

router = APIRouter()

@router.get("/{player_id}", response_model=Player)
def read_player(player_id: int):
    player = get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
