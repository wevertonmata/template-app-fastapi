from fastapi import APIRouter, responses
from fastapi.openapi.utils import get_openapi
import os
import datetime
from pydantic import  EmailStr

DATE = datetime.datetime.today().strftime("%d/%m/%y %H:%M:%S")

class openapi:
    def __init__(self, app):
        self.app = app
        self.title: str =   "template-app-python"
        self.name: str =    "squad-plataforma-ops" # 
        self.email: EmailStr = "contact.squad@gmail.com.br" 
        self.contact: dict =  { "name": self.name, "email": self.email }
        self.description: str = "Insert your description"
        self.version: str = "1.0.0"
        self.license: dict = {"name": f"Version generation date {DATE}"}
        self.servers = []

        if "ENVIRONMENT" in os.environ.keys():
            host = os.environ["ENVIRONMENT"].lower()
            namespace = self.title.strip()
            self.servers = [
                {"url": f"https://{namespace}.{host}.io" , "description": "HTTPS"},
                {"url": f"http://{namespace}.{host}.io", "description": "HTTP"}
            ]
            
           
    def custom_openapi(self):
        if self.app.openapi_schema:
            return self.app.openapi_schema
        openapi_schema = get_openapi(
            title = self.title,
            description = self.description,
            version =  self.version,
            contact = self.contact,
            servers= self.servers,
            license_info= self.license,
            routes=self.app.routes)
        
        self.app.openapi_schema = openapi_schema
        return self.app.openapi_schema


redirect_to_docs = APIRouter()

@redirect_to_docs.get("/",  include_in_schema=False)
async def docs_redirect():
    return responses.RedirectResponse(url='/docs')
