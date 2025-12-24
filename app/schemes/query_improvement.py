from pydantic import BaseModel

class SQueryImproveRequest(BaseModel):
    query: str

class SQueryImproveResponse(BaseModel):
    improved_query: str