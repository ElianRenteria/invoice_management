# Path: backend/app/schemas/client.py

from app.schemas.invoice import Invoice

from pydantic import BaseModel
from typing import List


class ClientBase(BaseModel):
    """
    ClientBase schema class.

    Attributes:
        name (str): The name of the client.
        email (str): The email of the client.
    """
    name: str
    email: str


class ClientCreate(ClientBase):
    """
    ClientCreate schema class for creating a new client.

    Attributes:
        Inherits attributes from ClientBase schema class.
    """
    pass


class ClientUpdate(ClientBase):
    """
    Update schema for a client.

    Attributes:
        id (int): The ID of the client to be updated.
    """
    id: int


class Client(ClientBase):
    """
    Client schema for invoice management.

    Attributes:
        id (int): The ID of the client.
        invoices (List[Invoice]): The list of invoices associated
            with the client.
        created_by (int): The ID of the user who created the client.

    Config:
        from_attributes (bool): Whether to load attributes from the
            class definition.
    """
    id: int
    invoices: List[Invoice] = []
    created_by: int

    class Config:
        from_attributes = True
