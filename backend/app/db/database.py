from typing import Any, Generator
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import Session
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine: Engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)

Base: Any = declarative_base()


def create_db_and_tables() -> None:
    from app.db.models.conversation import Conversation, Message
    from app.db.models.user import User

    Base.metadata.create_all(engine)


def get_db() -> Generator[Session, Any, None]:
    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()
