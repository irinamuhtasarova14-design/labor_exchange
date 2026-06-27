from storage.sqlalchemy.client import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from datetime import datetime
from sqlalchemy import ForeignKey, String, Text, Boolean, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, comment="Идентификатор вакансии")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, comment="Идентификатор пользователя (работодателя)")
    title: Mapped[str] = mapped_column(String(255), nullable=False, comment="Название вакансии")
    description: Mapped[str] = mapped_column(Text, nullable=False, comment="Описание вакансии")
    salary_from: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True, comment="Зарплата от")
    salary_to: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True, comment="Зарплата до")
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, comment="Активна ли вакансия")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment="Дата создания")

    user: Mapped["User"] = relationship(back_populates="jobs") # noqa
    responses: Mapped[list["Response"]] = relationship(back_populates="job") # noqa