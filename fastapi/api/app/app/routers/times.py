from fastapi import APIRouter
import datetime

router = APIRouter()


@router.get("/times/", tags=["time"])
def get_times() -> str:
    time: str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return time
