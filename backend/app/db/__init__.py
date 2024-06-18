# Ensure Base is imported before any models to avoid circular imports
from app.db.base import Base

# Import all models here to ensure they are registered in the correct order
from app.db.models.service import Service  # noqa
from app.db.models.invoice import Invoice, InvoiceService  # noqa
from app.db.models.client import Client  # noqa
from app.db.models.payment import Payment  # noqa
from app.db.models.user import User  # noqa


def init_db():
    from app.db.session import engine
    Base.metadata.create_all(bind=engine)
