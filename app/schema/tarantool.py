from typing import Any

from pydantic import BaseModel


class WriteRequest(BaseModel):
    data: dict[str, Any]


class ReadRequest(BaseModel):
    keys: list[str]


class LoginRequest(BaseModel):
    username: str
    password: str
