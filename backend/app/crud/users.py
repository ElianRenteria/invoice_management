from sqlalchemy.orm import Session, joinedload
from app.db.models.users import Users as UsersModel
from app.schemas.signup import SignUpRequest, SignUpResponse
from app.db.models.invoice import Invoice as InvoiceModel, InvoiceService as InvoiceServiceModel


def create_user(db: Session, user: SignUpRequest):
    db_user = UsersModel(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user