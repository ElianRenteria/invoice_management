# Path: backend/app/api/v1/endpoints/client.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.schemas.invoice as schemas
import app.crud.invoice as crud
from app.db.models.user import User
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Invoice])
def read_invoices(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Retrieve invoices from the database.

    Args:
        skip (int, optional): Number of invoices to skip.
            Defaults to 0.
        limit (int, optional): Maximum number of invoices to retrieve.
            Defaults to 100.
        db (Session, optional): Database session.
            Defaults to Depends(deps.get_db).
        current_user (User, optional): Current user.
            Defaults to Depends(deps.get_current_user).

    Returns:
        List[Invoice]: List of invoices retrieved from the database.
    """
    return crud.get_invoices(db, user=current_user, skip=skip, limit=limit)
    return crud \
        .get_invoices(db, user=current_user, skip=skip, limit=limit)


@router.get("/{invoice_id}", response_model=schemas.Invoice)
def read_invoice(
    invoice_id: int,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Retrieve an invoice from the database.

    Args:
        invoice_id (int): The ID of the invoice to retrieve.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).
        current_user (User, optional): The current user.
            Defaults to Depends(deps.get_current_user).

    Returns:
        Invoice: The retrieved invoice.

    Raises:
        HTTPException: If the invoice is not found.
    """
    db_invoice = crud.get_invoice(db, user=current_user, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice


@ router.post("/", response_model=schemas.Invoice)
def create_invoice(
    invoice: schemas.InvoiceCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Create a new invoice.

    Args:
        invoice (schemas.InvoiceCreate): The invoice data to be created.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).
        current_user (User, optional): The current authenticated user.
            Defaults to Depends(deps.get_current_user).

    Returns:
        The created invoice.
    """
    # TODO: Add Constraint to Check if Invoice Number (NOT ID) is Unique
    db_invoice = crud.create_invoice(db=db, user=current_user, invoice=invoice)
    return db_invoice


@router.put("/{invoice_id}", response_model=schemas.Invoice)
def update_invoice(
    invoice_id: int,
    invoice: schemas.InvoiceUpdate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Update an invoice in the database.

    Args:
        invoice_id (int): The ID of the invoice to update.
        invoice (schemas.InvoiceUpdate): The updated invoice data.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).
        current_user (User, optional): The current user.
            Defaults to Depends(deps.get_current_user).

    Raises:
        HTTPException: If the invoice is not found.

    Returns:
        schemas.Invoice: The updated invoice.
    """
    db_invoice = crud.get_invoice(db, user=current_user, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return crud.update_invoice(db=db, user=current_user, invoice=invoice)


@router.delete("/{invoice_id}", response_model=schemas.Invoice)
def delete_invoice(
    invoice_id: int,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Delete an invoice.

    Args:
        invoice_id (int): The ID of the invoice to be deleted.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).
        current_user (User, optional): The current user.
            Defaults to Depends(deps.get_current_user).

    Raises:
        HTTPException: If the invoice is not found.

    Returns:
        None
    """
    db_invoice = crud.get_invoice(db, user=current_user, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return crud.delete_invoice(db=db, user=current_user, invoice_id=invoice_id)
