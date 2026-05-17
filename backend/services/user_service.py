from repository.user_repository import UserRepository
from schemas.user_schema import (UserCreate, UserResponse, UserUpdate)
from models.user_model import User
from passlib.hash import sha256_crypt
from typing import List
#Ajustar a injeção de dependencia amanhã
class UserService :
    def __init__(self, repo: UserRepository) :
        self.repo = repo        
       
       
    def save_user(self, schema: UserCreate) -> User :
        user = self.parse_user_create(schema)
        return self.repo.create_user(user)
    
    def get_user(self, id: int) -> User :
        return self.repo.get_user(id)
    
    def get_user_by_email(self, email: str) :
        return self.repo.get_user_by_email(email)
    
    def list_user(self) -> List[User] :
        return self.repo.list_user()
    
    def update_user(self,id: int, schema: UserUpdate) -> User :
        user = self.field_not_none_validate(id, schema)
        return self.repo.update_users(user)
    
    def delete_user(self, id: int) -> None :
        return self.repo.delete_user(id)

    #Transforma schemas em objetos
    def parse_user_create(self, schema: UserCreate) -> User :
        user = User(
            name = schema.name,
            email = schema.email,
            number = schema.number,
            address = schema.address,
            role = schema.role,
            hash = self.hashing(schema.password)
        )
        return user
    def parse_user_update(self, id: int, schema: UserUpdate) -> User :
        user = User(
            name = schema.name,
            email = schema.email,
            number = schema.number,
            address = schema.address,
            role = schema.role,
            id = id,
            hash = self.hashing(schema.password)
        )
        return user
    def parse_user_response(self, id:int, schema: UserResponse) -> User :
        user = User(
            name = schema.name,
            email = schema.email,
            number = schema.number,
            address = schema.address,
            role = schema.role,
            
        )
        return user
    
    #Válida se os campos são nulos
    def field_not_none_validate(self, id: int, schema: UserUpdate) -> User:
        
        user = self.repo.get_user(id)
        new_data = self.parse_user_update(id, schema)
        
        for field in ["name", "email", "number", "address", "role"]:
            value = getattr(new_data, field)

            if value is not None:
                setattr(user, field, value)
        return user
    
    #Criptograda uma variavel
    def hashing(self, password: str) -> str:
        return sha256_crypt.using(rounds=8000).hash(password)
    
    #Verifica uma variavel por meio de comparação
    def verify_password(self, password: str, hash: str) -> bool:
        return sha256_crypt.verify(password, hash)