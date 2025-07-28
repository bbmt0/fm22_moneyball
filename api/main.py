from fastapi import FastAPI

app = FastAPI(title="FM Moneyball API", version="1.0.0")

from fastapi import APIRouter
from routes import player_route

@app.get("/")
def index():
    return {"message": "Salut"}

app.include_router(player_route.router, prefix="/players", tags=["Players"])

