from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.api import api_router
from app.db.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, Welcome to the API of Nexus.ai!"}
