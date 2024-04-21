from fastapi import FastAPI
from app.config.health_checks import health_checks
from app.config.docs_openapi import redirect_to_docs
from app.config.docs_openapi import  custom_openapi_factory
from app.config.configs import get_settings
from api import api_v1

settings = get_settings()

app = FastAPI(root_path="", docs_url=settings.DOCS_ROUTE, openapi_url=settings.OPENAPI_ROUTE)
app.openapi = custom_openapi_factory(app)

app.include_router(health_checks)
app.include_router(redirect_to_docs)
app.include_router(api_v1, prefix=settings.API_VERSION)

if __name__ == "__main__":
    import uvicorn  
    uvicorn.run("api_main:app", host="0.0.0.0", port=settings.port, reload=True)