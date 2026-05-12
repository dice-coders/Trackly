from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from repository.user_repository import UserRepository
from repository.goal_repository import GoalRepository
from services.user_service import UserService

def get_user_repository(db: Session = Depends(get_db)) :
    return UserRepository(db=db)
def get_goal_repository(db: Session = Depends(get_db)) :
    return GoalRepository(db=db)


def get_user_service(repo: UserRepository = Depends(get_user_repository)) :
    return UserService(repo=repo)
def get_goal_repository(repo: GoalRepository = Depends(get_goal_repository)) :
    return GoalRepository(repo=repo)