from typing import Coroutine
from fastapi.responses import Response, JSONResponse
from app.utils import XMLViewRequest
from app.forms.SubscriptionStatusForm import *
import json
from xmltodict import unparse 
from app import users,service
class SubscriptionStatusXMLView(XMLViewRequest):
    validation_class = SuscriptionStatusRequestForm
    response_class = SubscriptionStatusResponseForm
    def content(self, data: dict) -> Response:

        service.get_service(data['serviceId'])
        user_exist = users.exist_user(data['callingParty'],data['serviceId'])
        if not user_exist: 
            return JSONResponse(content={"error":True,"detail":"The current user not exist in the system for the service provided"},status_code=400)

        user = users.get_user(data['callingParty'])
        return self.make_response(user)
