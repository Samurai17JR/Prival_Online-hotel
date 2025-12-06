from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, DECIMAL, DATE
from sqlalchemy.orm import declarative_base, relationship,mapped_column,Mapped
from datetime import datetime,date
from .base import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    users: Mapped[list["UserModel"]] = relationship(back_populates="role")
