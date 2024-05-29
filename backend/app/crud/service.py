# Path: backend/app/crud/service.py

from sqlalchemy.orm import Session
from app.db.models.service import Service as ServiceModel
from app.schemas.service import ServiceCreate, ServiceUpdate


def create_service(db: Session, service: ServiceCreate):
    db_service = ServiceModel(**service.model_dump())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


def get_service(db: Session, service_id: int):
    return db.query(ServiceModel).filter(ServiceModel.id == service_id).first()


def get_services(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ServiceModel).offset(skip).limit(limit).all()


def update_service(db: Session, service: ServiceUpdate):
    db_service = db.query(ServiceModel).filter(
        ServiceModel.id == service.id).first()
    if db_service:
        db_service.name = service.name
        db_service.price = service.price
        db.commit()
        db.refresh(db_service)
    return db_service


def delete_service(db: Session, service_id: int):
    db_service = db.query(ServiceModel).filter(
        ServiceModel.id == service_id).first()
    if db_service:
        db.delete(db_service)
        db.commit()
    return db_service
