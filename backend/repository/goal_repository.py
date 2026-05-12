from sqlalchemy import delete, select
from sqlalchemy.orm import Session
from models.goal_model import Goal
from typing import List
class GoalRepository :
    def __init__(self, db: Session) :
        self.db = db
        
    def create_goal(self, goal: Goal) -> Goal :
        self.db.add(goal)
        self.db.commit()
        self.db.refresh(goal)
        return goal

    def get_goal(self, id: int) -> Goal :
        return self.db.get(Goal, id)

    def list_goals(self) -> List[Goal] :
        return self.db.scalars(select(Goal)).all()

    def update_goal(self, goal: Goal) -> Goal :
        updated = self.db.merge(goal)
        self.db.commit()
        self.db.refresh(updated)
        return updated

    def delete_goal(self, id: int) -> None:
        self.db.execute(delete(Goal).where(Goal.id == id))
        self.db.commit()
        
        
        
