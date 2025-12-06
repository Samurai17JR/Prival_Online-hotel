from __future__ import annotations 

from datetime import datetime,date
from sqlalchemy import Text, ForeignKey, Integer,DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Review(Base):
    __tablename__ = 'reviews'

    review_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), nullable=False)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.hotel_id'), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)  
    comment: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="reviews")
    hotel: Mapped["Hotel"] = relationship(back_populates="reviews")