from typing import Union

from pydantic import BaseModel


class Product(BaseModel):
    id: Union[int, None] = None
    name: str
    details: str
    price: float
    available: bool

    class Config:
        orm_mode = True
