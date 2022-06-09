from proj.app_001.ExDev import exdev
from fastapi import FastAPI
from fastapi.responses import FileResponse

from fastapi.middleware.cors import CORSMiddleware

import os

from pydantic import BaseModel
from typing import List, Union

from datetime import datetime, timezone, timedelta


class welcome_message(BaseModel):
    token: str
    message: str


class incoming_message(BaseModel):
    session_id: str
    text: str
    context: dict


class outgoing_message(BaseModel):
    text: str
    context: dict


app = FastAPI()
app.include_router(exdev.router)

# CORS (Cross-Origin Resource Sharing)
# ["https://localhost","http://localhost","http://localhost:8080"]
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello Worlds"}


@app.get("/welcome")
def root(device_id: str):
    token = '6930525350968360228'
    return {
        "token": token,
        "message": "ยินดีต้อนรับ"
    }


@app.get("/chat", tags=["Chat"], response_model=outgoing_message)
def chat(inc_msg: incoming_message):
    return {"Hello": "World"}
# https://fastapi.tiangolo.com/tutorial/response-model/


"""
test area
"""


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


@app.get("/ChatMsg", tags=["test"])
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


@app.get("/GetPdfFile", tags=["test"])
def get_pdf_file(jsB_file_path: str):
    return file(jsB_file_path)


# REF: https://www.youtube.com/watch?v=vpTAqnAbowo
path = "/code/app/"


def file(jsB: str):
    file_path = os.path.join(path, jsB)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found!"}
