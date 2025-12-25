
from fastapi import APIRouter, HTTPException

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
from fastapi import APIRouter
from fastapi import HTTPException

from app.api.dependencies import DBDep, IsAdminDep
from app.exceptions.roles import (
    RoleAlreadyExistsError,
    RoleAlreadyExistsHTTPError,
    RoleNotFoundError,
    RoleNotFoundHTTPError,
)
from app.schemes.hotels import SHotelAdd, SHotelGet
from app.schemes.roles import SRoleAdd, SRoleGet
from app.schemes.relations_users_roles import SRoleGetWithRels
from app.services.hotels import HotelService
from app.services.roles import RoleService

router = APIRouter(prefix="", tags=["Управление отелями"])


@router.post("/hotels", summary="Создание новой роли")
async def create_new_hotel(
    hotel_data: SHotelAdd,
    db: DBDep,
) -> dict[str, str]:
    
    hotels = await HotelService(db).create_hotel(hotel_data)
    
    if hotels is None:
        raise HTTPException(status_code=404)
    
    return {"status": "OK"}


@router.get("/hotels", summary="Получение списка ролей")
async def get_all_roles(
    db: DBDep,
) -> list[SHotelGet] | None:
    return await HotelService(db).get_hotels()



