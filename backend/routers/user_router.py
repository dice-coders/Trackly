from fastapi import APIRouter, Depends
from typing import List
from dependencies import get_user_service
from services.user_service import UserService
from services.user_service import (UserService)
from schemas.user_schema import UserCreate, UserResponse, UserUpdate
router = APIRouter()

class UserRouters :
    def __init__(self, service: UserService = Depends(get_user_service)) :
        self.service = service
        
    @router.post("/user", response_model=UserResponse, status_code=201)
    def user_create(self, schema: UserCreate) :
        return self.service.save_user(schema)
        
    @router.get("/user/{id}", response_model=UserResponse, status_code=200)
    def user_get(self, id: int) :
        return self.service.get_user(id)


    @router.get("/user", response_model=List[UserResponse], status_code=201)
    def user_list(self) :
        return self.service.list_user()

    @router.put("/user/{id}")
    def user_update(self, id: int, schema: UserUpdate) :
        return self.service.update_user(id, schema)

    @router.delete("/user/{id}")
    def user_delete(self, id: int) :
        self.service.delete_user(id)