# Path: backend/app/api/deps.py

from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.core.security import decode_access_token
from app.core.config import settings
from app.crud.user import query_user_by_email
from app.db.models.user import User
from app.db.session import SessionLocal
from typing import Generator


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = HTTPException(
        status_code=401, detail="Could not validate credentials")
    try:
        if (payload := decode_access_token(token)) is None:
            print("payload is None")
            raise credentials_exception
        if (email := payload.get("sub")) is None:
            print("user_id is None")
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = query_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user
