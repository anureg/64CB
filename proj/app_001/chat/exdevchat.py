from fastapi import APIRouter

from fastapi.responses import FileResponse
import os

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
    prefix="/ExDevChat",
    tags=["ExDevChat"],
)


@router.get("/welcome")
def welcome(device_id: str):
    # Time zone in Thailand UTC+7
    tz = timezone(timedelta(hours=7))
    # Create a date object with given timezone
    timestr = datetime.now(tz=tz).isoformat(sep=" ")
    # hash(device_id + timestr)
    token = hash(device_id + timestr)  # type token int

    context = Cardmessage(
        topic='สวัสดี ฉันคือ บอท',
        subtopic='มีอะไรให้ฉันช่วยไหม',
    )

    return {
        "token": token,
        "Time": timestr,
        "context": context
    }


@router.get("/ChatMsg")
def chat_msg(msg: str, device_token: int, contextSend: str):

    if msg == 'text':
        contextAns = Cardmessage(
            topic='ข้อความ',
        )
    elif msg == 'case1':
        contextAns = Cardmessage(
            topic='card1',
            subtopic='คลิกเลือก website ที่ต้องการ :',
            buttonText=[
                'เข้าสู่เว็บไซต์ google',
                'https://www.google.com/',
                'เข้าสู่เว็บไซต์ youtube',
                'https://www.youtube.com/',
            ],
        )
    elif msg == 'case2':
        contextAns = Cardmessage(
            topic='card2',
            subtopic='คลิกเลือกรายการที่ต้องการ :',
            buttonText=[
                'select item 1',
                'show item 1',
                'select item 2',
                'show item 2',
                'select item 3',
                'show item 3',
            ],
        )
    elif msg == 'case3':
        contextAns = Cardmessage(
            topic='card3',
            subtopic='หมายเลข 0 2831 9888\nวันและเวลาราชการ (08.30-16.30)',
            buttonPhone=[
                'โทรออก',
                '028319888',
            ],
        )
    elif msg == 'case5':
        contextAns = Cardmessage(
            topic='test_pdf.pdf',
            file_path='test_pdf.pdf'
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
        "TimeSend": datetime.now(tz=timezone(timedelta(hours=7))).isoformat(sep=" "),
        "TimeAns": "2022-06-07 15:04:58.408218+07:00",
        "msgSend": msg,
        "context": contextAns
    }


# REF: https://www.youtube.com/watch?v=vpTAqnAbowo
path_files_in_github = "/app/proj/app_001/platform/files/"


@router.get("/GetFile")
def get_file(file_name: str, device_token: int):
    file_path = os.path.join(path_files_in_github, file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found!"}
