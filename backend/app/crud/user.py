from sqlalchemy.orm import Session
from app.db.models.user import User as UserModel
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from typing import Optional


def query_user_by_email(db: Session, email: str) -> Optional[UserModel]:
    """
    Retrieve a user from the database based on their email.

    Args:
        db (Session): The database session.
        email (str): The email of the user to retrieve.

    Returns:
        Optional[UserModel]: The user with the specified email, if found. Otherwise, None.
    """
    return db.query(UserModel).filter(UserModel.email == email).first()


def query_user_by_id(db: Session, user_id: int):
    """
    Retrieve a user from the database by their ID.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to retrieve.

    Returns:
        UserModel: The user with the specified ID, or None if not found.
    """
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def create_user(db: Session, user: UserCreate):
    """
    Create a new user in the database.

    Args:
        db (Session): The database session.
        user (UserCreate): The user data to be created.

    Returns:
        UserModel: The created user object.
    """
    db_user = UserModel(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email.lower(),
        date_of_birth=user.date_of_birth,
        hashed_password=get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
