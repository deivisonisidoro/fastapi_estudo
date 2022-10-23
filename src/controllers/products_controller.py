from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.product import ProductRepository
from src.schema import schema

router = APIRouter()


@router.post("/")
def create_product(product: schema.Product, db: Session = Depends(get_db)):
    product_created = ProductRepository(db=db).create(product=product)
    return product_created


@router.get("/")
def list_products(db: Session = Depends(get_db)):
    products = ProductRepository(db=db).list()
    return products


@router.get("//{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = ProductRepository(db=db).get(product_id=product_id)
    return product


@router.delete("//{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    ProductRepository(db=db).destroy(product_id=product_id)
    return {"msg": "removido com sucesso"}
