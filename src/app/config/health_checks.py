from fastapi import APIRouter

from ..schemas.models import HealthSchema

health_checks = APIRouter()

@health_checks.get("/liveness", tags=["Health"], include_in_schema=False)
async def liveness_status():
    """Check API health.

    Returns:
        dict: dict with api version and api status
    """
    return "Liveness check completed"


@health_checks.get("/ready", tags=["Health"], include_in_schema=False)
async def ready_status():
    """Check API health.

    Returns:
        dict: dict with api version and api status
    """
    return "ready check completed"

@health_checks.get("/health", tags=["Health"], response_model=HealthSchema, include_in_schema=False)
async def health_status():
    """Check API health.

    Returns:
        dict: dict with api version and api status
    """
    return HealthSchema(api_up=True, api_version="v1")


