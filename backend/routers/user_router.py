from fastapi import APIRouter, Depends
from typing import List
from dependencies import get_user_service
from services.user_service import UserService
from services.user_service import (UserService)
from schemas.user_schema import UserCreate, UserResponse, UserUpdate
router = APIRouter(prefix="/user", tags=["User defs"])

@router.post("/user", response_model=UserResponse, status_code=201)
def user_create(schema: UserCreate, service: UserService = Depends(get_user_service)) :
    return service.save_user(schema)
    
@router.get("/user/{id}", response_model=UserResponse, status_code=200)
def user_get(id: int, service: UserService = Depends(get_user_service)) :
    return service.get_user(id)

@router.get("/user", response_model=List[UserResponse], status_code=201)
def user_list(service: UserService = Depends(get_user_service)) :
    return service.list_user()

@router.put("/user/{id}")
def user_update(id: int, schema: UserUpdate, service: UserService = Depends(get_user_service)) :
    return service.update_user(id, schema)

@router.delete("/user/{id}", response_model=None, status_code=200)
def user_delete(id: int, service: UserService = Depends(get_user_service)) :
    return service.delete_user(id)