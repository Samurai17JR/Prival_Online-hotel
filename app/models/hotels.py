from __future__ import annotations  

from typing import List
from sqlalchemy import String, Text, DECIMAL, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.database.database import Base



class Hotel(Base):
    __tablename__ = 'hotels'

    hotel_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)  
    address: Mapped[str] = mapped_column(Text, nullable=False)      
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    rating: Mapped[float | None] = mapped_column(DECIMAL(2, 1), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
   
    rooms: Mapped[List["Room"]] = relationship(back_populates="hotel")
    reviews: Mapped[List["Review"]] = relationship(back_populates="hotel")

    # rooms: Mapped[List["Room"]] = relationship(back_populates="hotel")
    # reviews: Mapped[List["Review"]] = relationship(back_populates="hotel")

