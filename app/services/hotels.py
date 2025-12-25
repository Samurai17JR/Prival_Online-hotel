from app.exceptions.base import ObjectAlreadyExistsError
from app.exceptions.roles import RoleAlreadyExistsError
from app.models.hotels import Hotel
from app.schemes.hotels import SHotelAdd, SHotelPatch
from app.services.base import BaseService


class HotelService(BaseService):

    async def create_hotel(self, hotel_data: SHotelAdd):
        hotel = Hotel(**hotel_data.model_dump())
        self.db.add(hotel)
        await self.db.flush()
        await self.db.commit()
        return {"status": "OK"}

    async def get_hotels(self, limit: int | None = None, offset: int | None = None):
        return await self.db.hotels.get_all(limit=limit, offset=offset)

    async def get_hotel_by_id(self, hotel_id: int):
        return await self.db.hotels.get_one_or_none(hotel_id=hotel_id)

    async def update_hotel(self, hotel_id: int, hotel_data: SHotelPatch):
        await self.db.hotels.edit(hotel_data, hotel_id=hotel_id)
        await self.db.commit()
        return await self.get_hotel_by_id(hotel_id)

    async def delete_hotel(self, hotel_id: int):
        await self.db.hotels.delete(hotel_id=hotel_id)
        return {"status": "OK"}