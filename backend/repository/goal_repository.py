
from sqlalchemy import delete
import database
import models.goal_model as model

def create_goal(goal: model.Goal, db = database.get_db):
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

def get_goal_by_id(id: int, db = database.get_bd):
    return db.get(model.Goal, id)
  
def update_goal(goal: model.Goal, id: int, db = database.get_bd):
    old_goal = db.get(model.Goal,id)

    for field in ["title", "description", "state"]:
        value = getattr(goal, field)
        if value is not None:
            setattr(old_goal, field, value)

def update_goal(goal: model.Goal, db = database.get_bd):
    db.add(goal)
    db.commit()
    db.refresh(goal)

    return goal

def delete_goal(id: int, db = database.get_bd) :
    db.execute(delete(model.Goal).where(model.Goal.id == id))
    db.commit()
    
    
    
