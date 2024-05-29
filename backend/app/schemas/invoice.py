# Path: backend/app/schemas/invoice.py

from pydantic import BaseModel, computed_field
from datetime import date as Date
from typing import List, Optional
from enum import Enum

from app.schemas.payment import Payment, PaymentCreate
from app.schemas.service import Service


class InvoiceStatus(Enum):
    ESTIMATE = 0
    DRAFT = 1
    PENDING_APPROVAL = 2
    APPROVED = 3
    SENT = 4
    VIEWED = 5
    PARTIALLY_PAID = 6
    PAID = 7
    OVERDUE = 8
    DISPUTED = 9
    CANCELLED = 10
    WRITTEN_OFF = 11
    REFUNDED = 12


class InvoiceServiceBase(BaseModel):
    service_id: int
    quantity: int


class InvoiceServiceCreate(InvoiceServiceBase):
    invoice_id: int


class InvoiceServiceUpdate(InvoiceServiceBase):
    id: int


class InvoiceService(InvoiceServiceBase):
    id: int
    invoice_id: int
    service: Service

    class Config:
        from_attributes = True


class InvoiceBase(BaseModel):
    invoice_number: str
    date: Date
    due_date: Optional[Date] = None
    status: InvoiceStatus
    client_id: int


class InvoiceCreate(InvoiceBase):
    services: List[InvoiceServiceCreate] = []
    payments: List[PaymentCreate] = []


class InvoiceUpdate(InvoiceBase):
    id: int

    services: List[InvoiceServiceCreate] = []
    payments: List[PaymentCreate] = []


class Invoice(InvoiceBase):
    id: int
    services: List[InvoiceService] = []
    payments: List[Payment] = []

    @computed_field
    def total(self) -> float:
        return sum([service.service.price * service.quantity for service in self.services])

    @computed_field
    def total_paid(self) -> float:
        return sum([payment.amount for payment in self.payments])

    @computed_field
    def total_due(self) -> float:
        return self.total - self.total_paid

    class Config:
        from_attributes = True
