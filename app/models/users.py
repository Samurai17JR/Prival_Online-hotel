from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.roles import RoleModel

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column( primary_key=True, autoincrement=True)
    email:Mapped[str] =  mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    

    bookings = relationship("Booking", back_populates="user")
    reviews = relationship("Review", back_populates="user")

