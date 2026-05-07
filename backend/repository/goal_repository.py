from sqlalchemy import delete
import database
import models.goal_model as model

def create_goal(goal: model.Goal, db = database.get_db):
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

def update_goal(goal: model.Goal, id: int, db = database.get_bd):
    old_goal = db.get(model.Goal,id)
    new_goal: model.Goal

    if not goal.title:
        new_goal.title = goal.title

    if not goal.description:
        new_goal.description = goal.description

    if not goal.state:
        new_goal.state = goal.state

    db.commit()
    db.refresh(new_goal)
    return new_goal