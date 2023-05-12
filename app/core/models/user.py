from .base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    favorites = relationship('favorite', backref='user')