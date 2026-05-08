from ..schemas import goal_schemas as s
from ..models import goal_model as model
from ..repository import goal_repository as repo
def create_goal() :
    pass
def get_goal_id() :
    pass
def get_all_goal() :
    pass
def update_goal() :
    pass
def delete_goal() :
    pass

def field_not_none_validate(id: int, data: s.GoalResponse) -> model.Goal:
    
    goal = repo.get_goal_by_id(id)
    new_data = goal_response_to_model(data)
    
    for field in ["title", "description", "state"]:
        value = getattr(new_data, field)

        if value is not None:
            setattr(goal, field, value)
    return goal

def goal_create_to_model(schema: s.GoalCreate) -> model.Goal:
    goal = model.Goal(
        title = schema.title,
        description = schema.description,
        state = schema.state
    )
    return goal

def goal_response_to_model(schema: s.GoalResponse) -> model.Goal:
    goal = model.Goal(
        title = schema.title,
        description = schema.description,
        state = schema.state
    )
    return goal

def goal_update_to_model(schema: s.GoalUpdate) -> model.Goal:
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

def attributes_not_null() :
    pass