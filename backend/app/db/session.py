from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
"""
An instance of the create_engine function from the SQLAlchemy library.
"""

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
An instance of the sessionmaker class from the SQLAlchemy library.
"""
