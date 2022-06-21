from proj.app_001.chat import exdevchat
from proj.app_001.platform import exdevplatform
from proj.app_001.platform import conversation

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(exdevchat.router)
app.include_router(exdevplatform.router)
app.include_router(conversation.router)

# CORS (Cross-Origin Resource Sharing)
# ["https://localhost","http://localhost","http://localhost:8080"]
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World"}
