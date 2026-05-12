from fastapi import APIRouter
from services.user_service import (UserService)
from schemas.user_schema import UserCreate, UserResponse, UserUpdate
router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=201)
def user_create(schema: UserCreate) :
    return UserService.save_user(schema)

@router.get("/{id}", response_model=UserResponse, status_code=200)
def user_get(id: int) :
    return UserService.get_user(id)

@router.get("/")
def user_list() :
    return UserService.list_user()

@router.put("/{id}")
def user_update(id: int, schema: UserUpdate) :
    return UserService.update_user(schema)

@router.delete("/{id}")
def user_delete(id: int) :
    UserService.delete_user(id)