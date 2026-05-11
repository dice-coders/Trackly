from sqlalchemy import select
from models.user_model import User
from database import Session
from typing import List
def create_user(user: User, db: Session) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    
def get_user_by_id(id: int, db: Session) -> User:
    return db.get(User, id)

def get_all_users(db: Session) -> List[User]:
    return db.scalars(select(User)).all()

def update_users(user: User, db: Session) :
    db_user = db.get(User, user.id)
    #Fazer lógica de atualização depois
    return db_user

def delete_user(id: int, db: Session) :
    db.delete(User).where(User.id == id)
    