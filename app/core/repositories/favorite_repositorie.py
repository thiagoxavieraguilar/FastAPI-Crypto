from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.models.favorite_models import FavoritesCrypto
from app.db.config import get_session

from .base import BaseRepository
from typing  import  Type


class FavoriteRepository(BaseRepository):
    """User Repository is an interface to the database."""


    def create_favorite_repository(self, symbol: str, quantity: float, user_id: int ) -> FavoritesCrypto:
        return FavoritesCrypto(symbol=symbol,quantity=quantity,user_id=user_id)

      
    def create_favorite_on_db_repository(self, favorite: Type[FavoritesCrypto]) -> None:
         self.create(favorite)


    
    
def get_favorite_repository(db: Session = Depends(get_session)) -> FavoriteRepository:
    return FavoriteRepository(FavoritesCrypto, db)