# Path: backend/app/crud/service.py

from sqlalchemy.orm import Session
from app.db.models.service import Service as ServiceModel
from app.schemas.service import ServiceCreate, ServiceUpdate
from app.schemas.user import User


def create_service(db: Session, user: User, service: ServiceCreate):
    """
    Create a new service in the database.

    Args:
        db (Session): The database session.
        user (User): The user creating the service.
        service (ServiceCreate): The service data to be created.

    Returns:
        ServiceModel: The created service.
    """
    db_service = ServiceModel(**service.model_dump())
    db_service.created_by = user.id
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


def get_service(db: Session, user: User, service_id: int):
    """
    Retrieve a service by its ID that belongs to a specific user.

    Args:
        db (Session): The database session.
        user (User): The user object.
        service_id (int): The ID of the service.

    Returns:
        ServiceModel: The service object if found, otherwise None.
    """
    return db \
        .query(ServiceModel) \
        .filter(ServiceModel.created_by == user.id) \
        .filter(ServiceModel.id == service_id) \
        .first()


def get_services(db: Session, user: User, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of services created by a specific user.

    Args:
        db (Session): The database session.
        user (User): The user object.
        skip (int, optional): The number of services to skip. Defaults to 0.
        limit (int, optional): The maximum number of services to retrieve. Defaults to 100.

    Returns:
        List[ServiceModel]: A list of service objects.
    """
    return db \
        .query(ServiceModel) \
        .filter(ServiceModel.created_by == user.id) \
        .offset(skip) \
        .limit(limit) \
        .all()


def update_service(db: Session, user: User, service: ServiceUpdate):
    """
    Update a service in the database.

    Args:
        db (Session): The database session.
        user (User): The user performing the update.
        service (ServiceUpdate): The updated service information.

    Returns:
        ServiceModel: The updated service model.
    """
    db_service = db \
        .query(ServiceModel) \
        .filter(ServiceModel.created_by == user.id) \
        .filter(ServiceModel.id == service.id) \
        .first()
    if db_service:
        db_service.name = service.name
        db_service.price = service.price
        db.commit()
        db.refresh(db_service)
    return db_service


def delete_service(db: Session, user: User, service_id: int):
    """
    Deletes a service from the database.

    Args:
        db (Session): The database session.
        user (User): The user who created the service.
        service_id (int): The ID of the service to be deleted.

    Returns:
        ServiceModel: The deleted service if it exists, otherwise None.
    """
    db_service = db \
        .query(ServiceModel) \
        .filter(ServiceModel.created_by == user.id) \
        .filter(ServiceModel.id == service_id) \
        .first()
    if db_service:
        db.delete(db_service)
        db.commit()
    return db_service
