from ..schemas import goal_schemas as s
from ..models import goal_model as model
def create_goal() :
    pass
def get_goal_by_id() :
    pass
def get_all_goal() :
    pass
def update_goal() :
    pass
def delete_goal() :
    pass


def convert_GoalCreate_in_object(schema: s.GoalCreate) -> model.Goal:
    goal = model.Goal(
        title = schema.title,
        description = schema.description,
        state = schema.state
    )
    return goal

def convert_GoalResponse_in_object() :
    pass

def convert_GoalUpdate_in_object() :
    pass

def object_not_null() :
    pass

def attributes_not_null() :
    pass