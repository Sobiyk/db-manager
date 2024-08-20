from fastapi.routing import APIRouter

from .endpoints.tarantool import router as tnt_router
from .endpoints.auth import router as auth_router

router = APIRouter()
router.include_router(tnt_router)
router.include_router(auth_router)
