from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers import router as tnt_router
from app.core.db import conn


async def get_tnt_connection():
    await conn.connect()


async def close_tnt_connection():
    await conn.disconnect()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await get_tnt_connection()
    yield
    await close_tnt_connection()


app = FastAPI(title='test', lifespan=lifespan)
app.include_router(tnt_router, prefix='/api')
