# Path: backend/app/api/v1/endpoints/invoice_service.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.schemas.invoice as schemas
import app.crud.invoice_service as crud
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.InvoiceService)
def create_invoice_service(
    invoice_service: schemas.InvoiceServiceCreate,
    db: Session = Depends(deps.get_db)
):
    """
    Create a new invoice service.

    Args:
        invoice_service (schemas.InvoiceServiceCreate): The invoice
            service data.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).

    Returns:
        The created invoice service.
    """
    return crud.create_invoice_service(db=db, invoice_service=invoice_service)


@router.get("/{invoice_service_id}", response_model=schemas.InvoiceService)
def read_invoice_service(
    invoice_service_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    Retrieve an invoice service by its ID.

    Args:
        invoice_service_id (int): The ID of the invoice service.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).

    Returns:
        db_invoice_service: The retrieved invoice service.

    Raises:
        HTTPException: If the invoice service is not found.
    """
    db_invoice_service = crud.get_invoice_service(
        db, invoice_service_id=invoice_service_id)
    if db_invoice_service is None:
        raise HTTPException(status_code=404, detail="InvoiceService not found")
    return db_invoice_service


@router.get("/", response_model=List[schemas.InvoiceService])
def read_invoice_services(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db)
):
    """
    Reads invoice services from the database.

    Args:
        skip (int): Number of records to skip (default: 0).
        limit (int): Maximum number of records to retrieve (default: 100).
        db (Session): Database session dependency.

    Returns:
        List[schemas.InvoiceService]: List of invoice services retrieved
            from the database.
    """
    invoice_services = crud.get_invoice_services(db, skip=skip, limit=limit)
    return invoice_services


@router.put("/{invoice_service_id}", response_model=schemas.InvoiceService)
def update_invoice_service(
    invoice_service_id: int,
    invoice_service: schemas.InvoiceServiceUpdate,
    db: Session = Depends(deps.get_db)
):
    """
    Update an invoice service in the database.

    Args:
        invoice_service_id (int): The ID of the invoice service to update.
        invoice_service (schemas.InvoiceServiceUpdate): The updated invoice
            service data.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).

    Returns:
        schemas.InvoiceService: The updated invoice service.

    Raises:
        HTTPException: If the invoice service with the given ID is not found.
    """
    db_invoice_service = crud.get_invoice_service(
        db, invoice_service_id=invoice_service_id)
    if db_invoice_service is None:
        raise HTTPException(status_code=404, detail="InvoiceService not found")
    return crud.update_invoice_service(db=db, invoice_service=invoice_service)


@router.delete("/{invoice_service_id}", response_model=schemas.InvoiceService)
def delete_invoice_service(
    invoice_service_id: int,
    db: Session = Depends(deps.get_db)
):
    """
    Delete an invoice service by its ID.

    Args:
        invoice_service_id (int): The ID of the invoice service to delete.
        db (Session, optional): The database session. Defaults to Depends(deps.get_db).

    Raises:
        HTTPException: If the invoice service is not found.

    Returns:
        None
    """
    db_invoice_service = crud.get_invoice_service(
        db, invoice_service_id=invoice_service_id)
    if db_invoice_service is None:
        raise HTTPException(status_code=404, detail="InvoiceService not found")
    return crud.delete_invoice_service(
        db=db, invoice_service_id=invoice_service_id)
