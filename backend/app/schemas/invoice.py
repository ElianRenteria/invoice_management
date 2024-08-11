# Path: backend/app/schemas/invoice.py

from pydantic import BaseModel, computed_field
from datetime import date as Date
from typing import List, Optional
from enum import Enum

from app.schemas.payment import Payment, PaymentCreate
from app.schemas.service import Service


class InvoiceStatus(Enum):
    """
    Enum class representing the status of an invoice.

    Attributes:
        ESTIMATE (int): Represents the status of an estimated invoice.
        DRAFT (int): Represents the status of a draft invoice.
        PENDING_APPROVAL (int): Represents the status of an invoice
            pending approval.
        APPROVED (int): Represents the status of an approved invoice.
        SENT (int): Represents the status of a sent invoice.
        VIEWED (int): Represents the status of a viewed invoice.
        PARTIALLY_PAID (int): Represents the status of a partially
            paid invoice.
        PAID (int): Represents the status of a fully paid invoice.
        OVERDUE (int): Represents the status of an overdue invoice.
        DISPUTED (int): Represents the status of a disputed invoice.
        CANCELLED (int): Represents the status of a cancelled invoice.
        WRITTEN_OFF (int): Represents the status of a written-off invoice.
        REFUNDED (int): Represents the status of a refunded invoice.
    """
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
    """
    InvoiceServiceBase schema class.

    Attributes:
        service_id (int): The ID of the service.
        quantity (int): The quantity of the service.
    """
    service_id: int
    quantity: int


class InvoiceServiceCreate(InvoiceServiceBase):
    """
    Create a new invoice service.

    Attributes:
        invoice_id (int): The ID of the invoice.
    """
    invoice_id: int


class InvoiceServiceUpdate(InvoiceServiceBase):
    """
    Update schema for the invoice service.

    Attributes:
        id (int): The ID of the invoice to be updated.
    """
    id: int


class InvoiceService(InvoiceServiceBase):
    """
    Represents an invoice service.

    Attributes:
        id (int): The ID of the invoice service.
        invoice_id (int): The ID of the invoice.
        service (Service): The service associated with the invoice.

    Config:
        from_attributes (bool): Indicates whether to populate the
            attributes from the input data.
    """

    id: int
    invoice_id: int
    service: Service

    class Config:
        from_attributes = True


class InvoiceBase(BaseModel):
    """
    Represents the base schema for an invoice.

    Attributes:
        invoice_number (str): The invoice number.
        date (Date): The date of the invoice.
        due_date (Optional[Date], optional): The due date of the invoice.
            Defaults to None.
        status (InvoiceStatus): The status of the invoice.
        client_id (int): The ID of the client associated with the invoice.
    """
    invoice_number: str
    date: Date
    due_date: Optional[Date] = None
    status: InvoiceStatus
    client_id: int


class InvoiceCreate(InvoiceBase):
    """
    Create schema for invoice.

    Attributes:
        services: List of InvoiceServiceCreate objects representing
            the services provided in the invoice.
        payments: List of PaymentCreate objects representing the
            payments made for the invoice.
    """
    services: List[InvoiceServiceCreate] = []
    payments: List[PaymentCreate] = []


class InvoiceUpdate(InvoiceBase):
    """
    Update schema for an invoice.

    Attributes:
        id (int): The ID of the invoice.
        services (List[InvoiceServiceCreate]): The list of services
            associated with the invoice.
        payments (List[PaymentCreate]): The list of payments made for
            the invoice.
    """
    id: int
    services: List[InvoiceServiceCreate] = []
    payments: List[PaymentCreate] = []


class Invoice(InvoiceBase):
    """
    Represents an invoice.

    Attributes:
        id (int): The ID of the invoice.
        services (List[InvoiceService]): The list of services included
            in the invoice.
        payments (List[Payment]): The list of payments made for the invoice.

    Computed Fields:
        total (float): The total amount of the invoice, calculated by
            summing the price of each service multiplied by its quantity.
        total_paid (float): The total amount paid for the invoice,
            calculated by summing the amount of each payment.
        total_due (float): The total amount due for the invoice,
            calculated by subtracting the total paid from the total amount.

    Config:
        from_attributes (bool): Indicates whether the invoice should be
            created from attributes.
    """
    id: int
    services: List[InvoiceService] = []
    payments: List[Payment] = []

    @computed_field
    def total(self) -> float:
        return sum([
            service.service.price * service.quantity
            for service in self.services
        ])

    @computed_field
    def total_paid(self) -> float:
        return sum([
            payment.amount
            for payment in self.payments
        ])

    @computed_field
    def total_due(self) -> float:
        return self.total - self.total_paid

    class Config:
        from_attributes = True
