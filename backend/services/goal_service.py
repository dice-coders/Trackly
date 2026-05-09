from ..schemas import goal_schemas as schemas
from ..models import goal_model as model
from ..repository import goal_repository as repo


def create_goal(schema: schemas.GoalUpdate) -> model.Goal:
    goal = goal_create_to_model(schema)
    repo.create_goal(goal)
    return goal

def get_goal(id: int) -> model.Goal:
    if id_checker(id) :
        raise None
    goal = repo.get_goal_by_id(id)
    return goal

def get_all_goals():
    return repo.get_all_goals()

def update_goal(id: int, schema: schemas.GoalUpdate) -> model.Goal:
    if id_checker(id) :
        raise None
    goal = goal_update_to_model(schema)
    updated = repo.update_goal(goal, id)
    return updated

def delete_goal(id: int) -> None:
    if id_checker(id) :
        raise None
    repo.delete_goal(id)



def goal_create_to_model(schema: schemas.GoalCreate) -> model.Goal:
    goal = model.Goal(
        title = schema.title,
        description = schema.description,
        state = schema.state
    )
    return goal

def goal_response_to_model(schema: schemas.GoalResponse) -> model.Goal:
    goal = model.Goal(
        title = schema.title,
        description = schema.description,
        state = schema.state
    )
    return goal

def goal_update_to_model(schema: schemas.GoalUpdate) -> model.Goal:
    goal = model.Goal(
        title = schema.title,
        description = schema.description,
        state = schema.state
    )
    return goal

def object_not_null(goal: model.Goal) :
    if goal is not None :
        return goal
    #raise a global exception handler

def field_not_none_validate(id: int, data: schemas.GoalResponse) -> model.Goal:
    
    goal = repo.get_goal_by_id(id)
    new_data = goal_response_to_model(data)
    
    for field in ["title", "description", "state"]:
        value = getattr(new_data, field)

        if value is not None:
            setattr(goal, field, value)
    return goal

def id_checker(id: int) :
    if id is not None :
        return id
