from fastapi import APIRouter

from pydantic import BaseModel
from typing import List, Union

from datetime import datetime, timezone, timedelta


router = APIRouter(
    prefix="/ExDevPlatform",
    tags=["ExDevPlatform"],
)


@router.get("/")
def hello():
    return {"hello": "platform"}
