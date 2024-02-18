from xml.etree import ElementTree as ET
from xmlschema import XMLSchema
from pydantic import ValidationError
def is_valid_xml(xml_string: str, xsd_path: str) -> bool:
    try:
        schema = XMLSchema(xsd_path)
        root = ET.fromstring(xml_string)
        return schema.is_valid(root)
    except Exception as e:
        return False
    
def validate_form(data: dict, form):
    try:
        form = form(**data)
        return True, None
    except ValidationError as e:
        return False, e.errors()