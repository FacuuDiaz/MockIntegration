from fastapi.responses import Response, JSONResponse
from app.utils import XMLViewRequest
from app.forms.SubscriptionForm import *
import json
from xmltodict import unparse 
from app import users,service
class SubscriptionXMLView(XMLViewRequest):
    validation_class = SubscriptionRequestForm
    response_class = SubscriptionResponseForm
    def content(self, data) -> Response:
        """Function `Content`

        Args:
            data (dict): A Dictionary with all de data from the request to process

        Returns:
            Response: A Response with the xml content with a values like this:
                ```
                <ocsResponse>
                    <sequenceNo>1404556</sequenceNo>
                    <cpcgFlag>10</cpcgFlag>
                    <requestType>20</requestType>
                    <serviceNode>Zmessenger</serviceNode>
                    <bearerId>WEB</bearerId>
                    <callingParty>750190029</callingParty>
                    <serviceId>6774_1</serviceId>
                    <serviceType>Pick_Win_5</serviceType>
                    <category>-1</category>
                    <contentId>-1</contentId>
                    <planId>Zmess_6774_1</planId>
                    <subscrFlag>S</subscrFlag>
                    <balanceAmount>0.0</balanceAmount>
                    <subsCharge>0.0</subsCharge>
                    <refundAmount>0.0</refundAmount>
                    <errorCode>3021</errorCode>
                    <result>Ok, Accepted</result>
                </ocsResponse>
                ```
        """
        service_data = service.get_service(data['serviceId'])
        user_exist = users.exist_user(data['callingParty'],data['serviceId'])
        if user_exist: 
            return JSONResponse(content={"error":True,"detail":"The current user exist in the system for the service provided"},status_code=400)

        user_register = users.register_user(data['callingParty'])
        if user_register:
            user = next((user for user in users.users if user['callingParty'] == data['callingParty']),None)
            user['service'].append(service_data)
            users.save_data()
        else:
            user_data = users.format_user(self.format_response(data))
            user_data={**user_data, 'service': [service_data]}
            users.save_user(user_data)

        return self.make_response(data,status_code=201)