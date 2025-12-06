from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, DECIMAL, DATE
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class Room(Base):
    __tablename__ = 'rooms'

    room_id: Mapped[int] = mapped_column( primary_key=True, autoincrement=True)
    hotel_id: Mapped[int] = mapped_column( ForeignKey('hotels.hotel_id'), nullable=False)
    room_type: Mapped[str] = mapped_column(String(100), nullable=False)
    price_per_night:Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), nullable=False)
    max_guests: Mapped[int] = mapped_column( nullable=False)
    is_available: Mapped[Boolean] = mapped_column(Boolean, default=True)

    hotel = relationship("Hotel", back_populates="rooms")
    bookings = relationship("Booking", back_populates="room")