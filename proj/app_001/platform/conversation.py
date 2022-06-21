import uuid
from fastapi import APIRouter

from pydantic import BaseModel
from typing import List, Union

router = APIRouter(
    prefix="/Conversation",
    tags=["Conversation"],
)

fake_db_conversation = [
    {
        "_id": "623836ece7d78760dd80e41b",
        "conver_name": "00-2-1-GreetingUser-TH",
        "description": "ทักทายภาษาไทย",
    },
    {
        "_id": "623836ece7d78760dd80e41c",
        "conver_name": "02-1-2-โทรศัพท์ DSI",
        "description": "เบอร์โทรศัพท์ DSI"
    },
    {
        "_id": "623836ece7d78760dd80e41d",
        "conver_name": "02-2-3-บริการ-ร้องเรียน ร้องทุกข์ แจ้งเบาะแส",
        "description": "บริการ ร้องเรียน ร้อทุกข์ แจ้งเบาะแส"
    }
]

myuuid = uuid.uuid4()


class Conversation(BaseModel):
    _id: gen_id
    conver_name: str
    description: Union[str, None] = None

    class Config:
        gen_id: myuuid


@router.get("/readall/", response_model=List[Conversation])
async def read_conver():
    return fake_db_conversation


@router.post("/create/", response_model=List[Conversation])
async def create_conver(conver: Conversation):
    fake_db_conversation.append(conver)
    return fake_db_conversation
