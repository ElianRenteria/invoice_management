from sqlalchemy.orm import Session
from app.db.models.user import User as UserModel
from app.schemas.user import UserCreate
from app.core.security import get_password_hash


def query_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username.lower()).first()


def query_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email.lower()).first()


def create_user(db: Session, user: UserCreate):
    db_user = UserModel(
        username=user.username.lower(),
        email=user.email.lower(),
        hashed_password=get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
