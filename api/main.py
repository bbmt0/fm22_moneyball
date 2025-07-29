from fastapi import FastAPI

app = FastAPI(title="FM Moneyball API", version="1.0.0")

from fastapi import APIRouter
from routes import players_route

@app.get("/")
def index():
    return {"message": "Salut"}


app.include_router(players_route.router, prefix="/players", tags=["Players"])
