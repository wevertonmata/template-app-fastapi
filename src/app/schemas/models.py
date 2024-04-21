# https://fastapi.tiangolo.com/tutorial/response-model/
from enum import Enum
from pydantic import BaseModel
class HealthSchema(BaseModel):
    """Health Schema."""

    api_up: bool
    api_version: str

class ResponseSchema(BaseModel):
    """Response Schema."""
    entity: str
    exists: bool
    data: dict
    
class ModelName(str, Enum):
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"