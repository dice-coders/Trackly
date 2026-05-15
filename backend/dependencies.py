from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from repository.user_repository import UserRepository
from repository.goal_repository import GoalRepository
from repository.lead_repository import LeadRepository
from repository.dashboard_repository import DashboardRepository
from repository.chat_history_repository import ChatHistoryRepository
from services.user_service import UserService
from services.goal_service import GoalService
from services.lead_service import LeadService
from services.dashboard_service import DashboardService
from services.chat_history_service import ChatHistoryService

def get_user_repository(db: Session = Depends(get_db)) :
    return UserRepository(db)
def get_goal_repository(db: Session = Depends(get_db)) :
    return GoalRepository(db)
def get_lead_repository(db: Session = Depends(get_db)) :
    return LeadRepository(db)
def get_dashboard_repository(db: Session = Depends(get_db)) :
    return DashboardRepository(db)
def get_chat_history_repository(db: Session = Depends(get_db)) :
    return ChatHistoryRepository(db)

def get_user_service(repo: UserRepository = Depends(get_user_repository)) :
    return UserService(repo)
def get_goal_service(repo: GoalRepository = Depends(get_goal_repository)) :
    return GoalService(repo)
def get_lead_service(repo: LeadRepository = Depends(get_lead_repository)) :
    return LeadService(repo)
def get_dashboard_service(repo: DashboardRepository = Depends(get_dashboard_repository)) :
    return DashboardService(repo)
def get_chat_history_service(repo: ChatHistoryRepository = Depends(get_chat_history_repository)) :
    return ChatHistoryService(repo)