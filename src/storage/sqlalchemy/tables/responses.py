from storage.sqlalchemy.client import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from sqlalchemy import ForeignKey, Text, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

class Response(Base):
    __tablename__ = "responses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, comment="Идентификатор отклика")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, comment="Идентификатор пользователя (соискателя)")
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"), nullable=False, comment="Идентификатор вакансии")
    message: Mapped[str | None] = mapped_column(Text, nullable=True, comment="Сопроводительное письмо")
    status: Mapped[str] = mapped_column(
        SQLAlchemyEnum('pending', 'accepted', 'rejected', name='response_status'),
        nullable=False,
        default='pending',
        comment="Статус отклика"
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment="Дата создания")
    user: Mapped["User"] = relationship(back_populates="responses") # noqa
    job: Mapped["Job"] = relationship(back_populates="responses") # noqa
