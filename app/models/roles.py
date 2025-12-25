
from __future__ import annotations
from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, DECIMAL, DATE
from sqlalchemy.orm import declarative_base, relationship,mapped_column,Mapped
from datetime import datetime,date
from .base import Base
if TYPE_CHECKING:
    from app.models.users import User

if TYPE_CHECKING:
    from .users import User

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    users: Mapped[List["User"]] = relationship(back_populates="role")  