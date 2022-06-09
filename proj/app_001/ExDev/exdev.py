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


@router.get("/ChatMsg")
def chat_msg(msg: str, mytoken: int, contextSend: str):

    if msg == 'card1':
        contextAns = Cardmessage(
            topic='ร้องเรียนเจ้าหน้าที่',
            subtopic='การแจ้งข้อมูลจะต้องเป็นความจริงทุกประการ\nการใช้ข้อมูลเท็จหรือใช้ข้อมูลผู้อื่นของมาแอบอ้าง\nอาจถูกดำเนินการตามกฎหมาย',
            buttonLink=[
                'เข้าสู่เว็บไซต์',
                'https://register.dsi.go.th/'
            ],
            image='https://www.dsi.go.th//images/banner/complaint_dsi_officer.jpg'
        )
    elif msg == 'card2':
        contextAns = Cardmessage(
            topic='เมนูหลัก',
            subtopic='คลิกเลือกรายการที่ต้องการ :',
            buttonText=[
                'ช่องทางการติดต่อ',
                'ช่องทางการติดต่อ',
                'เมนูติดต่อ',
                'เมนูติดต่อ',
                'บริการ',
                'บริการ',
                'เมนูบริการ',
                'เมนูบริการ',
                'กฎหมายและระเบียบ',
                'กฎหมายและระเบียบ',
                'เมนูกฎหมาย',
                'เมนูกฎหมาย',
            ]
        )
    elif msg == 'card3':
        contextAns = Cardmessage(
            topic='โทรศัพท์',
            subtopic='หมายเลข 0 2831 9888\nวันและเวลาราชการ (08.30-16.30)',
            buttonPhone=[
                'โทรออก',
                '028319888',
            ]
        )
    elif msg == 'card5':
        contextAns = Cardmessage(
            topic='test pdf',
            file_path='file_doc/test_pdf.pdf'
        )
    else:
        contextAns = Cardmessage(
            topic=msg
        )

    return {
        "token": mytoken,
        "TimeSend": "2022-06-07 15:04:58.408218+07:00",
        "TimeAns": "2022-06-07 15:04:58.408218+07:00",
        "msgSend": msg,
        "context": contextAns
    }
