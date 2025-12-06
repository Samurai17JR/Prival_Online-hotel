from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, DECIMAL, DATE
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotels'

    hotel_id: Mapped[int] = mapped_column( primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column( nullable=False)
    address: Mapped[Text] = mapped_column( nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    rating: Mapped[DECIMAL] = mapped_column(DECIMAL(2, 1), nullable=True)
    description:Mapped[Text] = mapped_column( nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)

    rooms = relationship("Room", back_populates="hotel")
    reviews = relationship("Review", back_populates="hotel")
