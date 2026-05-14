from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from repository.user_repository import UserRepository
from repository.goal_repository import GoalRepository
from repository.lead_repository import LeadRepository
from services.user_service import UserService
from services.goal_service import GoalService
from services.lead_service import LeadService

def get_user_repository(db: Session = Depends(get_db)) :
    return UserRepository(db)
def get_goal_repository(db: Session = Depends(get_db)) :
    return GoalRepository(db)
def get_lead_repository(db: Session = Depends(get_db)) :
    return LeadRepository(db)

def get_user_service(repo: UserRepository = Depends(get_user_repository)) :
    return UserService(repo)
def get_goal_service(repo: GoalRepository = Depends(get_goal_repository)) :
    return GoalService(repo)
def get_lead_service(repo: LeadRepository = Depends(get_lead_repository)) :
    return LeadService(repo)