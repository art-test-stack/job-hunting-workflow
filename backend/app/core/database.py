# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, DeclarativeBase
# from app.core.config import settings

# class Base(DeclarativeBase):
#     pass

# engine = create_engine(settings.db_url, echo=False)
# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from app.core.config import settings
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated


connect_args = {"check_same_thread": False}
engine = create_engine(settings.db_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]