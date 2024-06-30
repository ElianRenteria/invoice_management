# Path: backend/app/api/v1/endpoints/client.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.schemas.login as schemas
import app.crud.users as crud
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.LoginResponse)
def login_response(request: schemas.LoginRequest, db: Session = Depends(deps.get_db)):
    return schemas.LoginResponse(name="nick", username="sddas", email=request.email)
    #return crud.create_user(db=db, service=request)