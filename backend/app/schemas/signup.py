# Path: backend/app/schemas/client.py

from pydantic import BaseModel
from typing import List


class SignUpRequest(BaseModel):
    name: str
    username: str
    email: str
    password: str


class SignUpResponse(BaseModel):
    name: str
    username: str
    email: str
