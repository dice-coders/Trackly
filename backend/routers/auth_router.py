from fastapi import APIRouter, Depends, HTTPException, status
from dependencies import get_user_service
from schemas.auth_schema import LoginRequest, TokenResponse
from services.user_service import UserService
from auth.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest, service: UserService = Depends(get_user_service)) :
    user = service.get_user_by_email(body.email)
    
    if not user or not service.verify_password(body.password, user.hash) :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZES, detail="Email ou senhas incorretos")
    
    token = create_access_token({"sub": str(user.id)})
    return TokenResponse(access_token=token)