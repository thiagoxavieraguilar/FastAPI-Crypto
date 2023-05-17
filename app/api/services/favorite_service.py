from app.core.repositories.favorite_repositorie import FavoriteRepository, get_favorite_repository
from typing import List, Optional, Tuple, Type
from sqlalchemy.exc import NoResultFound
from app.core.models.favorite_models import FavoritesCrypto
from app.api.services.base import Service 
from fastapi import Depends



class FavoriteService(Service):
    def __init__(self, repository: FavoriteRepository):
         super().__init__(repository)

    def create_favorite(self,symbol: str, quantity: float, user_id: int ) -> FavoritesCrypto:
          favorite = self.repository.create_favorite_repository(symbol=symbol,quantity=quantity,user_id=user_id)
          return favorite
    
    def create_favorite_on_db(self, favorite: Type[FavoritesCrypto]) -> None:
         self.repository.create_favorite_on_db_repository(favorite=favorite)

    def remove_favorite_on_db(self,user_id: str, symbol: str) -> FavoritesCrypto:
         self.repository.remove_favorite_on_db_repository(user_id=user_id,symbol=symbol)
       
  
    

def get_favorite_repository(favorite_repository: FavoriteRepository = Depends(get_favorite_repository)):
    return FavoriteService(repository=favorite_repository)