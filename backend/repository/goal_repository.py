from sqlalchemy import delete, select
from sqlalchemy.orm import Session
from models.goal_model import Goal

def create_goal(goal: Goal, db: Session) -> Goal :
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

def get_goal_by_id(id: int, db: Session) -> Goal :
    return db.get(Goal, id)

def get_all_goals(db: Session) -> Goal :
    return db.scalars(select(Goal)).all()

def update_goal(goal: Goal, db: Session) -> Goal :
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

def delete_goal(id: int, db: Session) :
    db.execute(delete(Goal).where(Goal.id == id))
    db.commit()
    
    
    
