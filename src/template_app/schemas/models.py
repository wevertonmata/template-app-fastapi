from typing import Optional
from pydantic import BaseModel, Field


class HealthSchema(BaseModel):
    """Health Schema."""

    api_up: bool
    api_version: str


class ResponseSchema(BaseModel):
    """Response Schema."""

    entity: str
    exists: bool
    data: dict