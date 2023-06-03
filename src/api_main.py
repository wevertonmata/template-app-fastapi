from fastapi import FastAPI
from app.config.docs_openapi import openapi, redirect_to_docs
from app.config.health_checks import health_checks

app = FastAPI(root_path="")
docs = openapi(app)
app.openapi = docs.custom_openapi

app.include_router(health_checks)
app.include_router(redirect_to_docs)


# Route

from api import api_v1

app.include_router(api_v1, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api_main:app", host="0.0.0.0", port=5000, reload=True)