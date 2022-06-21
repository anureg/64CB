import os
import json

from fastapi import APIRouter
from fastapi.responses import FileResponse

from pydantic import BaseModel
from typing import List, Union

from datetime import datetime, timezone, timedelta


router = APIRouter(
    prefix="/ExDevPlatform",
    tags=["ExDevPlatform"],
)


def load_json(filename: str):
    with open(f'/app/proj/app_001/platform/fake_db/{filename}') as json_file:
        js_file = json.load(json_file)
        return js_file


path_ImageProfile = "/app/proj/app_001/platform/icon_users/"


class login_req(BaseModel):
    username: str
    password: str
    device_id: str


class login_res(BaseModel):
    StatusLogin: str
    token: Union[int, None] = None
    user_id: Union[str, None] = None
    user_Username: Union[str, None] = None
    user_Name: Union[str, None] = None
    user_Surname: Union[str, None] = None
    user_ImageProfile: Union[str, None] = None


def GenToken(id):
    # Time zone in Thailand UTC+7
    tz = timezone(timedelta(hours=7))
    # Create a date object with given timezone
    timestr = datetime.now(tz=tz).isoformat(sep=" ")
    # hash(device_id + timestr)
    token = hash(id + timestr)  # type token int
    return token


@router.post("/", response_model=login_res, response_model_exclude_unset=True)
async def login_platform(login: login_req):

    fake_db_users = load_json('fake_db_users.json')
    for item in fake_db_users:
        if login.username == item["user_Username"] and login.password == item["user_Password"]:

            user = item
            token = GenToken(id=login.device_id)

            return {
                "StatusLogin": "Connect",
                "token": int(token),
                "user_id": str(user['_id']),
                "user_Username": str(user['user_Username']),
                "user_Name": str(user['user_Name']),
                "user_Surname": str(user['user_Surname']),
                "user_ImageProfile": str(path_ImageProfile + user['user_ImageProfile'])
            }

    return {"StatusLogin": "Login error"}


class ChatHistory(BaseModel):
    Chat_Token: int
    Chat_Type: str
    Chat_Msg: str
    Chat_Timestamp: str


@router.get("/chat/", response_model=List[ChatHistory])
async def read_chat():
    fake_db_chat_his = load_json('fake_db_chat_historys.json')
    return fake_db_chat_his


@router.get("/GetIcon")
def get_Icon(location_icon: str,):
    file_path = os.path.join(path_ImageProfile, location_icon)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found!"}
