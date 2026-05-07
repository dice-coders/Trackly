
from sqlalchemy import delete
import database
import models.goal_model as model



def get_goal_by_id(id: int, db = database.get_bd) :
    return db.get(model.Goal, id)

def delete_goal(id: int, db = database.get_bd) :
    db.execute(delete(model.Goal).where(model.Goal.id == id))
    db.commit()
    
    
    