from pydantic import BaseModel


class FavoriteInput(BaseModel):
    symbol: str
    quantity: float
    user_id: int