# Path: backend/app/crud/invoice.py

from sqlalchemy.orm import Session, joinedload
from app.db.models.invoice import Invoice as InvoiceModel, InvoiceService as InvoiceServiceModel
from app.schemas.invoice import InvoiceCreate, InvoiceUpdate
from app.db.models.user import User


def create_invoice(db: Session, user: User, invoice: InvoiceCreate):
    db_invoice = InvoiceModel(**invoice.model_dump())
    db_invoice.created_by = user.id
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


def get_invoice(db: Session, user: User, invoice_id: int):
    return db \
        .query(InvoiceModel) \
        .filter(InvoiceModel.created_by == user.id) \
        .filter(InvoiceModel.id == invoice_id) \
        .first()


def get_invoices(db: Session, user: User, skip: int = 0, limit: int = 100):
    return db \
        .query(InvoiceModel) \
        .filter(InvoiceModel.created_by == user.id) \
        .offset(skip) \
        .limit(limit) \
        .all()


def update_invoice(db: Session, user: User, invoice: InvoiceUpdate):
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
