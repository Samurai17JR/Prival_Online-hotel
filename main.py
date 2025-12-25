import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.sample import router as sample_router
from app.api.auth import router as auth_router
from app.api.roles import router as role_router
from app.api.hotels import router as hotel_router
from app.api.query_improvement import router as query_router
from app.database.database import engine, Base
from fastapi.responses import FileResponse


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(title="individual_project_template", version="0.0.1")

app.mount("/static", StaticFiles(directory="app/static"), "static")
from fastapi.responses import FileResponse

@app.get("/")
async def index():
    return FileResponse("templates/index.html")
@app.get("/catalog")
async def catalog():
    return FileResponse("templates/catalog.html")
app.include_router(sample_router)
app.include_router(auth_router)
app.include_router(role_router)
app.include_router(query_router)
app.include_router(hotel_router)

if __name__ == "__main__":
    asyncio.run(init_db())
    uvicorn.run(app=app)

    