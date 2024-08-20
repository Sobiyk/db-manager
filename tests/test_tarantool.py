import pytest
from fastapi import status
from tests.conftest import AsyncClient


@pytest.mark.asyncio
async def test_write_batch(ac: AsyncClient):
    response = await ac.post(
        '/api/write',
        headers={'Authorization': 'Bearer admin'},
        json={
            'data': {
                '1': 'Hello',
                '2': 'World'
            }
        })

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {'status': 'success'}

    response = await ac.post(
        '/api/write',
        headers={'Authorization': 'Bearer wrong'},
        json={
            'data': {
                '1': 'Hello',
                '2': 'World'
            }
        })

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = await ac.post(
        '/api/write',
        headers={'Authorization': 'Bearer admin'},
        json={
            'data': {
                '1': 'Hello',
                '2': 'World'
            }
        })

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response = await ac.post(
        '/api/write',
        headers={'Authorization': 'Bearer admin'},
        json={
            'wrong': {
                'fields': 'error'
            }
        })

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_read_batch(ac: AsyncClient):
    response = await ac.post(
        '/api/read',
        headers={'Authorization': 'Bearer admin'},
        json={'keys': ['1']})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'data': {'1': [1, 'test']}}

    response = await ac.post(
        '/api/read',
        headers={'Authorization': 'Bearer admin'},
        json={'keys': ['111']})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        'detail': 'Объект с таким ключом отсутствует в базе'
    }

    response = await ac.post(
        '/api/read',
        headers={'Authorization': 'Bearer admin'},
        json={'cheap': 'tomatoes'})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
