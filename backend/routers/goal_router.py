from dependencies import get_goal_service
from services.goal_service import GoalService
from fastapi import APIRouter, Depends
from schemas.goal_schemas import (GoalCreate, GoalUpdate, GoalResponse)
router = APIRouter()

@router.post("/goal/{JSON}", response_model=GoalResponse, status_code=201)
def create_goal(schema: GoalCreate, service: GoalService = Depends(get_goal_service)) :
    return service.create_goal(schema)

@router.get("/goal", response_model=list[GoalResponse], status_code=200)
def list_goals(service: GoalService = Depends(get_goal_service)) :
    return service.list_goals()

@router.get("/goal/{id}", response_model=GoalResponse, status_code=200)
def get_goal(id: int, service: GoalService = Depends(get_goal_service)) :
    return service.get_goal(id)

@router.put("/goal/{id}", response_model=GoalResponse, status_code=200)
def update_goal(id: int, schema: GoalUpdate, service: GoalService = Depends(get_goal_service)) :
    return service.update_goal(id, schema)

@router.delete("/goal/{id}", status_code=204)
def delete_goal(id: int, service: GoalService = Depends(get_goal_service)) :
    service.delete_goal(id)
    