from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    hashed_password = Column(String)

    invoices = relationship("Invoice", back_populates="owner")
