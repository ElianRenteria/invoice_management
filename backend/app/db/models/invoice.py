# Path: backend/app/db/models/invoice.py

from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base
from app.schemas.invoice import InvoiceStatus


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, index=True)
    date = Column(Date)
    due_date = Column(Date, nullable=True)
    status = Column(Enum(InvoiceStatus), default=InvoiceStatus.ESTIMATE)
    client_id = Column(Integer, ForeignKey('clients.id'))
    owner_id = Column(Integer, ForeignKey('users.id'))

    client = relationship(
        "Client", back_populates="invoices")
    services = relationship(
        "InvoiceService", cascade="all, delete-orphan", back_populates="invoice")
    payments = relationship(
        "Payment", back_populates="invoice")
    owner = relationship("User", back_populates="invoices")


class InvoiceService(Base):
    __tablename__ = 'invoice_services'

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    quantity = Column(Integer)

    invoice = relationship("Invoice", back_populates="services")
    service = relationship("Service", back_populates="invoice_services")
