# Path: backend/app/schemas/client.py

from app.schemas.invoice import Invoice

from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Literal
from datetime import datetime


class ClientStatus(str, Enum):
    """
    Enum class representing the status of a client.

    Attributes:
        active (str): Represents an active client.
        inactive (str): Represents an inactive client.
    """
    active = "active"
    inactive = "inactive"


class ClientBase(BaseModel):
    """
    ClientBase schema class.

    Attributes:
        name (str): The name of the client.
        email (str): The email of the client.
        phone (Optional[str]): The phone number of the client.
        facsimile (Optional[str]): The facsimile number of the client.
        address (Optional[Address]): The address of the client.
        billing_address (Optional[Address]): The billing address of the client.
        contact_person (Optional[str]): The contact person of the client.
        company_name (Optional[str]): The company name of the client.
        industry (Optional[str]): The industry of the client.
        website (Optional[str]): The website of the client.
        notes (Optional[str]): The notes of the client.
        status (Literal["active", "inactive"]): The status of the client.
    """
    name: str
    email: str
    phone: Optional[str] = None
    facsimile: Optional[str] = None
    contact_person: Optional[str] = None
    company_name: Optional[str] = None
    industry: Optional[str] = None
    website: Optional[str] = None
    notes: Optional[str] = None
    status: ClientStatus

    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    address_city: Optional[str] = None
    address_state: Optional[str] = None
    address_postal_code: Optional[str] = None
    address_country: Optional[str] = None

    billing_address_line1: Optional[str] = None
    billing_address_line2: Optional[str] = None
    billing_address_city: Optional[str] = None
    billing_address_state: Optional[str] = None
    address_postal_code: Optional[str] = None
    billing_address_country: Optional[str] = None


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
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        from_attributes = True
