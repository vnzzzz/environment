import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# ---- mysql ----
DB_USER = os.environ.get("DB_USER", "fastapi")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "fastapi")
DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = os.environ.get("DB_PORT", "3306")
DB_DATABASE = os.environ.get("DB_DATABASE", "fastapi")

SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}".format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
