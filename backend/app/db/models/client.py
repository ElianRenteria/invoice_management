# Path: backend/app/db/models/client.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    invoices = relationship("Invoice", back_populates="client")
