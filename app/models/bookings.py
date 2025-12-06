from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .users import User
    from .rooms import Room

from datetime import  date,datetime
from sqlalchemy import String, DECIMAL, ForeignKey, DateTime, DATE
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Booking(Base):
    __tablename__ = 'bookings'

    booking_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), nullable=False)
    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.room_id'), nullable=False)
    check_in_date: Mapped[date] = mapped_column(DATE,nullable=False)
    check_out_date: Mapped[date] = mapped_column(DATE,nullable=False)
    total_price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="bookings")
    room: Mapped["Room"] = relationship(back_populates="bookings")