
from fastapi import APIRouter
from app.config.configs import get_settings
from app.log.logger import Logger

settings = get_settings()
logger = Logger(__name__)

api_v1 = APIRouter()

@api_v1.get("/hello")
def hello_world(name: str = "Your Name") -> dict:
    return {"message": "Hello World", "name": name}

@api_v1.get("/logs")
def logs() -> dict:
    logger.error("error")
    logger.info("information")
    return {"Message": "Logs enviados", "Ambiente": settings.environment}
