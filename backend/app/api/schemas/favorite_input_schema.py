from pydantic import BaseModel


class FavoriteInput(BaseModel):
    symbol: str
