from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base

class User(Base):
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    created_date = Column(DateTime, default=func.now(), nullable=False)
    card_id = Column(String, unique=True, index=True)