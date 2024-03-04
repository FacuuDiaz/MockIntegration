from fastapi.responses import Response, JSONResponse
from app.utils import XMLViewRequest
from app.forms.unsubscriptionForm import *
import json
from xmltodict import unparse 
from app import users,service
class UnsubscriptionXMLView(XMLViewRequest):
    validation_class = UnsubscribeRequestForm
    response_class = UnsubscribeResponseForm
    def content(self, data) -> Response:
        service_data = service.get_service(data['serviceId'])
        user_exist = users.exist_user(data['callingParty'],data['serviceId'])
        if not user_exist: 
            return JSONResponse(content={"error":True,"detail":"The current user not exist in the system for the service provided"},status_code=400)

        user_register = users.register_user(data['callingParty'])
        if not user_register:
            return JSONResponse(content={"error":True,"detail":"The current user not register in the system for the service provided"},status_code=400)

        users.deactivate_service_user(data['callingParty'],data['serviceId'])

        return self.make_response(data)