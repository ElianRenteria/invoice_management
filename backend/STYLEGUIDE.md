# Invoice Management API Project Style Guide

This style guide outlines the design patterns and coding styles used throughout the Invoice Management API project. All team members should adhere to these guidelines to ensure consistency and maintainability of the codebase.

## General Guidelines

1. **Follow PEP 8**: All Python code should adhere to the PEP 8 style guide. This includes conventions for naming, spacing, and formatting.
2. **Use Type Hints**: Always use type hints for function signatures and variable declarations.
3. **Write Docstrings**: Use docstrings to document all modules, classes, and functions. Follow the Google style for docstrings.

## Project Structure

- **Main Entry Point**: `main.py` initializes the FastAPI application and includes middleware configurations.
- **Configuration**: Configurations are managed using Pydantic settings in `app/core/config.py`.
- **Database**: SQLAlchemy ORM is used for database models. All models are defined in the `app/db/models` directory.
- **Schemas**: Pydantic schemas are defined in the `app/schemas` directory.
- **CRUD Operations**: CRUD operations are defined in the `app/crud` directory.
- **API Endpoints**: API routes and endpoints are defined in the `app/api/v1/endpoints` directory.

## Code Style

### Import Statements

- **Standard Library Imports**: Import standard libraries first.
- **Third-Party Imports**: Import third-party libraries second.
- **Local Imports**: Import local modules last.

Example:

```python
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.schemas.client as schemas
import app.crud.client as crud
from app.api import deps
```

### Naming Conventions

- **Classes**: Use `PascalCase` for class names.
- **Variables and Functions**: Use `snake_case` for variable and function names.
- **Constants**: Use `UPPER_SNAKE_CASE` for constants.

### Function Definitions

- **Type Hints**: Use type hints for all function parameters and return types.
- **Docstrings**: Document each function with a docstring.

Example:

```python
def get_client(db: Session, client_id: int) -> schemas.Client:
    """
    Retrieve a client by ID.

    Args:
        db (Session): Database session.
        client_id (int): ID of the client to retrieve.

    Returns:
        schemas.Client: Retrieved client.
    """
    return db.query(ClientModel).filter(ClientModel.id == client_id).first()
```

### Database Models

- **Base Class**: All models should inherit from the `Base` class.
- **Relationships**: Define relationships using SQLAlchemy's `relationship` and `ForeignKey`.

Example:

```python
class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    invoices = relationship("Invoice", cascade="all, delete-orphan", back_populates="client")
```

### Pydantic Schemas

Pydantic schemas are used to define the shape of the data for request and response validation. There are different types of schemas based on their usage:

- **Base Schemas**: Define the common attributes shared among the create, update, and read schemas. They serve as the base class for other schemas.

Example:

```python
class ClientBase(BaseModel):
    name: str
    email: str
```

- **Create Schemas**: Define the attributes required for creating a new record. These schemas usually extend from the base schema.

Example:

```python
class ClientCreate(ClientBase):
    pass
```

- **Update Schemas**: Define the attributes required for updating an existing record. These schemas usually extend from the base schema and include an `id` attribute.

Example:

```python
class ClientUpdate(ClientBase):
    id: int
```

- **Read Schemas**: Define the attributes included in the response when retrieving records. These schemas usually extend from the base schema and include additional read-only attributes.

Example:

```python
class Client(ClientBase):
    id: int
    invoices: List[Invoice] = []

    class Config:
        from_attributes = True
```

### CRUD Operations

- **Session Management**: Use the `Session` object for database operations.
- **Error Handling**: Use appropriate HTTP exceptions for error handling.

Example:

```python
def get_client(db: Session, client_id: int) -> schemas.Client:
    db_client = db.query(ClientModel).filter(ClientModel.id == client_id).first()
    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client
```

### API Endpoints

- **Router**: Define a `APIRouter` for each entity.
- **Dependency Injection**: Use `Depends` for injecting dependencies like the database session.

Example:

```python
@router.get("/", response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients
```

## Version Control

- **Commit Messages**: Use clear and descriptive commit messages.
- **Branching Model**: Use a branching model with `main` for production-ready code and `develop` for ongoing development. Feature branches should be used for new features and bug fixes.

## Documentation

- **API Documentation**: Ensure all endpoints are documented.
- **README**: Keep the `README.md` file up-to-date with installation instructions, usage examples, and any other relevant information.

By following this style guide, we can ensure that our codebase remains clean, consistent, and maintainable. If you have any questions or suggestions, please feel free to discuss them with the team or reach out to Salman for any clarification concerns.
