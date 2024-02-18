from pydantic import BaseModel
from typing import Optional,List
from datetime import datetime
class Service(BaseModel):
    serviceType: str
    serviceId: str
    planId: str
    contentId: int
    category: int
    renewalDate: str = str(datetime.today().timestamp())
    graceExpDate: str = str(datetime.today().timestamp())
    suspendExpDate: str = str(datetime.today().timestamp())
    languageId: str
    status: str = "A"

class SuscriptionStatusRequestForm(BaseModel):
    sequenceNo: str
    cpcgFlag: int
    requestType: int
    serviceNode: str
    serviceId: str
    callingParty: str

class SubscriptionStatusBaseForm(BaseModel):
    sequenceNo: int
    cpcgFlag: int
    requestType: int
    serviceNode: str
    callingParty: str
    resultCode: int
    result: str

class SubscriptionStatusResponseForm(SubscriptionStatusBaseForm):
    service: List[Service]