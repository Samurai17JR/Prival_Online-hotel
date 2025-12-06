
from __future__ import annotations  # ← обязательно для строковых ссылок

from typing import List
from sqlalchemy import String, Text, DECIMAL, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Room(Base):
    __tablename__ = 'rooms'

    room_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.hotel_id'), nullable=False)
    room_type: Mapped[str] = mapped_column(String(100), nullable=False)
    price_per_night: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    max_guests: Mapped[int] = mapped_column(Integer, nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)

    hotel: Mapped["Hotel"] = relationship(back_populates="rooms")
    bookings: Mapped[List["Booking"]] = relationship(back_populates="room")