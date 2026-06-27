from datetime import datetime
from sqlalchemy import String, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from storage.sqlalchemy.client import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, comment="Идентификатор пользователя")
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, comment="Email адрес")
    name: Mapped[str] = mapped_column(String(255), nullable=False, comment="Имя пользователя")
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False, comment="Зашифрованный пароль")
    role: Mapped[str] = mapped_column(
        SQLAlchemyEnum('employer', 'applicant', name='user_roles'),
        nullable=False,
        comment="Роль пользователя"
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment="Дата создания")

    jobs: Mapped[list["Job"]] = relationship(back_populates="user", cascade="all, delete-orphan") # noqa
    responses: Mapped[list["Response"]] = relationship(back_populates="user", cascade="all, delete-orphan") # noqa