from functools import lru_cache
from typing import Generator
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy import create_engine
from .globals import DATABASE_URL


engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


@lru_cache
def create_session() -> scoped_session:
    Session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return Session


def get_session() -> Generator[scoped_session, None, None]:
    Session = create_session()

    try:
        yield Session
    finally:
        Session.remove()
