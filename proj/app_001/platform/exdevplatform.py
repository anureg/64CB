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
    StatusLogin: str
    token: int
    user_id: Union[str, None] = None
    user_Username: Union[str, None] = None
    user_Name: Union[str, None] = None
    user_Surname: Union[str, None] = None
    user_ImageProfile: Union[str, None] = None


@router.post("/", response_model=login_res, response_model_exclude_unset=True)
def login_platform(login: login_req):
    # Time zone in Thailand UTC+7
    tz = timezone(timedelta(hours=7))
    # Create a date object with given timezone
    timestr = datetime.now(tz=tz).isoformat(sep=" ")
    # hash(device_id + timestr)
    get_token = hash(login.device_id + timestr)  # type token int

    for item in fake_db_users:
        if item["user_Username"] == login.username:
            user = item
            if item["user_Password"] == login.password:
                StatusLogin = "Connect"  # ถ้ารหัสถูก
                break
            else:
                StatusLogin = "Login error"  # ถ้ารหัสผิด
                break
        else:
            return {"StatusLogin": "Not Found"}

    return {
        "StatusLogin": StatusLogin,
        "token": int(get_token),
        "user_id": str(user['_id']),
        "user_Username": str(user['user_Username']),
        "user_Name": str(user['user_Name']),
        "user_Surname": str(user['user_Surname']),
        "user_ImageProfile": str(path_ImageProfile + user['user_ImageProfile'])
    }


class Test1(BaseModel):
    test1: str


class Test2(BaseModel):
    test2: str
    testtest2: str
    _ii: str


@router.post("/test", response_model=Test2)
def test(T: Test1):
    userId = fake_db_users[0]["_id"]
    return {
        "test2": str(T.test1),
        "testtest2": str(usesrId),
        "_ii": str(T.test1 + T.test1 + T.test1)
    }
