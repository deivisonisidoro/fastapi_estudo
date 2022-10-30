from typing import Optional, Union

from pydantic import BaseModel
from src.schema.user_schema import User


class ProductBase(BaseModel):
    id: Union[int, None] = None
    name: str
    details: str
    price: float
    available: bool
    owner: Optional[User]


class Product(ProductBase):
    class Config:
        orm_mode = True


class UpdateProduct(BaseModel):
    id: Union[int, None] = None
    name: Optional[str]
    details: Optional[str]
    price: Optional[float]
    available: Optional[bool]

    class Config:
        orm_mode = True
