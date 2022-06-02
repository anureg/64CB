from fastapi import APIRouter

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.get("/")
def hello_login():
    return {"hello": "login"}
