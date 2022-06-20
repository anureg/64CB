from fastapi import APIRouter

from pydantic import BaseModel
from typing import List, Union

from datetime import datetime, timezone, timedelta


router = APIRouter(
    prefix="/ExDevPlatform",
    tags=["ExDevPlatform"],
)


path_ImageProfile = "/app/proj/app_001/platform/icon_users/"
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
def login_platform(login: login_req):

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



# import json
# fake_db_chat_his = json.load('/proj/app_001/platform/fake_db/fake_db_chat_his.json')


# class ChatHistory(BaseModel):
#     Chat_Token: int
#     Chat_Type: str
#     Chat_Msg: str
#     Chat_Timestamp: str


# @router.get("/", response_model=List[ChatHistory], response_model_exclude_unset=True)
# def chat_his():
#     return fake_db_chat_his


class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@router.get("/items/", response_model=List[Item])
async def read_items():
    return items