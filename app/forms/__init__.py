from pydantic import BaseModel
class BaseResponseForm(BaseModel):
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
