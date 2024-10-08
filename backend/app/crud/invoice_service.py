# Path: backend/app/crud/invoice_service.py

from sqlalchemy.orm import Session, joinedload
from app.db.models.invoice import InvoiceService as InvoiceServiceModel
from app.schemas.invoice import InvoiceServiceCreate, InvoiceServiceUpdate
from app.db.models.service import Service as ServiceModel
from app.db.models.invoice import Invoice as InvoiceModel
from fastapi import HTTPException, status


def create_invoice_service(db: Session, invoice_service: InvoiceServiceCreate):
    """
    Create an invoice service.

    Args:
        db (Session): The database session.
        invoice_service (InvoiceServiceCreate): The invoice service data.

    Raises:
        HTTPException: If the service or invoice with the given ID does not exist.

    Returns:
        InvoiceServiceModel: The created invoice service.
    """
    db_service = db.query(ServiceModel).filter(
        ServiceModel.id == invoice_service.service_id).first()
    if not db_service:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Service with the given ID does not exist"
        )
    db_invoice = db.query(InvoiceModel).filter(
        InvoiceModel.id == invoice_service.invoice_id).first()
    if not db_invoice:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invoice with the given ID does not exist"
        )
    db_invoice_service = InvoiceServiceModel(**invoice_service.model_dump())
    db.add(db_invoice_service)
    db.commit()
    db.refresh(db_invoice_service)
    return db_invoice_service


def get_invoice_service(db: Session, invoice_service_id: int):
    """
    Retrieve an invoice service from the database by its ID.

    Args:
        db (Session): The database session.
        invoice_service_id (int): The ID of the invoice service to retrieve.

    Returns:
        InvoiceServiceModel: The retrieved invoice service.
    """
    return db.query(InvoiceServiceModel).filter(InvoiceServiceModel.id == invoice_service_id).first()


def get_invoice_services(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of invoice services from the database.

    Args:
        db (Session): The database session.
        skip (int, optional): The number of records to skip. Defaults to 0.
        limit (int, optional): The maximum number of records to retrieve. Defaults to 100.

    Returns:
        List[InvoiceServiceModel]: A list of invoice services.
    """
    return db.query(InvoiceServiceModel).offset(skip).limit(limit).all()


def update_invoice_service(db: Session, invoice_service: InvoiceServiceUpdate):
    """
    Update an invoice service in the database.

    Args:
        db (Session): The database session.
        invoice_service (InvoiceServiceUpdate): The updated invoice service.

    Returns:
        InvoiceServiceModel: The updated invoice service in the database.
    """
    db_invoice_service = db.query(InvoiceServiceModel).filter(
        InvoiceServiceModel.id == invoice_service.id).first()
    if db_invoice_service:
        db_invoice_service.quantity = invoice_service.quantity
        db.commit()
        db.refresh(db_invoice_service)
    return db_invoice_service


def delete_invoice_service(db: Session, invoice_service_id: int):
    """
    Deletes an invoice service from the database.

    Args:
        db (Session): The database session.
        invoice_service_id (int): The ID of the invoice service to delete.

    Returns:
        InvoiceServiceModel: The deleted invoice service, or None if it doesn't exist.
    """
    db_invoice_service = db \
        .query(InvoiceServiceModel) \
        .options(joinedload(InvoiceServiceModel.service)) \
        .filter(InvoiceServiceModel.id == invoice_service_id) \
        .first()
    if db_invoice_service:
        db.delete(db_invoice_service)
        db.commit()
    return db_invoice_service
