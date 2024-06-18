# Path: backend/app/core/config.py

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from base64 import b64decode
import os

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Invoice Management"
    VERSION: str = "0.0.1"
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./test.db"

    JWT_PRIVATE_KEY: str = b64decode(
        os.getenv("PRIVATE_KEY_BASE64")).decode('utf-8')
    JWT_PUBLIC_KEY: str = b64decode(
        os.getenv("PUBLIC_KEY_BASE64")).decode('utf-8')
    JWT_ALGORITHM: str = "RS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        case_sensitive = True


settings = Settings()
