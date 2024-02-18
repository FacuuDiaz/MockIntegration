import json
from app.forms.SubscriptionStatusForm import SubscriptionStatusBaseForm
from fastapi import HTTPException
from typing import Union
class UserManager:
    
    def __init__(self) -> None:
        self.users = self.get_users()
    
    def get_users(self) -> dict:
        with open('db/users.json', 'r') as f:
            users = json.load(f)
        return users
    
    def save_data(self) -> None:
        with open('db/users.json', 'w') as f:
            json.dump(self.users, f, indent=4)
    
    def save_user(self,data:dict) -> None :
        self.users.append(data)
        self.save_data()
    
    def exist_user(self,msisdn:str,serviceId:str) -> bool:
        for user in self.users:
            if msisdn == user['callingParty'] and serviceId:
                if [u for u in user['service'] if u['serviceId'] == serviceId]:
                    return True
        return False

    def register_user(self,msisdn:str) -> bool:
        for user in self.users:
            if msisdn == user['callingParty']:
                return True
        return False

    def format_user(self,data:dict) -> dict:
        return json.loads(SubscriptionStatusBaseForm(**data).model_dump_json())
    

    def get_user(self,msisdn:str) -> Union[None, HTTPException]:
        for user in self.users:
            if msisdn == user['callingParty']:
                return user
        raise HTTPException(status_code=404,detail="User not found with the service provided")

    def deactivate_service_user(self,msisdn:str,serviceId:str) -> Union[None, HTTPException]:
        for user in self.users:
            if msisdn == user['callingParty']:
                if [u for u in user['service'] if u['serviceId'] != serviceId]:
                    for service in user['service']:
                        if service['serviceId'] == serviceId: service['status'] = "D"
                    self.save_data()
                    return True
        raise HTTPException(status_code=404,detail="Cannot deactivate the user because the User is not found with the service provided")