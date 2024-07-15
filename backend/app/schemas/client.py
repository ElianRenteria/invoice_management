# Path: backend/app/schemas/client.py

from app.schemas.invoice import Invoice

from pydantic import BaseModel
from typing import List


class ClientBase(BaseModel):
    name: str
    email: str


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    id: int


class Client(ClientBase):
    id: int
    invoices: List[Invoice] = []
    created_by: int

    class Config:
        from_attributes = True
