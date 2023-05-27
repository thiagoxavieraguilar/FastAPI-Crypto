from functools import lru_cache
from typing import Generator
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv



load_dotenv()

DB_NAME = os.environ.get('DB_NAME') 
MYSQL_USER = os.environ.get('MYSQL_USER') 
MYSQL_PASS = os.environ.get('MYSQL_PASS') 

#DATABASE_URL= f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@mysqldb:3306/{DB_NAME}"

DATABASE_URL= f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@localhost:3306/{DB_NAME}"

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