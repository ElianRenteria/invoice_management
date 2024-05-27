# backend/app/api/v1/endpoints/service.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.schemas.service as schemas
import app.crud.service as crud
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Service)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(deps.get_db)):
    return crud.create_service(db=db, service=service)


@router.get("/{service_id}", response_model=schemas.Service)
def read_service(service_id: int, db: Session = Depends(deps.get_db)):
    db_service = crud.get_service(db, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service


@router.get("/", response_model=List[schemas.Service])
def read_services(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    services = crud.get_services(db, skip=skip, limit=limit)
    return services


@router.put("/", response_model=schemas.Service)
def update_service(service: schemas.ServiceUpdate, db: Session = Depends(deps.get_db)):
    db_service = crud.get_service(db, service.id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return crud.update_service(db=db, service=service)


@router.delete("/{service_id}", response_model=schemas.Service)
def delete_service(service_id: int, db: Session = Depends(deps.get_db)):
    db_service = crud.get_service(db, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return crud.delete_service(db=db, service_id=service_id)
