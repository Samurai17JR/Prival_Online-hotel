from typing import List, Optional
from app.models.hotels import Hotel
from app.schemes.hotels import SHotelAdd, SHotelPatch, SHotelGet
from app.services.base import BaseService


class HotelService(BaseService):
    model = Hotel

    async def create_hotel(self, hotel_data: SHotelAdd):
        hotel = Hotel(**hotel_data.model_dump())
        self.db.add(hotel)
        await self.db.flush()
        await self.db.commit()
        return {"status": "OK"}

    async def get_hotels(self, limit: int | None = None, offset: int | None = None) -> List[SHotelGet]:
        hotels = await self.db.hotels.get_all(limit=limit, offset=offset)
        return [SHotelGet.model_validate(hotel) for hotel in hotels]

    async def get_hotel_by_id(self, hotel_id: int) -> Optional[SHotelGet]:
        hotel = await self.db.hotels.get_one_or_none(hotel_id=hotel_id)
        return SHotelGet.model_validate(hotel) if hotel else None

    async def update_hotel(self, hotel_id: int, hotel_data: SHotelPatch) -> Optional[SHotelGet]:
        await self.db.hotels.edit(hotel_data, hotel_id=hotel_id)
        await self.db.commit()
        return await self.get_hotel_by_id(hotel_id)

    async def delete_hotel(self, hotel_id: int):
        await self.db.hotels.delete(hotel_id=hotel_id)
        return {"status": "OK"}

    # === НОВЫЕ МЕТОДЫ ===

    async def search_hotels(
        self,
        city: Optional[str] = None,
        country: Optional[str] = None,
        rating_min: Optional[float] = None,
        name: Optional[str] = None,
        limit: int = 50,
    ) -> List[SHotelGet]:
        hotels = await self.db.hotels.search(city, country, rating_min, name, limit)
        return [SHotelGet.model_validate(hotel) for hotel in hotels]

    async def get_top_hotels(self, limit: int) -> List[SHotelGet]:
        hotels = await self.db.hotels.get_top(limit)
        return [SHotelGet.model_validate(hotel) for hotel in hotels]

    async def get_hotels_count(self) -> int:
        return await self.db.hotels.count()

    async def get_hotels_by_country(self, country: str) -> List[SHotelGet]:
        hotels = await self.db.hotels.get_by_country(country)
        return [SHotelGet.model_validate(hotel) for hotel in hotels]
   

