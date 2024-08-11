# Path: backend/app/schemas/payment.py

from enum import Enum
from typing import Optional
from pydantic import BaseModel


class PaymentType(str, Enum):
    """
    Enum class representing different types of payment.

    Attributes:
        CASH (str): Represents cash payment.
        CHECK (str): Represents check payment.
        CARD (str): Represents card payment.
    """
    CASH = "Cash"
    CHECK = "Check"
    CARD = "Card"


class PaymentBase(BaseModel):
    """
    PaymentBase schema represents the base structure for a payment.

    Attributes:
        type (PaymentType): The type of payment.
        amount (float): The amount of the payment.
        reference_number (str): The reference number of the payment.
        network (Optional[str], optional): The network used for the payment. Defaults to None.
        last_4 (Optional[str], optional): The last 4 digits of the payment method. Defaults to None.
    """
    type: PaymentType
    amount: float
    reference_number: str
    network: Optional[str] = None
    last_4: Optional[str] = None


class PaymentCreate(PaymentBase):
    """
    Create a new payment.

    Attributes:
        All attributes inherited from PaymentBase class.
    """
    pass


class Payment(PaymentBase):
    """
    Payment schema.

    Attributes:
        id (int): The ID of the payment.
    """
    id: int

    class Config:
        from_attributes = True
