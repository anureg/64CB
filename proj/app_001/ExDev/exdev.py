from fastapi import APIRouter

from pydantic import BaseModel
from typing import List, Union

from datetime import datetime, timezone, timedelta


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


@router.get("/ChatMsg")
def chat_msg(msg: str, device_token: int, contextSend: str):

    if msg == 'greeting':
        contextAns = Cardmessage(
            topic='สวัสดีครับ',
        )
    elif msg == 'ช่องทางการติดต่อ':
        contextAns = Cardmessage(
            topic='ช่องทางการติดต่อ',
            subtopic='คลิกเลือกรายการที่ต้องการ :',
            buttonText=[
                'ที่ทำการ',
                'ที่ทำการ',
                'โทรศัพท์',
                'โทรศัพท์',
                'โทรสาร',
                'โทรสาร',
            ],
        )
    elif msg == 'โทรศัพท์':
        contextAns = Cardmessage(
            topic='โทรศัพท์',
            subtopic='หมายเลข 0 2831 9888\nวันและเวลาราชการ (08.30-16.30)',
            buttonPhone=[
                'โทรออก',
                '028319888',
            ],
        )

    else:
        contextAns = Cardmessage(
            topic='ขออภัย กรุณาบอกใหม่อีกครั้ง',
            subtopic='หรือลองดูบริการจากเมนูไหม ?',
            buttonText=[
                'ไปที่เมนู',
                'ไปที่เมนู',
            ],
        )

    return {
        "token": device_token,
        "TimeSend": "2022-06-07 15:04:58.408218+07:00",
        "TimeAns": "2022-06-07 15:04:58.408218+07:00",
        "msgSend": msg,
        "context": contextAns
    }
