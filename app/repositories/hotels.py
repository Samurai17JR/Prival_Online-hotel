from app.models.hotels import Hotel
from app.repositories.base import BaseRepository
from app.schemes.hotels import SHotelGet


class HotelsRepository(BaseRepository):
    model = Hotel
    schema = SHotelGet
    schema = SHotelGet

