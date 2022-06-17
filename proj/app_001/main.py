from proj.app_001.platform import exdevplatform
from proj.app_001.chat import exdevchat

from fastapi import FastAPI
from fastapi.responses import FileResponse

from fastapi.middleware.cors import CORSMiddleware

import os

from pydantic import BaseModel
from typing import List, Union

from datetime import datetime, timezone, timedelta


app = FastAPI()
app.include_router(exdevchat.router)
app.include_router(exdevplatform.router)

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
    return {"message": "Hello Worlds"}
