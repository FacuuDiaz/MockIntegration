from pydantic import BaseModel
from typing import Optional
from app.forms import BaseResponseForm
class UnsubscribeRequestForm(BaseModel):
    serviceNode:str
    sequenceNo:str
    cpcgFlag:int
    requestType:int
    callingParty:str
    calledParty:Optional[str]=""
    subscrFlag:str
    startTime:int
    serviceId:str
    serviceType:str
    bundleType:Optional[str]=""
    asyncFlag:str
    contentId:str
    bearerId:str
    crInfo:Optional[str]=""
    category:str
    contentName:Optional[str]=""

class UnsubscribeResponseForm(BaseModel):
    sequenceNo: int
    cpcgFlag: int
    requestType: int
    serviceNode: str
    bearerId: str
    callingParty: str
    serviceId: str
    serviceType: str
    category: int
    contentId: int
    planId: str
    subscrFlag: str = "S"
    balanceAmount: float = 0.0 
    chargeAmount: float = 0.0
    refundAmount: float = 0.0
    resultCode: int = 3021
    result: str = "Ok, Accepted"


