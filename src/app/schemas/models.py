from pydantic import BaseModel

from enum import Enum
from typing import Optional


"""Models
URL: https://fastapi.tiangolo.com/tutorial/response-model/

Você pode declarar o tipo usado para a resposta anotando o tipo de retorno da função de operação do caminho.

"""

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
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"