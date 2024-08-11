# Path: backend/app/schemas/service.py

from pydantic import BaseModel


class ServiceBase(BaseModel):
    """
    Represents a service.

    Attributes:
        name (str): The name of the service.
        price (float): The price of the service.
    """
    name: str
    price: float


class ServiceCreate(ServiceBase):
    """
    Create a new service.

    This class represents the schema for creating a new service.

    Attributes:
        Inherits all attributes from the ServiceBase class.
    """
    pass


class ServiceUpdate(ServiceBase):
    """
    Update schema for a service.

    Attributes:
        id (int): The ID of the service to be updated.
    """
    id: int


class Service(ServiceBase):
    """
    Service schema class for invoice management backend.

    Attributes:
        id (int): The ID of the service.

    Config:
        from_attributes (bool): Whether to load attributes from the model.
    """
    id: int

    class Config:
        from_attributes = True
