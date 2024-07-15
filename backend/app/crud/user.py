from sqlalchemy.orm import Session
from app.db.models.user import User as UserModel
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from typing import Optional


def query_user_by_email(db: Session, email: str) -> Optional[UserModel]:
    return db.query(UserModel).filter(UserModel.email == email).first()


def query_user_by_id(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def create_user(db: Session, user: UserCreate):
    db_user = UserModel(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email.lower(),
        hashed_password=get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
