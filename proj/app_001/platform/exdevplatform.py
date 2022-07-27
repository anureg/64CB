import os
import json

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from pydantic import BaseModel
from typing import List, Union

from datetime import datetime, timezone, timedelta


router = APIRouter(
    prefix="/ExDevPlatform/Login",
    tags=["Login"],
)


def GenToken(id):
    # Time zone in Thailand UTC+7
    tz = timezone(timedelta(hours=7))
    # Create a date object with given timezone
    timestr = datetime.now(tz=tz).isoformat(sep=" ")
    # hash(device_id + timestr)
    token = hash(id + timestr)  # type token int
    return token


def load_json(filename: str):
    with open(f"/app/proj/app_001/platform/fake_db/{filename}") as json_file:
        js_file = json.load(json_file)
        return js_file


path_ImageProfile = "/app/proj/app_001/platform/icon_users/"


class login_req(BaseModel):
    username: str
    password: str

    device_id: str


class login_res(BaseModel):
    status_login: str

    token: int

    id: str
    user_Username: str

    user_Firstname: Union[str, None] = None
    user_Lastname: Union[str, None] = None
    user_Picture: Union[str, None] = None


@router.post("/", response_model=login_res, response_model_exclude_unset=True)
async def login_platform(login: login_req):
    """
    user login\n
    {
        "username": "name1",
        "password": "pass1"
    }
    """

    fake_db_users = load_json("fake_db_users.json")
    for item in fake_db_users:
        if (
            login.username != item["user_Username"]
            or login.password != item["user_Password"]
        ):
            raise HTTPException(status_code=404, detail="Not found")
        else:
            user = item

            user["status_login"] = "Success"
            user["id"] = str(user["_id"])
            user["token"] = GenToken(id=login.device_id)

            return user


@router.get("/GetIcon")
def get_Icon(icon_name: str):
    """
    icon_name = "user_Picture": "6219bc9ba8a68a763a9ae90e.png"\n
    or\n
    icon_name = "/app/proj/app_001/platform/icon_users/6219bc9ba8a68a763a9ae90e.png"
    """

    file_path = os.path.join(path_ImageProfile, icon_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found!"}
