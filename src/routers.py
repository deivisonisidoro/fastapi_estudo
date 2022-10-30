from fastapi import APIRouter

from src.controllers import auth_controller as auth
from src.controllers import products_controller as products
from src.controllers import users_controller as users

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(products.router, prefix="/products", tags=["Products"])
