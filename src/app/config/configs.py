import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

ENV_PATH = ".env"
env_variables = os.environ.keys()
if not "ENVIRONMENT" in env_variables:
    if not os.path.exists(".env"):
        ENV_PATH = "src\.env"    
    load_dotenv(dotenv_path=ENV_PATH) # Carregar .env

def get_key_vault(secret_name: str):
    """
    Retorna o valor de uma chave do Azure KeyVault

    Obs: Rodando localmente os valores são buscados
    no arquivo .env
    """
    return os.getenv(secret_name)
    

class Settings(BaseSettings):
    """Configurações gerais usadas na aplicação"""

    # Default Settings
    model_config = SettingsConfigDict(case_sensitive=False, )
    is_debug: bool = False
    is_local: bool = os.getenv("ENVIROMENT") is None
    environment: str =  os.getenv("ENVIROMENT") or "localhost"
    port: int = 7000 if is_local else 5000
    
    # Openapi
    API_VERSION: str = '/v1'
    DOCS_ROUTE: str = "/swagger/index.html"
    OPENAPI_ROUTE: str = f"/swagger{API_VERSION}/swagger.json"
    
    
@lru_cache
def get_settings():
    """
    Cria as configurações da aplicação como singleton

    Obs: Os valores default da classe Settings são
    sobrescritos pelos valores do arquivo .env ou
    por variáveis ambiente pré-existentes.
    """
    
    return Settings()
