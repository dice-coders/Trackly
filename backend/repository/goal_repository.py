from sqlalchemy import delete, select
from database import get_db
from models.goal_model import Goal

def create_goal(goal: Goal, db = get_db):
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

def get_goal_by_id(id: int, db = get_db) :
    return db.get(Goal, id)

def get_all_goals(db = get_db) :
    return db.scalars(select(Goal)).all()

def update_goal(goal: Goal, db = get_db):
    db.add(goal)
    db.commit()
    db.refresh(goal)

    return goal

def delete_goal(id: int, db = get_db) :
    db.execute(delete(Goal).where(Goal.id == id))
    db.commit()
    
    
    
