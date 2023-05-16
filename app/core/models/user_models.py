from .base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)
    favorites = relationship('FavoritesCrypto', backref='user', lazy='subquery')
    
