from sqlalchemy import select
from models.user_model import User
from sqlalchemy import delete
from sqlalchemy.orm import Session
from typing import List

class UserRepository :
    def __init__(self, db: Session) :
        self.db = db
    
    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
        
    def get_user(self, id: int) -> User:
        return self.db.get(User, id)

    def list_user(self) -> List[User]:
        return self.db.scalars(select(User)).all()

    def update_users(self, user: User) -> User:
        updated = self.db.merge(user)
        self.db.add(updated)
        self.db.commit()
        self.db.refresh(updated)
        return updated

    def delete_user(self, id: int) -> None:
        self.db.execute(delete(User).where(User.id == id))
        self.db.commit()
        return None
        