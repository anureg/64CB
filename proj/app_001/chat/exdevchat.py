from fastapi import APIRouter

from fastapi.responses import FileResponse
import os

from pydantic import BaseModel
from typing import Union

from datetime import datetime, timezone, timedelta


# button
class ButtonMsg(BaseModel):
    button_type: str  # Link, Phone, Text

    button_name: str
    button_value: str


# context
class Cardmessage(BaseModel):
    topic: str
    subtopic: Union[str, None] = None
    description: Union[str, None] = None

    location: Union[str, None] = None  # map
    button: Union[list[dict], None] = None  # ButtonMsg
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
        topic="สวัสดี ฉันคือ บอท",
        subtopic="มีอะไรให้ฉันช่วยไหม",
    )

    return {"token": token, "Time": timestr, "context": context}


@router.get("/ChatMsg")
def chat_msg(msg: str, device_token: int, contextSend: str):

    if msg == "text":
        contextAns = [
            Cardmessage(
                topic="ข้อความ",
            )
        ]
    elif msg == "case1":
        contextAns = [
            Cardmessage(
                topic="card1",
                subtopic="คลิกเลือก website ที่ต้องการ :",
                button=[
                    ButtonMsg(
                        button_type="Link",
                        button_name="เข้าสู่เว็บไซต์ google",
                        button_value="https://www.google.com/",
                    ),
                    ButtonMsg(
                        button_type="Link",
                        button_name="เข้าสู่เว็บไซต์ youtube",
                        button_value="https://www.youtube.com/",
                    ),
                ],
            )
        ]
    elif msg == "case2":
        contextAns = [
            Cardmessage(
                topic="card2",
                subtopic="คลิกเลือกรายการที่ต้องการ :",
                button=[
                    ButtonMsg(
                        button_type="Text",
                        button_name="select item 1",
                        button_value="show item 1",
                    ),
                    ButtonMsg(
                        button_type="Text",
                        button_name="select item 2",
                        button_value="show item 2",
                    ),
                    ButtonMsg(
                        button_type="Text",
                        button_name="select item 3",
                        button_value="show item 3",
                    ),
                ],
            )
        ]
    elif msg == "case3":
        contextAns = [
            Cardmessage(
                topic="card3",
                subtopic="หมายเลข 0 2831 9888\nวันและเวลาราชการ (08.30-16.30)",
                button=[
                    ButtonMsg(
                        button_type="Phone",
                        button_name="โทรออก",
                        button_value="028319888",
                    ),
                ],
            )
        ]
    elif msg == "case5":
        contextAns = [Cardmessage(topic="test_pdf.pdf", file_path="test_pdf.pdf")]

    else:
        contextAns = [
            Cardmessage(
                topic="ขออภัย กรุณาบอกใหม่อีกครั้ง",
            ),
            Cardmessage(
                topic="หรือลองดูบริการจากเมนูไหม ?",
                button=[
                    ButtonMsg(
                        button_type="Text",
                        button_name="ไปที่เมนู1",
                        button_value="ไปที่เมนู1",
                    ),
                    ButtonMsg(
                        button_type="Link",
                        button_name="ไปที่เมนู2",
                        button_value="ไปที่เมนู2",
                    ),
                    ButtonMsg(
                        button_type="Phone",
                        button_name="โทรออก",
                        button_value="028319888",
                    ),
                ],
            ),
        ]

    return {
        "token": device_token,
        "TimeSend": datetime.now(tz=timezone(timedelta(hours=7))).isoformat(sep=" "),
        "msgSend": msg,
        "TimeAns": "2022-06-07 15:04:58.408218+07:00",
        "context": contextAns,
    }


# REF: https://www.youtube.com/watch?v=vpTAqnAbowo
path_files_in_github = "/app/proj/app_001/platform/files/"


@router.get("/GetFile")
def get_file(file_name: str, device_token: int):
    file_path = os.path.join(path_files_in_github, file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found!"}
