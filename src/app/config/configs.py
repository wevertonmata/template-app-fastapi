from fastapi import APIRouter, responses
from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """  

    class Config:
        case_sensitive = True
        
settings = Settings()
