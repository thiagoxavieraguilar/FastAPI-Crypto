from .base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class FavoritesCrypto(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(50), nullable=False)
    quantity = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

