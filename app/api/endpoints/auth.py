from typing import Annotated

from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from app.core.user import (
    fake_users_db,
    fake_hash_password,
    UserInDB,
)

router = APIRouter()


@router.post('/login')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=400,
            detail='Неверное имя пользователя или пароль'
        )
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400,
            detail='Неверное имя пользователя или пароль')

    return {'access_token': user.username, 'token_type': 'bearer'}
