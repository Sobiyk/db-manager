from fastapi.routing import APIRouter

from app.core.db import conn

from app.schema.tarantool import LoginRequest, ReadRequest, WriteRequest

router = APIRouter()


@router.post('/login')
async def login(request: LoginRequest):
    data = request.model_dump()
    pass


@router.post('/write')
async def write_batch(request: WriteRequest):
    data = request.model_dump()
    for key, value in data.get('data').items():
        value['id'] = int(key)
        await conn.insert(
            'users',
            [
                value['id'],
                value['fullname'],
                value['year']
            ]
        )
    return {'status': 'success'}


@router.post('/read')
async def read_batch(request: ReadRequest):
    data = request.model_dump()
    result = {}
    for key in data['keys']:
        obj = await conn.select('users', [key])
        result[key] = {i: v for i, v in obj.body[0].items()}
    return result
