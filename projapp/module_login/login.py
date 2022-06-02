from fastapi import APIRouter

router = APIRouter(
    prefix= "/login",
    tags= ["Login"]
)

@router.get("/")
def Hello_login():
    return {"Hello": "Login"}