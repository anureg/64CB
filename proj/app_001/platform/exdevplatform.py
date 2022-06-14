from fastapi import APIRouter

from pydantic import BaseModel
from typing import List, Union

from datetime import datetime, timezone, timedelta


router = APIRouter(
    prefix="/ExDevPlatform",
    tags=["ExDevPlatform"],
)


path_ImageProfile = "/platform/icon_users/"
fake_db_users = [
    {
        "_id": "6219bc9ba8a68a763a9ae90e",
        "user_Username": "uname1",
        "user_Password": "pass1",
        "user_Name": "name1",
        "user_Surname": "นามสกุล1",
        "user_ImageProfile": "6219bc9ba8a68a763a9ae90e.png",
        "user_Email": "Name1@gmail.com"
    },
    {
        "_id": "6219bccda8a68a763a9ae90f",
        "user_Username": "uname2",
        "user_Password": "pass2",
        "user_Name": "name2",
        "user_Surname": "นามสกุล2",
        "user_ImageProfile": "6219bccda8a68a763a9ae90f.png",
        "user_Email": "Name2@gmail.com"
    },
    {
        "_id": "6219bd1ea8a68a763a9ae910",
        "user_Username": "uname3",
        "user_Password": "pass3",
        "user_Name": "name3",
        "user_Surname": "นามสกุล3",
        "user_ImageProfile": "6219bd1ea8a68a763a9ae910.png",
        "user_Email": "Name3@gmail.com"
    }
]


class login_req(BaseModel):
    username: str
    password: str
    device_id: str


class login_res(BaseModel):
    token: int
    _id: str
    user_Username: str
    user_Name: str
    user_Surname: str
    user_ImageProfile: str


@router.post("/", response_model=login_res)
def login_platform(login: login_req):
    # Time zone in Thailand UTC+7
    tz = timezone(timedelta(hours=7))
    # Create a date object with given timezone
    timestr = datetime.now(tz=tz).isoformat(sep=" ")
    # hash(device_id + timestr)
    token = hash(device_id + timestr)  # type token int

    for item in fake_db_users:
        if item["user_Username"] == login.username:
            if item["user_Password"] == login.password:
                user = item  # ถ้ารหัสถูก
            else:
                return {"StatusLogin": "Login error"}  # ถ้ารหัสผิด
        else:
            return {"StatusLogin": "Not Found"}  # ถ้าหา username ใน DB ไม่เจอ

    return {
        "token": token,
        "_id": user["_id"]
    }
