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


    def get_favorite_id(self,user_id: str, symbol: str) -> int:
        favorite = self.query().filter(FavoritesCrypto.user_id==user_id,FavoritesCrypto.symbol==symbol).one()
        return favorite.id
    
    def remove_favorite_on_db_repository(self,user_id: str, symbol: str) -> None:
        favorite_id = self.get_favorite_id(user_id=user_id,symbol=symbol)
        self.delete(id=favorite_id)
    
def get_favorite_repository(db: Session = Depends(get_session)) -> FavoriteRepository:
    return FavoriteRepository(FavoritesCrypto, db)