from fastapi import APIRouter

from app.schemes.query_improvement import SQueryImproveRequest, SQueryImproveResponse
from app.services.query_improvement import QueryImprovementService

router = APIRouter(prefix="/query", tags=["Улучшение запросов"])

@router.post("/improve", summary="Улучшение поискового запроса")
async def improve_query(query_data: SQueryImproveRequest) -> SQueryImproveResponse:
    improved_query = QueryImprovementService.improve_query(query_data.query)
    return SQueryImproveResponse(improved_query=improved_query)