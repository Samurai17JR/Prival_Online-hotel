from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SHotelAdd(BaseModel):
    name: str
    address: str
    city: str
    country: str
    rating: Optional[float] = None
    description: Optional[str] = None


class SHotelGet(SHotelAdd):
    hotel_id: int
    created_at: datetime


class SHotelPatch(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    rating: Optional[float] = None
    description: Optional[str] = None