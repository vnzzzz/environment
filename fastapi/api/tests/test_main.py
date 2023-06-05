import pytest
from fastapi.testclient import TestClient
import starlette.status

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm.session import close_all_sessions
from sqlalchemy.exc import SQLAlchemyError

from app.main import app
from app.db.database import get_db, Base


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


class SessionLocal(Session):
    def commit(self):
        self.flush()
        self.expire_all()


@pytest.fixture(scope="module")
def test_db():
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)

    TestSessionLocal = sessionmaker(class_=SessionLocal, autocommit=False, autoflush=False, bind=engine)

    db = TestSessionLocal()

    def get_db_for_testing():
        try:
            yield db
            db.commit()
        except SQLAlchemyError as e:
            assert e is not None
            db.rollback()

    app.dependency_overrides[get_db] = get_db_for_testing

    yield db

    db.rollback()
    close_all_sessions()
    engine.dispose()


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == starlette.status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}


def test_create_users(test_db: Session):
    email: str = "test1@example.com"
    password: str = "test1"
    response = client.post(
        "/users/",
        json={"email": email, "password": password},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    assert response.json()["email"] == email

    email: str = "test2@example.com"
    password: str = "test2"
    response = client.post(
        "/users/",
        json={"email": email, "password": password},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    assert response.json()["email"] == email


def test_create_duplicate_users(test_db: Session):
    email: str = "test1@example.com"
    password: str = "test1"
    response = client.post(
        "/users/",
        json={"email": email, "password": password},
    )
    assert response.status_code == starlette.status.HTTP_400_BAD_REQUEST


def test_read_users(test_db: Session):
    response = client.get("/users/")
    response_json = response.json()
    assert response.status_code == starlette.status.HTTP_200_OK
    assert len(response_json) == 2
