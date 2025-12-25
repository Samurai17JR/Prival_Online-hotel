
from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.api.dependencies import DBDep
from app.schemes.hotels import SHotelAdd, SHotelGet, SHotelPatch
from app.services.hotels import HotelService

router = APIRouter(prefix="/hotels", tags=["Отели"])


@router.get("", summary="Получить список всех отелей")
async def get_hotels(
    db: DBDep,
    limit: int | None = None,
    offset: int | None = None,
) -> list[SHotelGet]:
    return await HotelService(db).get_hotels(limit=limit, offset=offset)


@router.get("/{hotel_id}", summary="Получить информацию об отеле по ID")
async def get_hotel(hotel_id: int, db: DBDep) -> SHotelGet:
    hotel = await HotelService(db).get_hotel_by_id(hotel_id)
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel


@router.post("", summary="Создать новый отель")
async def create_hotel(hotel_data: SHotelAdd, db: DBDep) -> dict[str, str]:
    return await HotelService(db).create_hotel(hotel_data)


@router.put("/{hotel_id}", summary="Обновить данные отеля")
async def update_hotel(hotel_id: int, hotel_data: SHotelPatch, db: DBDep) -> SHotelGet:
    hotel = await HotelService(db).update_hotel(hotel_id, hotel_data)
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel


@router.delete("/{hotel_id}", summary="Удалить отель")
async def delete_hotel(hotel_id: int, db: DBDep) -> dict[str, str]:
    return await HotelService(db).delete_hotel(hotel_id)


# === НОВЫЕ РУЧКИ ===

@router.get("/search", summary="Поиск отелей по параметрам")
async def search_hotels(
    db: DBDep,
    city: Optional[str] = Query(None),
    country: Optional[str] = Query(None),
    rating_min: Optional[float] = Query(None),
    name: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=100),
) -> list[SHotelGet]:
    return await HotelService(db).search_hotels(
        city=city,
        country=country,
        rating_min=rating_min,
        name=name,
        limit=limit,
    )


@router.get("/top", summary="Топ отелей по рейтингу")
async def get_top_hotels(
    db: DBDep,
    limit: int = Query(5, ge=1, le=20)
) -> list[SHotelGet]:
    return await HotelService(db).get_top_hotels(limit=limit)


@router.get("/count", summary="Получить общее количество отелей")
async def get_hotels_count(db: DBDep) -> dict[str, int]:
    count = await HotelService(db).get_hotels_count()
    return {"total_hotels": count}


@router.get("/by-country/{country}", summary="Отели по стране")
async def get_hotels_by_country(country: str, db: DBDep) -> list[SHotelGet]:
    hotels = await HotelService(db).get_hotels_by_country(country)
    if not hotels:
        raise HTTPException(status_code=404, detail=f"Нет отелей в стране '{country}'")
    return hotels

