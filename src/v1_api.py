import logging
from fastapi import FastAPI, Response, status
from template_app.schemas.models import (
    HealthSchema,
    ResponseSchema,
)

v1_api = FastAPI()

@v1_api.get("/liveness", tags=["Health"])
async def liveness_status():
    """Check API health.

    Returns:
        dict: dict with api version and api status
    """
    return "Liveness check completed"


@v1_api.get("/readiness", tags=["Health"])
async def readiness_status():
    """Check API health.

    Returns:
        dict: dict with api version and api status
    """
    return "Readiness check completed"


@v1_api.get("/health", tags=["Health"], response_model=HealthSchema)
async def health_status():
    """Check API health.

    Returns:
        dict: dict with api version and api status
    """
    return HealthSchema(api_up=True, api_version="v1")
