from fastapi import HTTPException
import json
from app.forms.SubscriptionStatusForm import Service
class ServiceManager:
    def __init__(self):
        self.services = self.get_services()
    
    def get_services(self):
        with open('db/services.json', 'r') as f:
            services = json.load(f)
        return services
    
    def format_service(self,data:dict)->dict:
        return json.loads(Service(**data).model_dump_json()) 
    
    def exist_service(self,id:str) -> bool:
        for service in self.services:
            if id == service['serviceId']:
                return True
        return False
    
    def get_service(self, id:str) -> dict:
        for service in self.services:
            if id == service['serviceId']:
                return service
        raise HTTPException(status_code=404,detail="Service not found with the Id provided")