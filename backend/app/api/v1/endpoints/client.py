# Path: backend/app/api/v1/endpoints/client.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.schemas.client as schemas
import app.crud.client as crud
from app.api import deps
from app.db.models.user import User

router = APIRouter()


@router.get("/", response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_user)):
    clients = crud.get_clients(db, user=current_user, skip=skip, limit=limit)
    return clients


@router.get("/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_user)):
    db_client = crud.get_client(db, user=current_user, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@ router.post("/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_user)):
    return crud.create_client(db=db, user=current_user, client=client)


@ router.put("/{client_id}", response_model=schemas.Client)
def update_client(client_id: int, client: schemas.ClientUpdate, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_user)):
    db_client = crud.get_client(db, user=current_user, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return crud.update_client(db=db, client=client)


@ router.delete("/{client_id}", response_model=schemas.Client)
def delete_client(client_id: int, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_user)):
    db_client = crud.get_client(db, user=current_user, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return crud.delete_client(db=db, user=current_user, client_id=client_id)
