import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Invoice Manager"
    PROJECT_VERSION: str = "0.0.1"

    USE_SQLITE_DB: str = None
    POSTGRES_USER: str = None
    POSTGRES_PASSWORD = None
    POSTGRES_SERVER: str = None
    POSTGRES_PORT: str = None
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = None
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins

    TEST_USER_EMAIL = "test@example.com"


settings = Settings()