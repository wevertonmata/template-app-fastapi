from ddtrace import patch
from fastapi import FastAPI
from v1_api import v1_api
import os
        
patch(fastapi=True)
app = FastAPI(
    title="Sample Python API",
    description="Template API Python using FastAPI",
    version="1",
)

app.mount("/api/v1", v1_api)
