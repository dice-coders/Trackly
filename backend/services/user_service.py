from repository.user_repository import (create_user as repo_create_user,
                                        get_user_by_id as repo_get_user_by_id,
                                        get_all_users as repo_get_all_users,
                                        update_users as repo_update_users,
                                        delete_user as repo_delete_user
                                        )
from schemas.user_schema import (UserCreate, UserResponse, UserUpdate)
from models.user_model import User
from database import Session
from typing import List
class UserService :
    def __init__(self, db: Session) :
        self.db = db
        
        
    def create_user(self, schema: UserCreate) -> User :
        user = self.parse_user_create(schema)
        return repo_create_user(user)
    
    def get_user_by_id(self, id: int) -> User :
        return repo_get_user_by_id(id)
    
    def get_all_users(self) -> List[User] :
        return repo_get_all_users()
    
    def update_user(self, schema: UserUpdate) -> User :
        user = self.parse_user_update(schema)
        return repo_update_users(user)
    
    def delete_user(self, id: int) -> None :
        repo_delete_user(id)


    def parse_user_create(self, schema: UserCreate) -> User :
        user = User(
            name = schema.name,
            email = schema.email,
            number = schema.number,
            address = schema.address,
            role = schema.role,
            #hash
        )
        return user
    def parse_user_update(self, schema: UserUpdate) -> User :
        user = User(
            name = schema.name,
            email = schema.email,
            number = schema.number,
            address = schema.address,
            role = schema.role,
            #hash
        )
        return user
    def parse_user_response(self, schema: UserResponse) -> User :
        user = User(
            name = schema.name,
            email = schema.email,
            number = schema.number,
            address = schema.address,
            role = schema.role,
            
        )
        return user
    
    #Até então só se aplicam no Update
    def is_not_null(self) -> bool:
        pass #Faça depois
    
    def attribute_is_not_null() -> bool:
        pass #Faça depois
