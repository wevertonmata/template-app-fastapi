from fastapi import APIRouter

from app.log.logger import Logger
logger = Logger(__name__)


api_v1 = APIRouter()


@api_v1.get("/hello")
async def hello_world(name = "your name"):
    return {"message": "Hello World", "name": name}

@api_v1.get("/logs")
async def logs():
    logger.warning("WARN")
    logger.info("INFO")
    logger.error("ERROR")
    logger.debug("debug")
    
    return {"message": "Logs enviados"}

