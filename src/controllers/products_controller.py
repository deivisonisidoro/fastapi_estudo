from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.product import ProductRepository
from src.schema import product_schema

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK, response_model=product_schema.Product)
def create_product(product: product_schema.Product, db: Session = Depends(get_db)):
    product_created = ProductRepository(db).create(product)
    return product_created


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[product_schema.Product])
def list_products(db: Session = Depends(get_db)):
    products = ProductRepository(db).list()
    return products


@router.get("/{product_id}", status_code=status.HTTP_200_OK, response_model=product_schema.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = ProductRepository(db=db).get(product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_product


@router.patch("/{product_id}", status_code=status.HTTP_200_OK, response_model=product_schema.Product)
def update_product(product_id: int, product: product_schema.UpdateProduct, db: Session = Depends(get_db)):
    db_product = ProductRepository(db=db).get(product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    product = ProductRepository(db=db).update(product_id, product)
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = ProductRepository(db=db).get(product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    ProductRepository(db=db).destroy(product_id=product_id)
    return {"msg": "Removido com sucesso"}
