# Path: backend/app/schemas/payment.py

from enum import Enum
from typing import Optional
from pydantic import BaseModel


class PaymentType(str, Enum):
    CASH = "Cash"
    CHECK = "Check"
    CARD = "Card"


class PaymentBase(BaseModel):
    type: PaymentType
    amount: float
    reference_number: str
    network: Optional[str] = None
    last_4: Optional[str] = None


class PaymentCreate(PaymentBase):
    pass


class Payment(PaymentBase):
    id: int

    class Config:
        from_attributes = True
