
from sqlalchemy import delete, select
from database import get_db
import models.goal_model as model

def create_goal(goal: model.Goal, db = get_db):
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

def get_goal_by_id(id: int, db = get_db) :
    return db.get(model.Goal, id)

def get_all_goals(db = get_db) :
    return db.scalars(select(model.Goal)).all()

def update_goal(goal: model.Goal, db = get_db):
    db.add(goal)
    db.commit()
    db.refresh(goal)

    return goal

def delete_goal(id: int, db = get_db) :
    db.execute(delete(model.Goal).where(model.Goal.id == id))
    db.commit()
    
    
    
