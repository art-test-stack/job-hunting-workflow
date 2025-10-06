from fastapi import APIRouter
from app.api.routes import user #, public_routes

router = APIRouter()
router.include_router(user.router)
# router.include_router(public_routes.router)
