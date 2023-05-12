from .base import Base
from sqlalchemy import Column, String, Integer


class FavoriteModel(Base):
    id = Column('id',Integer,primary_key=True)