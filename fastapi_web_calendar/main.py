from fastapi import FastAPI

from . import __version__, api


class settings:
    PROJECT_NAME = "FastAPI Web Calendar API"
    VERSION = __version__


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(api.v1.router, prefix="/api/v1")
