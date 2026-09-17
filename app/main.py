"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.orders import router as orders_router
from app.api.users import router as users_router

app = FastAPI(title="RepoMind Fixture API")
app.include_router(health_router)
app.include_router(users_router)
app.include_router(orders_router)
