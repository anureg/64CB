from fastapi import APIRouter

from pydantic import BaseModel
from typing import Union


router = APIRouter(
    prefix="/ExDevPlatform/Conversation",
)

fake_res_conversation_list = [
    {
        "id": "13001",
        "conver_name": "00-2-1-GreetingUser-TH",
        "description": "ทักทายภาษาไทย",
    },
    {
        "id": "13002",
        "conver_name": "02-1-2-โทรศัพท์ DSI",
        "description": "เบอร์โทรศัพท์ DSI",
    },
    {
        "id": "13003",
        "conver_name": "02-2-3-บริการ-ร้องเรียน ร้องทุกข์ แจ้งเบาะแส",
        "description": "บริการ ร้องเรียน ร้อทุกข์ แจ้งเบาะแส",
    },
]


class Conversation(BaseModel):
    id: str
    conver_name: str
    description: Union[str, None] = None


class CreateConver(BaseModel):
    # _id: str  # ตอนสร้าง conver ใหม่ ไม่ต้องใช้ _id เพราะ ให้ mongodb สร้าง objectId มาให้
    conver_name: str
    description: Union[str, None] = None


@router.get("/list", tags=["Conversation List"], response_model=list[Conversation])
def get_conversation_unit_list():
    # read all
    res = [
        {
            "id": "13001",
            "conver_name": "00-2-1-GreetingUser-TH",
            "description": "ทักทายภาษาไทย",
        },
        {
            "id": "13002",
            "conver_name": "02-1-2-โทรศัพท์ DSI",
            "description": "เบอร์โทรศัพท์ DSI",
        },
        {
            "id": "13003",
            "conver_name": "02-2-3-บริการ-ร้องเรียน ร้องทุกข์ แจ้งเบาะแส",
            "description": "บริการ ร้องเรียน ร้อทุกข์ แจ้งเบาะแส",
        },
    ]

    return res


@router.delete("/list", tags=["Conversation List"], response_model=list[Conversation])
def delete_conversation_unit_list(listId: list[str]):
    # delete many or one
    """
    listId = ["1","2"]\n
    or\n
    listId = ["1"]
    """
    res = [
        {
            "id": "",
            "conver_name": "deleted",
            "description": "ลบข้อมูลเรียบร้อยแล้ว",
        },
    ]

    return res


@router.post("/unit", tags=["Conversation Unit"], response_model=list[Conversation])
def create_conversation_unit(conversation: CreateConver):
    # create
    """
    {
        "conver_name": "created",
        "description": "เพิ่มข้อมูลเรียบร้อยแล้วจ้า",
    }
    """
    res = [
        {
            "id": "13001",
            "conver_name": "00-2-1-GreetingUser-TH",
            "description": "ทักทายภาษาไทย",
        },
        {
            "id": "13002",
            "conver_name": "02-1-2-โทรศัพท์ DSI",
            "description": "เบอร์โทรศัพท์ DSI",
        },
        {
            "id": "13003",
            "conver_name": "02-2-3-บริการ-ร้องเรียน ร้องทุกข์ แจ้งเบาะแส",
            "description": "บริการ ร้องเรียน ร้อทุกข์ แจ้งเบาะแส",
        },
        {
            "id": "mongo gen id",
            "conver_name": "created",
            "description": "เพิ่มข้อมูลเรียบร้อยแล้วจ้า",
        },
    ]

    return res


@router.get("/unit", response_model=list[Conversation], tags=["Conversation Unit"])
def get_conversation_unit(id: str):
    # read one
    """
    find by id\n
    id = "13001"
    """
    res = [
        {
            "id": "13001",
            "conver_name": "00-2-1-GreetingUser-TH",
            "description": "ทักทายภาษาไทย",
        },
    ]

    return res


@router.put("/unit", tags=["Conversation Unit"], response_model=list[Conversation])
def update_conversation_unit(conversation: Conversation):
    # update one
    """
    {
        "id": "13003",
        "conver_name": "update",
        "description": "แก้ไขข้อมูลเรียบร้อย",
    }
    """
    res = [
        {
            "id": "13001",
            "conver_name": "00-2-1-GreetingUser-TH",
            "description": "ทักทายภาษาไทย",
        },
        {
            "id": "13002",
            "conver_name": "02-1-2-โทรศัพท์ DSI",
            "description": "เบอร์โทรศัพท์ DSI",
        },
        {
            "id": "13003",
            "conver_name": "update",
            "description": "แก้ไขข้อมูลเรียบร้อย",
        },
    ]

    return res
