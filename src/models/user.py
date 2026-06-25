from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.storage.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)  # 'employer' или 'applicant'
    created_at = Column(DateTime, server_default=func.now())

    # Связи (аналог relationship в Author)
    jobs = relationship("Job", back_populates="employer")
    responses = relationship("Response", back_populates="applicant")
