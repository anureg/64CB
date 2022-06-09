from fastapi import APIRouter

from pydantic import BaseModel
from typing import List, Union

from datetime import datetime, timezone, timedelta

# welcome สวัสดี ชั้นชื่อ..
# fallback ช่วยบอกอีกทีได้ไหม
# case1 card1
# case2 card2


# context
class Cardmessage(BaseModel):
    topic: str
    subtopic: Union[str, None] = None
    description: Union[str, None] = None

    location: Union[str, None] = None  # map
    buttonLink: List[str] = []  # button link url
    buttonPhone: List[str] = []  # button phone number
    buttonText: List[str] = []  # button text
    image: Union[str, None] = None  # picture

    file_path: Union[str, None] = None  # file


router = APIRouter(
    prefix="/ExDev",
    tags=["ExDev"],
)


@router.get("/welcome")
def welcome(device_id: str):
    # Time zone in Thailand UTC+7
    tz = timezone(timedelta(hours=7))
    # Create a date object with given timezone
    timestr = datetime.now(tz=tz).isoformat(sep=" ")
    # hash(device_id + timestr)
    token = hash(device_id + timestr)  # type token int

    textWelcome = 'สวัสดี ฉันคือ บอท \nมีอะไรให้ฉันช่วยไหม'

    context = Cardmessage(topic=textWelcome)
    return {
        "token": token,
        "Time": timestr,
        "context": context
    }


@router.get("/")
def chat():
    return
