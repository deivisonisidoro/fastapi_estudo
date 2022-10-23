from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.product import ProductRepository
from src.schema import product_schema

router = APIRouter()


@router.post("/")
def create_product(product: product_schema.Product, db: Session = Depends(get_db)):
    product_created = ProductRepository(db).create(product)
    return product_created


@router.get("/")
def list_products(db: Session = Depends(get_db)):
    products = ProductRepository(db).list()
    return products


@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = ProductRepository(db=db).get(product_id)
    return product


@router.patch("/{product_id}")
def update_product(product_id: int, product: product_schema.Product, db: Session = Depends(get_db)):
    product = ProductRepository(db=db).update(product_id, product)
    return product


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    ProductRepository(db=db).destroy(product_id=product_id)
    return {"msg": "Removido com sucesso"}
