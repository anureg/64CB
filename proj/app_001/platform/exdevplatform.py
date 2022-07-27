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


def create_token(id):
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
    login_UUID: str

    login_Username: str
    login_Password: str


class login_res(BaseModel):
    login_Status: str  # success, not found, error

    login_Token: Union[int, None] = None

    user_id: Union[str, None] = None

    user_Firstname: Union[str, None] = None
    user_Lastname: Union[str, None] = None
    user_ImageProfile: Union[str, None] = None


@router.post("/", response_model=login_res, response_model_exclude_unset=True)
async def login_platform(login: login_req):
    """
    username, password login\n
    {
        "login_Username": "name1",
        "login_Password": "pass1"
    }
    """

    fake_db_users = load_json("fake_db_users.json")
    for item in fake_db_users:
        if login.login_Username == item["user_Username"]:
            user = item
        else:
            user = None

        if not user:
            raise HTTPException(status_code=404, detail="Not found")
        elif (
            login.login_Username != user["user_Username"]
            or login.login_Password != user["user_Password"]
        ):
            raise HTTPException(status_code=404, detail="error")
        else:
            user["login_Status"] = "Success"
            user["user_id"] = str(user["_id"])
            user["login_Token"] = create_token(id=login.login_UUID)

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
