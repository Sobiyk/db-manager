from fastapi.routing import APIRouter

from app.core.db import conn

from pydantic import BaseModel, Field

router = APIRouter()


class WriteRequest(BaseModel):
    id: int = Field(None)
    fullname: str
    year: int


class ReadRequest(BaseModel):
    key: int


@router.post('/write')
async def write_batch(request: WriteRequest):
    data = dict(request)
    data['id'] = 3
    await conn.insert('users', [data['id'], data['fullname'], data['year']])
    return {'status': 'success'}


@router.post('/read')
async def read_batch(request: ReadRequest):
    data = dict(request)
    result = await conn.select('users', [data['key']])
    return {i: v for i, v in result.body[0].items()}
