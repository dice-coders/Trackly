from sqlalchemy import select
from models.user_model import User
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
        
    def get_user_by_id(self, id: int) -> User:
        return self.db.get(User, id)

    def get_all_users(self) -> List[User]:
        return self.db.scalars(select(User)).all()

    def update_users(self, user: User) :
        db_user = self.db.get(User, user.id)
        #Fazer lógica de atualização depois
        return db_user

    def delete_user(self, id: int) :
        self.db.delete(User).where(User.id == id)
        