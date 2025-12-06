from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, DECIMAL, DATE
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Booking(Base):
    __tablename__ = 'bookings'

    booking_id:Mapped [int] = mapped_column( primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column( ForeignKey('users.user_id'), nullable=False)
    room_id: Mapped[int] = mapped_column( ForeignKey('rooms.room_id'), nullable=False)
    check_in_date: Mapped[DATE] = mapped_column( nullable=False)
    check_out_date: Mapped[DATE] = mapped_column(DATE, nullable=False)
    total_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    created_at: Mapped[DateTime] = mapped_column( default=datetime.utcnow)

    user = relationship("User", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")