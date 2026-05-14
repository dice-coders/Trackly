from fastapi import APIRouter, Depends
from schemas.lead_schemas import LeadReceive, LeadResponse
from services.lead_service import LeadService
from dependencies import get_lead_service 
router = APIRouter()

@router.post("/leads", response_model=LeadResponse)
def receive_leads_data(schema: LeadReceive, service: LeadService = Depends(get_lead_service)) :
    return service.receive_data(schema)