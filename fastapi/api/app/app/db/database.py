from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy import create_engine
import os

# ---- sqlite ----
# SQLALCHEMY_DATABASE_URL = "sqlite:///./app/db/sqlite.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# ---- postgres ----
# DB_USER = os.environ.get("DB_USER", "fastapi")
# DB_PASSWORD = os.environ.get("DB_PASSWORD", "fastapi")
# DB_HOST = os.environ.get("DB_HOST", "db")
# DB_PORT = os.environ.get("DB_PORT", "5432")
# DB_DB = os.environ.get("DB_DATABASE", "fastapi")
# SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
#     DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE
# )
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# ---- mysql ----
DB_USER = os.environ.get("DB_USER", "fastapi")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "fastapi")
DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = os.environ.get("DB_PORT", "3306")
DB_DATABASE = os.environ.get("DB_DATABASE", "fastapi")
SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
