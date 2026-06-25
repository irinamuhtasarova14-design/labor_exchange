from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.storage.db import Base

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    salary_from = Column(Numeric(10, 2), nullable=True)
    salary_to = Column(Numeric(10, 2), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

    employer = relationship("User", back_populates="jobs")
    responses = relationship("Response", back_populates="job")
