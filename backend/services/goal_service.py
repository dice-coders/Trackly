from repository.goal_repository import (
    create_goal as repo_create_goal,
    get_goal_by_id as repo_get_goal_by_id,
    get_all_goals as repo_get_all_goals,
    update_goal as repo_update_goal,
    delete_goal as repo_delete_goal,
    Session
)
from schemas.goal_schemas import (GoalCreate, GoalResponse, GoalUpdate)
from models.goal_model import Goal




def create_goal(schema: GoalCreate, db: Session) -> Goal:
    goal = goal_create_to_model(schema)
    
    return repo_create_goal(goal, db)

def get_goal(id: int, db: Session) -> Goal:
    id_checker(id)
        
    goal = repo_get_goal_by_id(id, db)
    return goal

def get_all_goals(db: Session):
    goals = repo_get_all_goals(db)
    return [GoalResponse.model_validate(g) for g in goals]

def update_goal(id: int, schema: GoalUpdate, db: Session) -> Goal:
    id_checker(id)
        
    goal = goal_update_to_model(schema)
    updated = repo_update_goal(goal, db)
    return updated

def delete_goal(id: int, db: Session):
    id_checker(id)
        
    repo_delete_goal(id, db)



def goal_create_to_model(schema: GoalCreate) -> Goal:
    goal = Goal(
        title = schema.title,
        description = schema.description,
        state = schema.state
    )
    return goal

def goal_response_to_model(schema: GoalResponse) -> Goal:
    goal = Goal(
        title = schema.title,
        description = schema.description,
        state = schema.state
    )
    return goal

def goal_update_to_model(schema: GoalUpdate) -> Goal:
    goal = Goal(
        title = schema.title,
        description = schema.description,
        state = schema.state
    )
    return goal

def object_not_null(goal: Goal) :
    if goal is not None :
        return goal
    #raise a global exception handler

def field_not_none_validate(id: int, data: GoalResponse, db: Session) -> Goal:
    
    goal = repo_get_goal_by_id(id, db)
    new_data = goal_response_to_model(data)
    
    for field in ["title", "description", "state"]:
        value = getattr(new_data, field)

        if value is not None:
            setattr(goal, field, value)
    return goal

def id_checker(id: int) :
    if id is not None :
        return id
