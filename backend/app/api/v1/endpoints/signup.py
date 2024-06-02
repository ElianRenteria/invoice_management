# Path: backend/app/api/v1/endpoints/signup.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.schemas.signup as schemas
import app.crud.users as crud
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.SignUpResponse)
def signup_response(request: schemas.SignUpRequest, db: Session = Depends(deps.get_db)):
    """
    Create new user if they already don't have an account
    """
    db_user = crud.get_user(db, user_email=request.email)
    if db_user is None:
        return crud.create_user(db=db, user=request)
    raise HTTPException(status_code=404, detail="User already exists")