# Path: backend/app/db/models/client.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)
