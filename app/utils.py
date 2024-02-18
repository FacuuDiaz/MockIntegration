from fastapi.responses import JSONResponse, Response
from app.helper import validate_form
from fastapi import Request
from xmltodict import parse as parse_xml,unparse
from app.decorators import validate_header
import json

class ViewRequest (object):
    validation_class = None
    content_type_valid = "json"
    def __init__(self, request):
        self.request = request

    async def content(self,data:dict) -> Response:
        raise NotImplementedError

    def set_data(self,data:dict) -> dict:
        return data

    async def get_data(self):
        content = await self.request.body()
        res = parse_xml(content.decode())
        return res

    def validate(self,data):
        return validate_form(data, self.validation_class)

    @classmethod
    @validate_header()
    async def run(cls,request:Request)->Response:
        instance = cls(request)
        data = await instance.get_data()
        data = instance.set_data(data)
        is_valid,errors = instance.validate(data)
        if is_valid:
            return instance.content(data)
        else:
            return JSONResponse(status_code=400, content={"error":True,"detail":"The content is invalid","error": errors})



class XMLViewRequest(ViewRequest):
    content_type_valid = "xml"
    response_class = None
    def set_data(self, data: dict) -> dict:
        return data['ocsRequest']
    
    def format_response(self,data:dict) -> dict:
        form = self.response_class(**data)
        response_values = json.loads(form.model_dump_json())
        return response_values

    def make_response(self,data:dict,status_code=200) ->dict:
        response_values = self.format_response(data)
        headers = {"Content-Type": "application/xml"}
        response = unparse({"ocsRequest":response_values})
        return Response(content=response, status_code=status_code, headers=headers)