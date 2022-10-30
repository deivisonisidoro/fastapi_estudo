from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user import UserRepository
from src.schema import user_schema

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=user_schema.User)
def create_user(user: user_schema.User, db: Session = Depends(get_db)):
    user_created = UserRepository(db).create(user)
    return user_created


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[user_schema.User])
def list_users(db: Session = Depends(get_db)):
    users = UserRepository(db).list()
    return users


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=user_schema.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserRepository(db=db).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@router.patch("/{user_id}", status_code=status.HTTP_200_OK, response_model=user_schema.User)
def update_user(user_id: int, user: user_schema.User, db: Session = Depends(get_db)):
    db_user = UserRepository(db=db).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    user = UserRepository(db=db).update(user_id, user)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserRepository(db=db).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    UserRepository(db=db).destroy(user_id=user_id)
    return {"msg": "Removido com sucesso"}
