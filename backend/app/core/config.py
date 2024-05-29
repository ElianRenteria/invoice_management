# Path: backend/app/core/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Invoice Management"
    VERSION: str = "0.0.1"
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./test.db"

    class Config:
        case_sensitive = True


settings = Settings()
