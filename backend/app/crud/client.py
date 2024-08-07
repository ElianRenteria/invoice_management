# Path: backend/app/crud/client.py
from sqlalchemy.orm import Session, joinedload
from app.db.models.client import Client as ClientModel
from app.schemas.client import ClientCreate, ClientUpdate
from app.db.models.invoice import Invoice as InvoiceModel, InvoiceService as InvoiceServiceModel
from app.db.models.user import User


def create_client(db: Session, user: User, client: ClientCreate):
    db_client = ClientModel(**client.model_dump())
    db_client.created_by = user.id
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_client(db: Session, user: User, client_id: int):
    return db \
        .query(ClientModel) \
        .filter(ClientModel.id == client_id) \
        .filter(ClientModel.created_by == user.id) \
        .first()


def get_clients(db: Session, user: User, skip: int = 0, limit: int = 100):
    return db \
        .query(ClientModel) \
        .filter(ClientModel.created_by == user.id) \
        .offset(skip) \
        .limit(limit) \
        .all()


def update_client(db: Session, user: User, client: ClientUpdate):
    db_client = db \
        .query(ClientModel) \
        .filter(ClientModel.created_by == user.id) \
        .filter(ClientModel.id == client.id) \
        .first()
    if db_client:
        db_client.name = client.name
        db_client.email = client.email
        db.commit()
        db.refresh(db_client)
    return db_client


def delete_client(db: Session, user: User, client_id: int):
    db_client = db \
        .query(ClientModel) \
        .options(
            joinedload(ClientModel.invoices)
            .joinedload(InvoiceModel.services)
            .joinedload(InvoiceServiceModel.service)
        ) \
        .filter(ClientModel.created_by == user.id) \
        .filter(ClientModel.id == client_id) \
        .first()
    if db_client:
        db.delete(db_client)
        db.commit()
    return db_client
