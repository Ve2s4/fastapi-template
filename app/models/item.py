from sqlalchemy import Column, String, BigInteger

from app.database.db import Base
from app.models.base import BaseModel


# Item model, inherits from BaseModel
class Item(Base, BaseModel):
    __tablename__ = "item"

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(BigInteger, nullable=False)
