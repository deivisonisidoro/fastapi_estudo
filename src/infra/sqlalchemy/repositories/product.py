from sqlalchemy import delete
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schema import product_schema


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: product_schema.Product):
        db_product = models.Product(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def list(self):
        db_products = self.db.query(models.Product).all()
        return db_products

    def get(self, product_id: int):
        db_product = (
            self.db.query(
                models.Product,
            )
            .filter(
                models.Product.id == product_id,
            )
            .first()
        )
        return db_product

    def update(self, product_id: int, product: product_schema.Product):
        db_product = self.db.get(models.Product, product_id)
        product_data = product.dict(exclude_unset=True)
        for key, value in product_data.items():
            setattr(db_product, key, value)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def destroy(self, product_id: int):
        self.db.execute(
            delete(models.Product,).where(
                models.Product.id == product_id,
            )
        )
        self.db.commit()
