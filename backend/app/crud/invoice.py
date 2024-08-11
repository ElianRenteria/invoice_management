# Path: backend/app/crud/invoice.py

from sqlalchemy.orm import Session, joinedload
from app.db.models.invoice import Invoice as InvoiceModel, InvoiceService as InvoiceServiceModel
from app.schemas.invoice import InvoiceCreate, InvoiceUpdate
from app.db.models.user import User


def create_invoice(db: Session, user: User, invoice: InvoiceCreate):
    """
    Create a new invoice in the database.

    Args:
        db (Session): The database session.
        user (User): The user creating the invoice.
        invoice (InvoiceCreate): The invoice data.

    Returns:
        InvoiceModel: The created invoice.
    """
    db_invoice = InvoiceModel(**invoice.model_dump())
    db_invoice.created_by = user.id
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


def get_invoice(db: Session, user: User, invoice_id: int):
    """
    Retrieve an invoice from the database.

    Args:
        db (Session): The database session.
        user (User): The user object.
        invoice_id (int): The ID of the invoice to retrieve.

    Returns:
        InvoiceModel: The retrieved invoice object.
    """
    return db \
        .query(InvoiceModel) \
        .filter(InvoiceModel.created_by == user.id) \
        .filter(InvoiceModel.id == invoice_id) \
        .first()


def get_invoices(db: Session, user: User, skip: int = 0, limit: int = 100):
    """
    Retrieve invoices created by a specific user.

    Args:
        db (Session): The database session.
        user (User): The user object.
        skip (int, optional): The number of invoices to skip. Defaults to 0.
        limit (int, optional): The maximum number of invoices to retrieve. Defaults to 100.

    Returns:
        List[InvoiceModel]: A list of invoices created by the user.
    """
    return db \
        .query(InvoiceModel) \
        .filter(InvoiceModel.created_by == user.id) \
        .offset(skip) \
        .limit(limit) \
        .all()


def update_invoice(db: Session, user: User, invoice: InvoiceUpdate):
    """
    Update an invoice in the database.

    Args:
        db (Session): The database session.
        user (User): The user performing the update.
        invoice (InvoiceUpdate): The updated invoice data.

    Returns:
        InvoiceModel: The updated invoice object.
    """
    db_invoice = db \
        .query(InvoiceModel) \
        .filter(InvoiceModel.created_by == user.id) \
        .filter(InvoiceModel.id == invoice.id) \
        .first()
    if db_invoice:
        db_invoice.invoice_number = invoice.invoice_number
        db_invoice.date = invoice.date
        db_invoice.due_date = invoice.due_date
        db_invoice.status = invoice.status
        db_invoice.client_id = invoice.client_id
        db.commit()
        db.refresh(db_invoice)
    return db_invoice


def delete_invoice(db: Session, user: User, invoice_id: int):
    """
    Deletes an invoice from the database.

    Args:
        db (Session): The database session.
        user (User): The user who created the invoice.
        invoice_id (int): The ID of the invoice to be deleted.

    Returns:
        InvoiceModel: The deleted invoice if it exists, otherwise None.
    """
    db_invoice = db \
        .query(InvoiceModel) \
        .options(
            joinedload(InvoiceModel.services)
            .joinedload(InvoiceServiceModel.service)
        ) \
        .filter(InvoiceModel.created_by == user.id) \
        .filter(InvoiceModel.id == invoice_id) \
        .first()
    if db_invoice:
        db.delete(db_invoice)
        db.commit()
    return db_invoice
