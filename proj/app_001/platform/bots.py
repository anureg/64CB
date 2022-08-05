from fastapi import APIRouter

from pydantic import BaseModel
from typing import Union


router = APIRouter(
    prefix="/ExDevPlatform/Bot",
)

fake_res_bot_list = [
    {
        "id": "14001",
        "Bot_Name": "bot1",
        "Bot_Description": "รายละเอียด bot1 รายละเอียด bot1 รายละเอียด bot1 รายละเอียด bot1 รายละเอียด bot1",
        "Bot_Picture_Name": "14001.png",
        "Bot_Status": "False",
    },
    {
        "id": "14002",
        "Bot_Name": "bot2",
        "Bot_Description": "รายละเอียด bot2",
        "Bot_Picture_Name": "14002.png",
        "Bot_Status": "False",
    },
    {
        "id": "14003",
        "Bot_Name": "bot3",
        "Bot_Description": "รายละเอียด bot3",
        "Bot_Picture_Name": "14003.png",
        "Bot_Status": "False",
    },
]


class Bot(BaseModel):
    id: str
    Bot_Name: str
    Bot_Description: Union[str, None] = None
    Bot_Picture_Name: str
    Bot_Status: bool


class CreateBot(BaseModel):
    # _id: str  # ตอนสร้าง bot ใหม่ ไม่ต้องใช้ _id เพราะ ให้ mongodb สร้าง objectId มาให้
    Bot_Name: str
    # Bot_Picture_Name: str  # ตอนสร้าง bot ใหม่ เอา id มาเป็นชื่อ
    # Bot_Status: False  # ตอนสร้าง bot ใหม่ ตั้งให้เป็น false
    Bot_Description: Union[str, None] = None


@router.get("/list", tags=["Bot List"], response_model=list[Bot])
def get_bot_unit_list():
    # read all
    res = fake_res_bot_list

    return res


@router.delete("/list", tags=["Bot List"], response_model=list[Bot])
def delete_bot_unit_list(listId: list[str]):
    # delete many or one
    """
    listId = ["1","2"]\n
    or\n
    listId = ["1"]
    """
    res = [
        {
            "id": "14001",
            "Bot_Name": "bot1",
            "Bot_Description": "รายละเอียด bot1 รายละเอียด bot1 รายละเอียด bot1 รายละเอียด bot1 รายละเอียด bot1",
            "Bot_Picture_Name": "14001.png",
            "Bot_Status": "False",
        },
        {
            "id": "14002",
            "Bot_Name": "bot2",
            "Bot_Description": "รายละเอียด bot2",
            "Bot_Picture_Name": "14002.png",
            "Bot_Status": "False",
        },
    ]

    return res


@router.post("/unit", tags=["Bot Unit"], response_model=list[Bot])
def create_bot_unit(bot: CreateBot):
    # create
    """
    {
        "Bot_Name": "bot4",
        "Bot_Description": "รายละเอียด bot4",
    }
    """
    res = fake_res_bot_list + [
        {
            "id": "14004",
            "Bot_Name": "bot4",
            "Bot_Description": "รายละเอียด bot4",
            "Bot_Picture_Name": "14004.png",
            "Bot_Status": "False",
        },
    ]

    return res


@router.get("/unit", response_model=list[Bot], tags=["Bot Unit"])
def get_bot_unit(id: str):
    # read one
    """
    find by id\n
    id = "14001"
    """
    res = [
        {
            "id": "14001",
            "Bot_Name": "bot1",
            "Bot_Picture_Name": "14001.png",
            "Bot_Status": "False",
        },
    ]

    return res


@router.put("/unit", tags=["Bot Unit"], response_model=list[Bot])
def update_bot_unit(bot: Bot):
    # update one
    """
    {
        "id": "14001",
        "Bot_Name": "bot1",
        "Bot_Description": "รายละเอียด bot1 แบบแก้ไข",
        "Bot_Picture_Name": "14001.png",
        "Bot_Status": "False",
    }
    """
    res = [
        {
            "id": "14001",
            "Bot_Name": "bot1",
            "Bot_Description": "รายละเอียด bot1 แบบแก้ไข",
            "Bot_Picture_Name": "14001.png",
            "Bot_Status": "False",
        },
        {
            "id": "14002",
            "Bot_Name": "bot2",
            "Bot_Description": "รายละเอียด bot2",
            "Bot_Picture_Name": "14002.png",
            "Bot_Status": "False",
        },
        {
            "id": "14003",
            "Bot_Name": "bot3",
            "Bot_Description": "รายละเอียด bot3",
            "Bot_Picture_Name": "14003.png",
            "Bot_Status": "False",
        },
    ]

    return res
