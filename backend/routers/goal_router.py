from fastapi import APIRouter
from schemas.goal_schemas import (GoalCreate, GoalUpdate)
router = APIRouter()
from services.goal_service import (create_goal, get_goal_by_id, get_all_goals, update_goal, delete_goal)

@router.post("/")
def create_goal(schema: GoalCreate) :
    return create_goal(schema)

@router.get("/")
def get_all_goal() :
    return get_all_goals()

@router.get("/{id}")
def get_goal_by_id(id: int) :
    return get_all_goals(id)

@router.put("/")
def update_goal(id: int, schema: GoalUpdate) :
    return update_goal(id, schema)

@router.delete("/{id}")
def delete_goal(id: int) :
    delete_goal(id)
    