from .base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
    #favorites = relationship('Favorite', backref='user', lazy='subquery')