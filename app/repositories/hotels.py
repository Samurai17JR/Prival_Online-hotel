from typing import Optional
from sqlalchemy import select, func
from app.models.hotels import Hotel
from app.repositories.base import BaseRepository
from app.schemes.hotels import SHotelGet


class HotelsRepository(BaseRepository):
    model = Hotel
    schema = SHotelGet

    async def search(
        self,
        city: Optional[str] = None,
        country: Optional[str] = None,
        rating_min: Optional[float] = None,
        name: Optional[str] = None,
        limit: int = 50,
    ) -> list[Hotel]:
        query = select(self.model)
        if city:
            query = query.where(self.model.city.ilike(f"%{city}%"))
        if country:
            query = query.where(self.model.country.ilike(f"%{country}%"))
        if rating_min is not None:
            query = query.where(self.model.rating >= rating_min)
        if name:
            query = query.where(self.model.name.ilike(f"%{name}%"))
        query = query.limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_top(self, limit: int) -> list[Hotel]:
        query = select(self.model).order_by(self.model.rating.desc()).limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def count(self) -> int:
        query = select(func.count()).select_from(self.model)
        result = await self.session.execute(query)
        return result.scalar_one()

    async def get_by_country(self, country: str) -> list[Hotel]:
        query = select(self.model).where(self.model.country.ilike(f"%{country}%"))
        result = await self.session.execute(query)
        return list(result.scalars().all())
