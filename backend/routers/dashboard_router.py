from fastapi import APIRouter, Depends
from dependencies import get_dashboard_service
from services.dashboard_service import DashboardService

router = APIRouter(prefix="/dashboard", tags=["Dashboard defs"])

@router.get("/", response_model=dict)
def get_dashboard(service: DashboardService = Depends(get_dashboard_service)):
    return service.get_dashboard()