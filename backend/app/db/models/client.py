# Path: backend/app/db/models/client.py

from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db import Base
from app.schemas.client import ClientStatus


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, nullable=True)
    facsimile = Column(String, nullable=True)
    contact_person = Column(String, nullable=True)
    company_name = Column(String, nullable=True)
    industry = Column(String, nullable=True)
    website = Column(String, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        onupdate=func.now(), nullable=True)
    status = Column(Enum(ClientStatus), nullable=False)
    created_by = Column(Integer, ForeignKey('users.id'))

    # Address fields for composite mapping
    address_line1 = Column(String, nullable=True)
    address_line2 = Column(String, nullable=True)
    address_city = Column(String, nullable=True)
    address_state = Column(String, nullable=True)
    address_postal_code = Column(String, nullable=True)
    address_country = Column(String, nullable=True)

    billing_address_line1 = Column(String, nullable=True)
    billing_address_line2 = Column(String, nullable=True)
    billing_address_city = Column(String, nullable=True)
    billing_address_state = Column(String, nullable=True)
    billing_address_postal_code = Column(String, nullable=True)
    billing_address_country = Column(String, nullable=True)

    invoices = relationship(
        "Invoice", cascade="all, delete-orphan", back_populates="client")
