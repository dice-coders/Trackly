from repository.goal_repository import (
    create_goal, get_goal_by_id, get_all_goals, update_goal, delete_goal
)
from schemas.goal_schemas import (GoalCreate, GoalResponse, GoalUpdate)
from models.goal_model import Goal



def create_goal(schema: GoalCreate) -> Goal:
    goal = goal_create_to_model(schema)
    create_goal(goal)
    return goal

def get_goal(id: int) -> Goal:
    if id_checker(id) :
        raise None
    goal = get_goal_by_id(id)
    return goal

def get_all_goals():
    return get_all_goals()

def update_goal(id: int, schema: GoalUpdate) -> Goal:
    if id_checker(id) :
        raise None
    goal = goal_update_to_model(schema)
    updated = update_goal(goal, id)
    return updated

def delete_goal(id: int) -> None:
    if id_checker(id) :
        raise None
    delete_goal(id)



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

def field_not_none_validate(id: int, data: GoalResponse) -> Goal:
    
    goal = get_goal_by_id(id)
    new_data = goal_response_to_model(data)
    
    for field in ["title", "description", "state"]:
        value = getattr(new_data, field)

        if value is not None:
            setattr(goal, field, value)
    return goal

def id_checker(id: int) :
    if id is not None :
        return id
