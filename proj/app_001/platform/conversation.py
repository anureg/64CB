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
        "_id": "62b173c605350640d79f2352",
        "conver_name": "00-2-1-GreetingUser-TH",
        "description": "ทักทายภาษาไทย",
    },
    {
        "_id": "62b173ec05350640d79f2354",
        "conver_name": "02-1-2-โทรศัพท์ DSI",
        "description": "เบอร์โทรศัพท์ DSI"
    },
    {
        "_id": "62b173f005350640d79f2355",
        "conver_name": "02-2-3-บริการ-ร้องเรียน ร้องทุกข์ แจ้งเบาะแส",
        "description": "บริการ ร้องเรียน ร้อทุกข์ แจ้งเบาะแส"
    }
]

myuuid = uuid.uuid4()


class Conversation(BaseModel):
    _id: str
    conver_name: str
    description: Union[str, None] = None


@router.get("/", response_model=List[Conversation])
async def read_conver():
    return fake_db_conversation


@router.post("/", response_model=List[Conversation])
async def create_conver(conver: Conversation):
   
    con = conver.dict()
    con["_id"] = str(myuuid)

    fake_db_conversation.append(con)

    return fake_db_conversation
