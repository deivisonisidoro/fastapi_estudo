from fastapi import APIRouter

from src.controllers import products_controller as products

router = APIRouter()

router.include_router(products.router, prefix="/products", tags=["Products"])
