from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.user import create_user, query_user_by_username
from app.schemas.user import UserCreate, UserLogin, User
from app.core.security import create_access_token, verify_password

router = APIRouter()


@router.get("/me", response_model=User)
def user_me(current_user: User = Depends(deps.get_current_user)):
    return current_user


@router.post("/signup", response_model=User)
def sign_up(user: UserCreate, db: Session = Depends(deps.get_db)):
    if query_user_by_username(db, user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    db_user = create_user(db, user)
    return db_user


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(deps.get_db)):
    _user = query_user_by_username(db, user.username)
    if not _user or not verify_password(user.password, _user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": _user.username})
    return {"access_token": access_token, "token_type": "bearer"}
