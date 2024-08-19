from pydantic import BaseModel


class Object(BaseModel):
    fullname: str
    year: int


class WriteRequest(BaseModel):
    data: dict[str, Object]


class ReadRequest(BaseModel):
    keys: list[int]


class LoginRequest(BaseModel):
    username: str
    password: str
