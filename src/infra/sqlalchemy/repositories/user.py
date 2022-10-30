from sqlalchemy import delete
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schema import user_schema


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: user_schema.CreateUser):
        db_user = models.User(
            name=user.name,
            email=user.email,
            phone=user.phone,
            password=user.password,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def list(self):
        db_users = self.db.query(models.User).all()
        return db_users

    def get_by_id(self, user_id: int):
        db_user = (
            self.db.query(
                models.User,
            )
            .filter(
                models.User.id == user_id,
            )
            .first()
        )
        return db_user

    def get_by_email(self, email: str) -> models.User:
        return self.db.query(models.User).filter(models.User.email == email).first()

    def update(self, user_id: int, user: user_schema.UpdateUser):
        db_user = self.db.get(models.User, user_id)
        user_data = user.dict(exclude_unset=True)
        for key, value in user_data.items():
            setattr(db_user, key, value)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def destroy(self, user_id: int):
        self.db.execute(
            delete(models.User,).where(
                models.User.id == user_id,
            )
        )
        self.db.commit()
