from ..schemas import goal_schemas as s
from ..models import goal_model as model
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

def goal_update_to_model() :
    pass

def object_not_null() :
    pass

def attributes_not_null() :
    pass