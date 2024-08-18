from fastapi.routing import APIRouter

from .tarantool import router as r

router = APIRouter()
router.include_router(r)
