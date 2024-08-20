import asyncio
from typing import Annotated
from fastapi import Depends
from fastapi.routing import APIRouter

from app.api.utils import convert_to_tuple
from app.core.db import conn

from app.core.user import User, get_current_active_user
from app.schema.tarantool import ReadRequest, WriteRequest

router = APIRouter()


@router.post('/write')
async def write_batch(
    request: WriteRequest,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    data = request.model_dump()
    tasks = []
    for key, value in data.get('data').items():
        obj_in = convert_to_tuple(key, value)
        tasks.append(conn.insert('tester', obj_in))

    await asyncio.gather(*tasks)
    return {'status': 'success'}


@router.post('/read')
async def read_batch(
    request: ReadRequest,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    data = request.model_dump()
    tasks = [conn.select('tester', [int(key)]) for key in data['keys']]
    tasks = await asyncio.gather(*tasks)
    result = {'data': {}}
    for response in tasks:
        key = response.body[0][0]
        result['data'][key] = [v for v in response.body[0].values()]
    return result
