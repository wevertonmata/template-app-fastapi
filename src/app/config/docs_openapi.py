import datetime
from fastapi import APIRouter, responses
from fastapi.openapi.utils import get_openapi
from app.config.configs import get_settings

TITLE: str = " tech-template-app-fastapi " # "template-app-python"
DESCRIPTION: str = "Insert your description"
VERSION: str = "1.0.0"
SQUAD_NAME: str =  " 87ba7ae1-46bd-d775-b077-2643bcfba03d "   # "squad-plataforma-ops"
BUILD_DATE: datetime = datetime.datetime.today().strftime("%d/%m/%y %H:%M:%S")

settings = get_settings()
redirect_to_docs = APIRouter()

def _get_servers():
    servers = []

    host = settings.environment
    if host != "localhost":
        namespace = TITLE.strip().replace(".", "-")
        url = f"https://{namespace}.com.br"
        servers = [{"url": url, "description": "HTTPS"}]
    return servers

def custom_openapi_factory(app):
    """Generate Custom OpenAPI Schema"""
    
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema  
        
        app.openapi_schema = get_openapi(
            title=TITLE,
            description=DESCRIPTION,
            version = "1.0.0",
            openapi_version = "3.0.3",
            contact={"name": SQUAD_NAME},
            servers=_get_servers(),
            license_info={"name": f"Version generation date {BUILD_DATE}"},
            routes=app.routes
        )
        
        # Habilita botao 'Authorize' para inserir JWT
        security_schemes = {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                    "description": "Token JWT gerado pelo M2M para consumir a aplicação",
                }
            }
        }
        if "components" not in app.openapi_schema:
            app.openapi_schema["components"] = security_schemes
        else:
            app.openapi_schema["components"].update(security_schemes)
        
        # Aplica a todos os endpoints
        app.openapi_schema["security"] = [{"bearerAuth": []}]
        return app.openapi_schema

    return custom_openapi

@redirect_to_docs.get("/", include_in_schema=False)
async def docs_redirect():
    """Redirect default path to docs"""
    
    return responses.RedirectResponse(url=settings.DOCS_ROUTE)
