from sqlalchemy import delete
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schema import schema


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schema.Product):
        db_product = models.Product(
            name=product.name, available=product.available, details=product.details, price=product.price
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def list(self):
        products = self.db.query(models.Product).all()
        return products

    def get(self, product_id: int):
        product = self.db.query(models.Product).filter(models.Product.id == product_id).first()
        return product

    def destroy(self, product_id: int):
        product = delete(models.Product).where(models.Product.id == product_id)
        self.db.execute(product)
        self.db.commit()
