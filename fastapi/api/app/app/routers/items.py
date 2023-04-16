from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from ..db import crud, models, schemas
from ..db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/items/", response_model=list[schemas.Item], tags=["items"])
def read_items(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/items/id/{item_id}", tags=["items"])
async def read_item(item_id: int):
    return {"item_id": item_id}
