from fastapi import FastAPI

from app.controllers.tablero_controller import router as tablero_router
from app.core.config import settings
from app.core.database import init_db

app = FastAPI(title=settings.app_name)


@app.on_event("startup")
def on_startup() -> None:
    """Initialize database metadata when the service boots."""

    init_db()


@app.get("/health", tags=["Health"])
def health_check() -> dict:
    return {"status": "ok"}


app.include_router(tablero_router)
