from fastapi import APIRouter

from pydantic import BaseModel
from typing import Union


router = APIRouter(
    prefix="/ExDevPlatform/Conversation",
)

fake_res_conversation_list = [
    {
        "id": "13001",
        "Conversation_BotID": "14001",
        "Conversation_Name": "00-2-1-GreetingUser-TH",
        "Conversation_Tag": "ทักทาย",
        "Conversation_Incoming": [
            "ดีครับ",
            "ไง",
            "ดีครับ",
            "หวัดดี",
            "สวัดสี",
            "สวัดสี",
            "สวัสดี",
            "สวัสดีคับ",
            "สวัสดีค่ะ",
            "ดีงับ",
        ],
        "Conversation_Outgoing": ["สวัสดีจ้า", "สวัสดี"],
        "Conversation_Description": "ทักทายภาษาไทย",
    },
    {
        "id": "13002",
        "Conversation_BotID": "14001",
        "Conversation_Name": "02-1-2-โทรศัพท์ DSI",
        "Conversation_Tag": "เบอร์โทร",
        "Conversation_Incoming": [
            "ขอเบอร์หน่อย",
            "เบอร์โทร",
            "โทรศัพท์ DSI",
            "เบอร์โทร DSI",
            "โทร",
            "เบอร์กรมเบอร์ไร",
        ],
        "Conversation_Outgoing": ["โทรศัพท์ หมายเลข 0 2831 9888", "0 2831 9888"],
        "Conversation_Description": "เบอร์โทรศัพท์ DSI",
    },
    {
        "id": "13003",
        "Conversation_BotID": "14001",
        "Conversation_Name": "02-2-3-บริการ-ร้องเรียน ร้องทุกข์ แจ้งเบาะแส",
        "Conversation_Tag": "บริการ",
        "Conversation_Incoming": [
            "ขอความเป็นธรรม",
            "บังคับสูญหาย",
            "อุ้มหาย",
            "โดนอุ้มหาย",
            "เหตุร้าย",
            "ทำร้าย",
            "ต้องสงสัย",
            "น่าสงสัย",
            "SMS",
            "ดูดข้อมูล",
        ],
        "Conversation_Outgoing": ["ร้องเรียน", "แจ้งเบาะแส", "ร้องทุกข์"],
        "Conversation_Description": "บริการ ร้องเรียน ร้อทุกข์ แจ้งเบาะแส",
    },
]


class Conversation(BaseModel):
    id: str
    Conversation_Name: str
    Conversation_BotID: str
    Conversation_Description: Union[str, None] = None


class CreateConver(BaseModel):
    # _id: str  # ตอนสร้าง conver ใหม่ ไม่ต้องใช้ _id เพราะ ให้ mongodb สร้าง objectId มาให้
    Conversation_Name: str
    Conversation_Description: Union[str, None] = None


@router.get("/list", tags=["Conversation List"], response_model=list[Conversation])
def get_conversation_unit_list():
    # read all
    res = fake_res_conversation_list

    return res


@router.delete("/list", tags=["Conversation List"], response_model=list[Conversation])
def delete_conversation_unit_list(listId: list[str]):
    # delete many or one
    res = [
        {
            "id": "13001",
            "Conversation_BotID": "14001",
            "Conversation_Name": "00-2-1-GreetingUser-TH",
            "Conversation_Tag": "ทักทาย",
            "Conversation_Incoming": [
                "ดีครับ",
                "ไง",
                "ดีครับ",
                "หวัดดี",
                "สวัดสี",
                "สวัดสี",
                "สวัสดี",
                "สวัสดีคับ",
                "สวัสดีค่ะ",
                "ดีงับ",
            ],
            "Conversation_Outgoing": ["สวัสดีจ้า", "สวัสดี"],
            "Conversation_Description": "ทักทายภาษาไทย",
        },
        {
            "id": "13002",
            "Conversation_BotID": "14001",
            "Conversation_Name": "02-1-2-โทรศัพท์ DSI",
            "Conversation_Tag": "เบอร์โทร",
            "Conversation_Incoming": [
                "ขอเบอร์หน่อย",
                "เบอร์โทร",
                "โทรศัพท์ DSI",
                "เบอร์โทร DSI",
                "โทร",
                "เบอร์กรมเบอร์ไร",
            ],
            "Conversation_Outgoing": ["โทรศัพท์ หมายเลข 0 2831 9888", "0 2831 9888"],
            "Conversation_Description": "เบอร์โทรศัพท์ DSI",
        },
    ]

    return res


@router.post("/unit", tags=["Conversation Unit"], response_model=list[Conversation])
def create_conversation_unit(conversation: CreateConver):
    # create
    res = [
        {
            "id": "13001",
            "Conversation_BotID": "14001",
            "Conversation_Name": "00-2-1-GreetingUser-TH",
            "Conversation_Tag": "ทักทาย",
            "Conversation_Incoming": [
                "ดีครับ",
                "ไง",
                "ดีครับ",
                "หวัดดี",
                "สวัดสี",
                "สวัดสี",
                "สวัสดี",
                "สวัสดีคับ",
                "สวัสดีค่ะ",
                "ดีงับ",
            ],
            "Conversation_Outgoing": ["สวัสดีจ้า", "สวัสดี"],
            "Conversation_Description": "ทักทายภาษาไทย",
        },
        {
            "id": "13002",
            "Conversation_BotID": "14001",
            "Conversation_Name": "02-1-2-โทรศัพท์ DSI",
            "Conversation_Tag": "เบอร์โทร",
            "Conversation_Incoming": [
                "ขอเบอร์หน่อย",
                "เบอร์โทร",
                "โทรศัพท์ DSI",
                "เบอร์โทร DSI",
                "โทร",
                "เบอร์กรมเบอร์ไร",
            ],
            "Conversation_Outgoing": ["โทรศัพท์ หมายเลข 0 2831 9888", "0 2831 9888"],
            "Conversation_Description": "เบอร์โทรศัพท์ DSI",
        },
        {
            "id": "13003",
            "Conversation_BotID": "14001",
            "Conversation_Name": "02-2-3-บริการ-ร้องเรียน ร้องทุกข์ แจ้งเบาะแส",
            "Conversation_Tag": "บริการ",
            "Conversation_Incoming": [
                "ขอความเป็นธรรม",
                "บังคับสูญหาย",
                "อุ้มหาย",
                "โดนอุ้มหาย",
                "เหตุร้าย",
                "ทำร้าย",
                "ต้องสงสัย",
                "น่าสงสัย",
                "SMS",
                "ดูดข้อมูล",
            ],
            "Conversation_Outgoing": ["ร้องเรียน", "แจ้งเบาะแส", "ร้องทุกข์"],
            "Conversation_Description": "บริการ ร้องเรียน ร้อทุกข์ แจ้งเบาะแส",
        },
        {
            "id": "13004",
            "Conversation_BotID": "14001",
            "Conversation_Name": "xxx",
            "Conversation_Tag": "xxx",
            "Conversation_Incoming": [
                "ขอความเป็นธรรม",
                "บังคับสูญหาย",
                "อุ้มหาย",
                "โดนอุ้มหาย",
                "เหตุร้าย",
                "ทำร้าย",
                "ต้องสงสัย",
                "น่าสงสัย",
                "SMS",
                "ดูดข้อมูล",
            ],
            "Conversation_Outgoing": ["ร้องเรียน", "แจ้งเบาะแส", "ร้องทุกข์"],
            "Conversation_Description": "คำอธิบาย xxx",
        },
    ]

    return res


@router.get("/unit", response_model=list[Conversation], tags=["Conversation Unit"])
def get_conversation_unit(id: str):
    # read one
    res = [
        {
            "id": "13003",
            "Conversation_BotID": "14001",
            "Conversation_Name": "02-2-3-บริการ-ร้องเรียน ร้องทุกข์ แจ้งเบาะแส",
            "Conversation_Tag": "บริการ",
            "Conversation_Incoming": [
                "ขอความเป็นธรรม",
                "บังคับสูญหาย",
                "อุ้มหาย",
                "โดนอุ้มหาย",
                "เหตุร้าย",
                "ทำร้าย",
                "ต้องสงสัย",
                "น่าสงสัย",
                "SMS",
                "ดูดข้อมูล",
            ],
            "Conversation_Outgoing": ["ร้องเรียน", "แจ้งเบาะแส", "ร้องทุกข์"],
            "Conversation_Description": "บริการ ร้องเรียน ร้อทุกข์ แจ้งเบาะแส",
        },
    ]

    return res


@router.put("/unit", tags=["Conversation Unit"], response_model=list[Conversation])
def update_conversation_unit(conversation: Conversation):
    # update one
    res = [
        {
            "id": "13001",
            "Conversation_BotID": "14001",
            "Conversation_Name": "00-2-1-GreetingUser-TH",
            "Conversation_Tag": "ทักทาย",
            "Conversation_Incoming": [
                "ดีครับ",
                "ไง",
                "ดีครับ",
                "หวัดดี",
                "สวัดสี",
                "สวัดสี",
                "สวัสดี",
                "สวัสดีคับ",
                "สวัสดีค่ะ",
                "ดีงับ",
            ],
            "Conversation_Outgoing": ["สวัสดีจ้า", "สวัสดี"],
            "Conversation_Description": "ทักทายภาษาไทย",
        },
        {
            "id": "13002",
            "Conversation_BotID": "14001",
            "Conversation_Name": "02-1-2-โทรศัพท์ DSI",
            "Conversation_Tag": "เบอร์โทร",
            "Conversation_Incoming": [
                "ขอเบอร์หน่อย",
                "เบอร์โทร",
                "โทรศัพท์ DSI",
                "เบอร์โทร DSI",
                "โทร",
                "เบอร์กรมเบอร์ไร",
            ],
            "Conversation_Outgoing": ["โทรศัพท์ หมายเลข 0 2831 9888", "0 2831 9888"],
            "Conversation_Description": "เบอร์โทรศัพท์ DSI",
        },
        {
            "id": "13003",
            "Conversation_BotID": "14001",
            "Conversation_Name": "02-2-3-บริการ-ร้องเรียน ร้องทุกข์ แจ้งเบาะแส xxx",
            "Conversation_Tag": "บริการ",
            "Conversation_Incoming": [
                "ขอความเป็นธรรม",
                "บังคับสูญหาย",
                "อุ้มหาย",
                "โดนอุ้มหาย",
                "เหตุร้าย",
                "ทำร้าย",
                "ต้องสงสัย",
                "น่าสงสัย",
                "SMS",
                "ดูดข้อมูล",
            ],
            "Conversation_Outgoing": ["ร้องเรียน", "แจ้งเบาะแส", "ร้องทุกข์"],
            "Conversation_Description": "บริการ ร้องเรียน ร้อทุกข์ แจ้งเบาะแส xxx",
        },
    ]

    return res
