from fastapi import APIRouter, Depends
from repository.goal_repository import Session
from schemas.goal_schemas import (GoalCreate, GoalUpdate, GoalResponse)
from services.goal_service import (create_goal, get_goal, update_goal, delete_goal, list_goals)
from database import get_db
router = APIRouter()


@router.post("/{JSON}", response_model=GoalResponse, status_code=201)
def post_goal(schema: GoalCreate, db: Session = Depends(get_db)) :
    return create_goal(schema, db)

@router.get("/", response_model=list[GoalResponse], status_code=200)
def get_all_goal(db: Session = Depends(get_db)) :
    return list_goals(db)

@router.get("/{id}", response_model=GoalResponse, status_code=200)
def get_goal_id(id: int, db: Session = Depends(get_db)) :
    return get_goal(id, db)

@router.put("/", response_model=GoalResponse, status_code=200)
def put_goal(id: int, schema: GoalUpdate, db: Session = Depends(get_db)) :
    return update_goal(id, schema, db)

@router.delete("/{id}", status_code=204)
def del_goal(id: int, db: Session = Depends(get_db)) :
    delete_goal(id, db)
    