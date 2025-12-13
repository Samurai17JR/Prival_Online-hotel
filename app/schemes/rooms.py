from pydantic import BaseModel
from typing import Optional


class SRoomAdd(BaseModel):
    hotel_id: int
    room_type: str
    price_per_night: float
    max_guests: int
    is_available: Optional[bool] = True


class SRoomGet(SRoomAdd):
    room_id: int


class SRoomPatch(BaseModel):
    hotel_id: Optional[int] = None
    room_type: Optional[str] = None
    price_per_night: Optional[float] = None
    max_guests: Optional[int] = None
    is_available: Optional[bool] = None