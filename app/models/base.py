import uuid
from datetime import datetime

from sqlalchemy import Column, String, BigInteger
from sqlalchemy.dialects.postgresql import UUID

# Abstract base model for all models, contains common fields and methods

class BaseModel:

    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, nullable=False, default=uuid.uuid4)
    created_at = Column(BigInteger, nullable=False, default=int(datetime.now().timestamp() * 1000))  # Unix timestamp (UTC, ms), int conversion is necessary, because it returns float
    updated_at = Column(BigInteger, nullable=False, default=int(datetime.now().timestamp() * 1000), onupdate=int(datetime.now().timestamp() * 1000))  # Unix timestamp (UTC, ms)

    @classmethod
    def create_item(cls, item, db):
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    @classmethod
    def get_item_by_id(cls, item_id, db):
        return db.query(cls).filter(cls.id == item_id).first()

    @classmethod
    def get_all_items(cls, db, skip=0, take=10):
        return db.query(cls).offset(skip).limit(take).all()