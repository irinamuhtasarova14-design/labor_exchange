from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.storage.db import Base


class Response(Base):
    __tablename__ = 'responses'
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message = Column(Text, nullable=True)
    status = Column(String(20), default='pending')  # pending, accepted, rejected
    created_at = Column(DateTime, server_default=func.now())

    job = relationship("Job", back_populates="responses")
    applicant = relationship("User", back_populates="responses")
