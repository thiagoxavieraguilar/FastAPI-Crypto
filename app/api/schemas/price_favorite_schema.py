from pydantic import BaseModel
from typing import Union
from datetime import datetime


class PriceFavorite(BaseModel):
    symbol: str
    price: Union[float, str]
    date: datetime
