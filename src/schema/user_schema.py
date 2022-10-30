from typing import Optional, Union

from pydantic import BaseModel


class UserBase(BaseModel):
    id: Union[int, None] = None
    name: str
    email: str
    phone: str


class CreateUser(UserBase):
    password: str

    class Config:
        orm_mode = True


class User(UserBase):
    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    id: Union[int, None] = None
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    phone: Optional[str]

    class Config:
        orm_mode = True
