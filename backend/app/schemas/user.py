from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    """
    Represents the base schema for a user.

    Attributes:
        first_name (Optional[str]): The first name of the user. Defaults to None.
        last_name (Optional[str]): The last name of the user. Defaults to None.
        email (EmailStr): The email address of the user.
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr


class UserCreate(UserBase):
    """
    Create a new user.

    Attributes:
        password (str): The password for the user.
    """
    password: str


class UserLogin(BaseModel):
    """
    UserLogin schema for user login information.

    Attributes:
        email (EmailStr): The email address of the user.
        password (str): The password of the user.
    """
    email: EmailStr
    password: str


class User(UserBase):
    """
    User class representing a user in the system.

    Attributes:
        id (int): The unique identifier for the user.

    Config:
        from_attributes (bool): Indicates whether to populate the
            class attributes from the input attributes.
    """
    id: int

    class Config:
        from_attributes = True
