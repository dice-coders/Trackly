from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import services.dashboard_service as service
from schemas.dashboard_schema import DashboardResponse

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/", response_model=DashboardResponse)
def get_dashboard(db: Session = Depends(get_db)):
    return service.get_dashboard(db)