from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SReviewAdd(BaseModel):
    user_id: int
    hotel_id: int
    rating: int
    comment: Optional[str] = None


class SReviewGet(SReviewAdd):
    review_id: int
    created_at: datetime


class SReviewPatch(BaseModel):
    user_id: Optional[int] = None
    hotel_id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None