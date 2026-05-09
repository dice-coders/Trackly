
from sqlalchemy import delete, select
import database
import models.goal_model as model

def create_goal(goal: model.Goal, db = database.get_db):
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

def get_goal_by_id(id: int, db = database.get_bd) :
    return db.get(model.Goal, id)

def get_all_goals(db = database.get_db) :
    return db.scalars(select(model.Goal)).all()

def update_goal(goal: model.Goal, db = database.get_bd):
    db.add(goal)
    db.commit()
    db.refresh(goal)

    return goal

def delete_goal(id: int, db = database.get_bd) :
    db.execute(delete(model.Goal).where(model.Goal.id == id))
    db.commit()
    
    
    
