from fastapi import APIRouter

from src.controllers import products_controller as products
from src.controllers import users_controller as users

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(products.router, prefix="/products", tags=["Products"])
