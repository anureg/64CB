from fastapi import FastAPI, Header, Form, Body
from pydantic import BaseModel


class ConversationUnit(BaseModel):
    text: str
    tag: str
    incoming_message: list
    outgoing_message: list
    created_at: str


class Service(BaseModel):
    name: str
    description: str
    version: str
    endpoint: str
    media_type: str
    parameter: list
    created_at: str


class incoming_message(BaseModel):
    session_id: str
    text: str
    context: dict


class outgoing_message(BaseModel):
    text: str
    context: dict


app = FastAPI(
    title="Chat API",
    description="Chat Backend API",
    version="0.1.0"
)
from appfile.module_login import login
app.include_router(login.router)


@app.get("/")
def read_root():
    return {"Hello": "Worlddddddd"}


@app.post("/conversation/unit", tags=["Conversation Unit"])
def create_conversation_unit(conversation_unit: ConversationUnit):
    res = {
        "status": "success",
    }
    return res


@app.get("/conversation/unit", tags=["Conversation Unit"])
def get_conversation_unit(cid: str):
    return {"Hello": "World"}


@app.put("/conversation/unit", tags=["Conversation Unit"])
def update_conversation_unit(conversation_unit: ConversationUnit):
    res = {
        "status": "success",
    }
    return res


@app.delete("/conversation/unit", tags=["Conversation Unit"])
def delete_conversation_unit(cid: str = ""):
    res = {
        "status": "success",
    }
    return res


@app.get("/conversation/list", tags=["Conversation Unit"])
def get_conversation_unit_list():
    res = []

    return res


@app.post("/service", tags=["Service"])
def create_service(service: Service):

    res = {
        "status": "success",
    }
    return res


@app.get("/service", tags=["Service"])
def get_service():
    return {"Hello": "World"}


@app.put("/service", tags=["Service"])
def update_service(service: Service):

    res = {
        "status": "success",
    }
    return res


@app.delete("/service", tags=["Service"])
def delete_service(sid: str = ""):

    res = {
        "status": "success",
    }
    return res


@app.get("/service/list", tags=["Service"])
def get_service_list():
    res = []
    return res


@app.get("/chat", tags=["Chat"], response_model=outgoing_message)
def chat(inc_msg: incoming_message):
    return {"Hello": "World"}
