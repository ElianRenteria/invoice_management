# Path: backend/app/db/models/payment_type.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db import Base

from app.schemas.payment import PaymentType


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    type = Column(Enum(PaymentType))
    amount = Column(Float)
    reference_number = Column(String)

    # Optional card details
    network = Column(String, nullable=True)
    last_4 = Column(String, nullable=True)

    invoice = relationship("Invoice", back_populates="payments")
