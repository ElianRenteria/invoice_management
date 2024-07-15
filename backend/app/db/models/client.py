# Path: backend/app/db/models/client.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    created_by = Column(Integer, ForeignKey('users.id'))

    invoices = relationship(
        "Invoice", cascade="all, delete-orphan", back_populates="client")
