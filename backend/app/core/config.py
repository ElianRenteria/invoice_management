# Path: backend/app/core/config.py

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from base64 import b64decode
import os

load_dotenv()
"""
Load the environment variables from the .env file.
"""


class Settings(BaseSettings):
    """
    Configuration settings for the Invoice Management application.

    Attributes:
        PROJECT_NAME (str): The name of the project.
        VERSION (str): The version of the project.
        API_V1_STR (str): The base URL for the API.
        SQLALCHEMY_DATABASE_URI (str): The URI for the SQLite database.
        JWT_PRIVATE_KEY (str): The private key for JWT token generation.
        JWT_PUBLIC_KEY (str): The public key for JWT token verification.
        JWT_ALGORITHM (str): The algorithm used for JWT token encoding.
        JWT_ACCESS_TOKEN_EXPIRE_MINUTES (int): The expiration time for
            JWT access tokens in minutes.

    """

    PROJECT_NAME: str = "Invoice Management"
    VERSION: str = "0.0.1"
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./test.db"

    JWT_PRIVATE_KEY: str = b64decode(
        os.getenv("PRIVATE_KEY_BASE64")).decode('utf-8')
    JWT_PUBLIC_KEY: str = b64decode(
        os.getenv("PUBLIC_KEY_BASE64")).decode('utf-8')
    JWT_ALGORITHM: str = "RS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        case_sensitive = True


settings = Settings()
"""
An instance of the Settings class.
"""
