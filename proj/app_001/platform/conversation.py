import uuid
from fastapi import APIRouter

from pydantic import BaseModel
from typing import List, Union

router = APIRouter(
    prefix="/Conversation",
    tags=["Conversation"],
)

fake_res_conversation_list = [
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


@router.get("/list", response_model=List[Conversation])
async def get_conversation_unit_list():
    # read all
    return fake_res_conversation_list


@router.delete("/list", response_model=List[Conversation])
async def delete_conversation_unit_list(ListName: []):
    ListNameDel = [item['conver_name'] for item in ListName]
    # delete many
    # 
    return fake_res_conversation_list


@router.post("/unit", response_model=List[Conversation])
async def create_conver(conver: Conversation):

    # convert BaseModel to dict
    con = conver.dict()
    # add oid
    # https://pymongo.readthedocs.io/en/stable/tutorial.html#inserting-a-document
    con["_id"] = str(myuuid)

    # add data to database
    fake_res_conversation_list.append(con)

    return fake_res_conversation_list


@router.put("/unit", response_model=List[Conversation])
def update_conversation_unit():
    return


#  rd conver list
#  crud conver unit
