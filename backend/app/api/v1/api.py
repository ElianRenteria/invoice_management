# Path: backend/app/api/v1/api.py

from fastapi import APIRouter

from app.api.v1.endpoints import client, invoice

api_router = APIRouter()

api_router.include_router(
    client.router, prefix="/clients", tags=["clients"])
api_router.include_router(
    invoice.router, prefix="/invoices", tags=["invoices"])
