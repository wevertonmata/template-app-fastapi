import logging

from fastapi import APIRouter

from ..schemas.models import HealthSchema

health_checks = APIRouter()
hc_kwargs = {"tags": ["Health"], "include_in_schema": False}


@health_checks.get("/liveness", **hc_kwargs)
async def liveness_status():
    """Check API liveness"""
    return "Liveness check completed"


@health_checks.get("/ready", **hc_kwargs)
async def ready_status():
    """Check API readyness"""
    return "ready check completed"


@health_checks.get("/health", response_model=HealthSchema, **hc_kwargs)
async def health_status():
    """Check API health"""
    return HealthSchema(api_up=True, api_version="v1")


class HealthCheckFilter(logging.Filter):
    """Log Filter for health checks"""

    blacklist = [route.path for route in health_checks.routes]

    def filter(self, record: logging.LogRecord):
        """Return False to remove from log"""
        if len(record.args) < 5:
            return True

        method = record.args[1]
        route = record.args[2]
        status = record.args[4]
        return (method != "GET") or (status != 200) or (route not in self.blacklist)


uvicorn_logger = logging.getLogger("uvicorn.access")
uvicorn_logger.addFilter(HealthCheckFilter())