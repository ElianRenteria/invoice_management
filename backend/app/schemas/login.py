# Path: backend/app/schemas/client.py

from pydantic import BaseModel
from typing import List


class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    name: str
    username: str
    email: str
    