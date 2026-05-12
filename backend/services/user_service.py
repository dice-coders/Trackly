from repository.user_repository import UserRepository
from schemas.user_schema import (UserCreate, UserResponse, UserUpdate)
from models.user_model import User

from typing import List
#Ajustar a injeção de dependencia amanhã
class UserService :
    def __init__(self, repo: UserRepository) :
        self.repo = repo        
       
    def save_user(self, schema: UserCreate) -> User :
        user = self.parse_user_create(schema)
        return self.repo.create_user(user)
    
    def get_user(self, id: int) -> User :
        return self.repo.get_user_by_id(id)
    
    def list_user(self) -> List[User] :
        return self.repo.get_all_users()
    
    def update_user(self,id: int, schema: UserUpdate) -> User :
        return self.field_not_none_validate(id, schema)
    
    def delete_user(self, id: int) -> None :
        self.repo.delete_user(id)


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
    
    def field_not_none_validate(self, id: int, schema: UserResponse) -> User:
        
        user = self.repo.get_goal_by_id(id)
        new_data = self.parse_user_response(schema)
        
        for field in ["name", "email", "number", "address", "role"]:
            value = getattr(new_data, field)

            if value is not None:
                setattr(user, field, value)
        return user