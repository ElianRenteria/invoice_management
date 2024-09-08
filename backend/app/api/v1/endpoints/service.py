# backend/app/api/v1/endpoints/service.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.schemas.service as schemas
import app.crud.service as crud
from app.api import deps
from app.schemas.user import User

router = APIRouter()


@router.post("/", response_model=schemas.Service)
def create_service(
    service: schemas.ServiceCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Create a new service.

    Args:
        service (schemas.ServiceCreate): The service data to be created.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).
        current_user (User, optional): The current authenticated user.
            Defaults to Depends(deps.get_current_user).

    Returns:
        The created service.
    """
    return crud.create_service(db=db, user=current_user, service=service)


@router.get("/{service_id}", response_model=schemas.Service)
def read_service(
    service_id: int,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Retrieve a service by its ID.

    Args:
        service_id (int): The ID of the service to retrieve.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).
        current_user (User, optional): The current authenticated user.
            Defaults to Depends(deps.get_current_user).

    Returns:
        The service with the specified ID.

    Raises:
        HTTPException: If the service is not found.
    """
    db_service = crud.get_service(db, user=current_user, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service


@router.get("/", response_model=List[schemas.Service])
def read_services(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Retrieve services.

    Args:
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to retrieve. Defaults to 100.
        db (Session, optional): Database session.
            Defaults to Depends(deps.get_db).
        current_user (User, optional): Current user.
            Defaults to Depends(deps.get_current_user).

    Returns:
        services: List of services.
    """
    services = crud.get_services(db, user=current_user, skip=skip, limit=limit)
    return services


@router.put("/{service_id}", response_model=schemas.Service)
def update_service(
    service_id: int,
    service: schemas.ServiceUpdate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Update a service in the database.

    Args:
        service (schemas.ServiceUpdate): The updated service information.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).
        current_user (User, optional): The current authenticated user.
            Defaults to Depends(deps.get_current_user).

    Raises:
        HTTPException: If the service is not found in the database.

    Returns:
        The updated service.
    """
    db_service = crud.get_service(db, user=current_user, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return crud.update_service(db=db, user=current_user, service=service)


@router.delete("/{service_id}", response_model=schemas.Service)
def delete_service(
    service_id: int,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Delete a service.

    Args:
        service_id (int): The ID of the service to be deleted.
        db (Session, optional): The database session.
            Defaults to Depends(deps.get_db).
        current_user (User, optional): The current user.
            Defaults to Depends(deps.get_current_user).

    Raises:
        HTTPException: If the service is not found.

    Returns:
        None
    """
    db_service = crud.get_service(db, user=current_user, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return crud.delete_service(db=db, user=current_user, service_id=service_id)
