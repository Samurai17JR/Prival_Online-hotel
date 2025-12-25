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


