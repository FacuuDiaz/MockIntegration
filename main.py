 
from fastapi import FastAPI, Request
from app.views.susbcription import SubscriptionXMLView
from app.views.status import SubscriptionStatusXMLView
from app.views.unsubscription import UnsubscriptionXMLView
app = FastAPI()

@app.post("/subscription")
async def subscription(request: Request):
    return await SubscriptionXMLView.run(request)

@app.post("/status")
async def status(request: Request):
    return await SubscriptionStatusXMLView.run(request)

@app.post("/unsubscription")
async def unsubscription(request: Request):
    return await UnsubscriptionXMLView.run(request)