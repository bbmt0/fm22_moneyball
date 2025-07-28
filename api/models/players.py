from pydantic import BaseModel

class Player(BaseModel):
    ID: int
    Name: str
    Age: int
    Club: str
    Division: str
    Rating: float | None = None
    Wage: float | None = None
