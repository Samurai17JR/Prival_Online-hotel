from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.users import UserModel

class Review(Base):
    __tablename__ = 'reviews'

    review_id: Mapped[int] = mapped_column( primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), nullable=False)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.hotel_id'), nullable=False)
    rating: Mapped[int] = mapped_column( nullable=False)
    comment: Mapped[Text] = mapped_column(Text, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="reviews")
    hotel = relationship("Hotel", back_populates="reviews")