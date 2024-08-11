# Path: backend/app/crud/client.py
from sqlalchemy.orm import Session, joinedload
from app.db.models.client import Client as ClientModel
from app.schemas.client import ClientCreate, ClientUpdate
from app.db.models.invoice import Invoice as InvoiceModel, InvoiceService as InvoiceServiceModel
from app.db.models.user import User


def create_client(db: Session, user: User, client: ClientCreate):
    """
    Create a new client in the database.

    Args:
        db (Session): The database session.
        user (User): The user creating the client.
        client (ClientCreate): The client data.

    Returns:
        ClientModel: The created client.
    """
    db_client = ClientModel(**client.model_dump())
    db_client.created_by = user.id
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_client(db: Session, user: User, client_id: int):
    """
    Retrieve a client from the database.

    Args:
        db (Session): The database session.
        user (User): The user object.
        client_id (int): The ID of the client to retrieve.

    Returns:
        ClientModel: The client object if found, otherwise None.
    """
    return db \
        .query(ClientModel) \
        .filter(ClientModel.id == client_id) \
        .filter(ClientModel.created_by == user.id) \
        .first()


def get_clients(db: Session, user: User, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of clients created by a specific user.

    Args:
        db (Session): The database session.
        user (User): The user object.
        skip (int, optional): The number of clients to skip. Defaults to 0.
        limit (int, optional): The maximum number of clients to retrieve. Defaults to 100.

    Returns:
        List[ClientModel]: A list of client objects.
    """
    return db \
        .query(ClientModel) \
        .filter(ClientModel.created_by == user.id) \
        .offset(skip) \
        .limit(limit) \
        .all()


def update_client(db: Session, user: User, client: ClientUpdate):
    """
    Update a client in the database.

    Args:
        db (Session): The database session.
        user (User): The user performing the update.
        client (ClientUpdate): The updated client information.

    Returns:
        ClientModel: The updated client object.

    """
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
    """
    Delete a client from the database.

    Args:
        db (Session): The database session.
        user (User): The user performing the deletion.
        client_id (int): The ID of the client to be deleted.

    Returns:
        ClientModel: The deleted client if found, otherwise None.
    """
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
