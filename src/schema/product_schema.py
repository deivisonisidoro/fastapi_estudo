from typing import Union

from pydantic import BaseModel


class User(BaseModel):
    id: Union[int, None] = None
    name: str
    email: str
    password: str
    phone: str

    class Config:
        orm_mode = True


class Product(BaseModel):
    id: Union[int, None] = None
    name: str
    details: str
    price: float
    available: bool

    class Config:
        orm_mode = True
