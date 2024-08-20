import asyncio
from typing import Annotated

from asynctnt.exceptions import TarantoolDatabaseError
from fastapi import Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
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
    tasks = [
        conn.insert('tester', convert_to_tuple(key, value)
                    ) for key, value in data.get('data').items()
    ]
    try:
        await asyncio.gather(*tasks)
    except TarantoolDatabaseError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Такой ключ уже есть в базе'
        )
    return JSONResponse(content={'status': 'success'})


@router.post('/read')
async def read_batch(
    request: ReadRequest,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    data = request.model_dump()
    tasks = [conn.select('tester', [key]) for key in data['keys']]
    tasks = await asyncio.gather(*tasks)
    result = {'data': {}}
    for response in tasks:
        try:
            key = response.body[0][0]
        except IndexError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Объект с таким ключом отсутствует в базе'
            )
        result['data'][key] = [v for v in response.body[0].values()]
    return JSONResponse(content=result)
