from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt \
        .encode(
            to_encode,
            settings.JWT_PRIVATE_KEY,
            algorithm=settings.JWT_ALGORITHM
        )
    return encoded_jwt


def decode_access_token(token: str):
    try:
        decoded_token = jwt \
            .decode(
                token,
                settings.JWT_PUBLIC_KEY,
                algorithms=[settings.JWT_ALGORITHM]
            )
        return decoded_token \
            if datetime.fromtimestamp(decoded_token.get("exp"), timezone.utc) \
            >= datetime.now(timezone.utc) \
            else None
    except JWTError:
        return None
