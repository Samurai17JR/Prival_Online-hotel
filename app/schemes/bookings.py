from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class SBookingAdd(BaseModel):
    user_id: int
    room_id: int
    check_in_date: date
    check_out_date: date
    total_price: float
    status: Optional[str] = "pending"


class SBookingGet(SBookingAdd):
    booking_id: int
    created_at: datetime


class SBookingPatch(BaseModel):
    user_id: Optional[int] = None
    room_id: Optional[int] = None
    check_in_date: Optional[date] = None
    check_out_date: Optional[date] = None
    total_price: Optional[float] = None
    status: Optional[str] = None