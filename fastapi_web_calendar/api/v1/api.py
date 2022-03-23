from fastapi import APIRouter

from .endpoints import event

api_router = APIRouter()
api_router.include_router(event.router, prefix="/events", tags=["events"])
