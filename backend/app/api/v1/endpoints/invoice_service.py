# Path: backend/app/api/v1/endpoints/invoice_service.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.schemas.invoice as schemas
import app.crud.invoice_service as crud
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.InvoiceService)
def create_invoice_service(invoice_service: schemas.InvoiceServiceCreate, db: Session = Depends(deps.get_db)):
    return crud.create_invoice_service(db=db, invoice_service=invoice_service)


@router.get("/{invoice_service_id}", response_model=schemas.InvoiceService)
def read_invoice_service(invoice_service_id: int, db: Session = Depends(deps.get_db)):
    db_invoice_service = crud.get_invoice_service(
        db, invoice_service_id=invoice_service_id)
    if db_invoice_service is None:
        raise HTTPException(status_code=404, detail="InvoiceService not found")
    return db_invoice_service


@router.get("/", response_model=List[schemas.InvoiceService])
def read_invoice_services(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    invoice_services = crud.get_invoice_services(db, skip=skip, limit=limit)
    return invoice_services


@router.put("/{invoice_service_id}", response_model=schemas.InvoiceService)
def update_invoice_service(invoice_service_id: int, invoice_service: schemas.InvoiceServiceUpdate, db: Session = Depends(deps.get_db)):
    db_invoice_service = crud.get_invoice_service(
        db, invoice_service_id=invoice_service_id)
    if db_invoice_service is None:
        raise HTTPException(status_code=404, detail="InvoiceService not found")
    return crud.update_invoice_service(db=db, invoice_service=invoice_service)


@router.delete("/{invoice_service_id}", response_model=schemas.InvoiceService)
def delete_invoice_service(invoice_service_id: int, db: Session = Depends(deps.get_db)):
    db_invoice_service = crud.get_invoice_service(
        db, invoice_service_id=invoice_service_id)
    if db_invoice_service is None:
        raise HTTPException(status_code=404, detail="InvoiceService not found")
    return crud.delete_invoice_service(db=db, invoice_service_id=invoice_service_id)
