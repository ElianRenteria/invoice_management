# Path: backend/app/api/v1/api.py
"""
This module defines the API routes for version 1 of the
invoice management backend.

The API routes include:
- Authentication routes: /auth
- Client routes: /clients
- Invoice routes: /invoices
- Service routes: /services
- Invoice Service routes: /invoice_services
"""

from fastapi import APIRouter

from app.api.v1.endpoints import client, invoice, service, \
    invoice_service, authentication

api_router = APIRouter()

api_router.include_router(
    authentication.router, prefix="/auth", tags=["auth"])
api_router.include_router(
    client.router, prefix="/clients", tags=["clients"])
api_router.include_router(
    invoice.router, prefix="/invoices", tags=["invoices"])
api_router.include_router(
    service.router, prefix="/services", tags=["services"])
api_router.include_router(
    invoice_service.router,
    prefix="/invoice_services", tags=["invoice_services"])
