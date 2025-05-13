from fastapi import FastAPI,APIRouter
from .sets import router as sets_router

router = APIRouter()


router.include_router(sets_router, prefix='/sets', tags=["Sets"])
