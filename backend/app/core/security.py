from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
"""
An instance of the CryptContext class from the passlib library.
"""


def verify_password(plain_password, hashed_password):
    """
    Verify if the plain password matches the hashed password.

    Args:
        plain_password (str): The plain password to be verified.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the plain password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    Generate a password hash using the provided password.

    Parameters:
    - password (str): The password to be hashed.

    Returns:
    - str: The hashed password.
    """
    return pwd_context.hash(password)


def create_access_token(data: dict):
    """
    Generates an access token based on the provided data.

    Args:
        data (dict): The data to be encoded in the access token.

    Returns:
        str: The encoded access token.
    """
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
    """
    Decode the access token and return the decoded token if it is valid and has not expired,
    otherwise return None.

    Parameters:
    - token (str): The access token to be decoded.

    Returns:
    - dict or None: The decoded token as a dictionary if it is valid and has not expired,
      otherwise None.
    """
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
