from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infra.providers.hash_provider import verify_password
from src.infra.providers.token_provider import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user import UserRepository
from src.schema import auth_schema

router = APIRouter()


@router.post("/token", status_code=status.HTTP_200_OK, response_model=auth_schema.Token)
def login(login_data: auth_schema.LoginData, db: Session = Depends(get_db)):
    email = login_data.email
    password = login_data.password

    db_user = UserRepository(db=db).get_by_email(email)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha estão incorreta",
            headers={"WWW-Authenticate": "Bearer"},
        )

    password_valid = verify_password(password, db_user.password)

    if not password_valid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email ou senha estão incorreta")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
