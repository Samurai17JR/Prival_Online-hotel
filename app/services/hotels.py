from app.exceptions.base import ObjectAlreadyExistsError
from app.exceptions.roles import RoleAlreadyExistsError
from app.schemes.hotels import SHotelAdd
from app.services.base import BaseService


class HotelService(BaseService):

    async def create_hotel(self, hotel_data: SHotelAdd):
        
        hotel = await self.db.hotels.add(hotel_data)
        await self.db.commit()
        return hotel

    async def get_hotels(self):
        return await self.db.hotels.get_all()


   