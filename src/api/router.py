from fastapi import APIRouter
from api import meta, status, fruits, inference

router = APIRouter(prefix='/api/v1')

router.include_router(meta.router)
router.include_router(status.router)
router.include_router(fruits.router)
router.include_router(inference.router)