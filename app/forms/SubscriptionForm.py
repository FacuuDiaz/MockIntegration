from pydantic import BaseModel
from typing import Optional
class SubscriptionRequestForm(BaseModel):
    serviceNode:str
    sequenceNo:str
    cpcgFlag:int
    requestType:int
    callingParty:str
    calledParty:Optional[str]  = ""
    planId:str
    subscrFlag:str
    startTime:int
    serviceId:str
    serviceType:str
    bundleType: str = ""
    asyncFlag:str
    usageFlag:Optional[str]  = ""
    contentId:str
    languageId:Optional[str]  = ""
    usage:Optional[int] = 0
    bearerId:str
    reqSource:Optional[str]  = ""
    crInfo:Optional[str]  = ""
    category:str = ""
    newContentId:Optional[str]  = ""
    contentName:Optional[str]  = ""
    toneChange:Optional[str]  = ""
    OptionalParams: Optional[str] = ""


class SubscriptionResponseForm(BaseModel):
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