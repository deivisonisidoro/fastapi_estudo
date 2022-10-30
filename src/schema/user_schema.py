from typing import Optional, Union

from pydantic import BaseModel


class User(BaseModel):
    id: Union[int, None] = None
    name: str
    email: str
    password: str
    phone: str


class UpdateUser(BaseModel):
    id: Union[int, None] = None
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    phone: Optional[str]

    class Config:
        orm_mode = True
