from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI

from src.config import settings

engine = create_async_engine(settings.DB_URL)
new_async_session = async_sessionmaker(engine)

def get_db() -> Session:
    with new_async_session() as session:
        yield session
