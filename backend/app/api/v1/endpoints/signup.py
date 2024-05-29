# Path: backend/app/api/v1/endpoints/client.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.schemas.signup as schemas
import app.crud.users as crud
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.SignUpResponse)
def signup_response(request: schemas.SignUpRequest, db: Session = Depends(deps.get_db)):
    #return schemas.SignUpResponse(name=request.name, username=request.username, email=request.email)
    return crud.create_user(db=db, user=request)