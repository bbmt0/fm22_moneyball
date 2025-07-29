from fastapi import APIRouter, HTTPException, Query
from services.players_service import get_all_players, get_player_by_id, search_players
from models.players import Player
from typing import Optional

router = APIRouter()


@router.get("/", response_model=list[Player])
def route_get_all_players():
    return get_all_players()

@router.get("/search", response_model=list[Player])
def route_search_players(
        club: Optional[str] = Query(None),
        position: Optional[str] = Query(None),
        name: Optional[str] = Query(None),
        nationality: Optional[str] = Query(None),
        min_age: Optional[int] = Query(None),
        max_age: Optional[int] = Query(None),
        min_value: Optional[float] = Query(None),
        max_value: Optional[float] = Query(None),
    ): 
    players = search_players(
        club=club,
        position=position,
        name=name,
        nationality=nationality,
        min_age=min_age,
        max_age=max_age,
        min_value=min_value,
        max_value=max_value,
    )
    if not players:
        raise HTTPException(
            status_code=404,
            detail={
                "error_code": "NO_PLAYER_FOUND",
                "message": "No player found matching the search criteria."
            }
        )
    return players

@router.get("/{player_id}", response_model=Player)
def route_get_player_by_id(player_id: int):
    player = get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


