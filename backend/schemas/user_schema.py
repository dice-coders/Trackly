from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Optional, Literal

class UserBase(BaseModel) :
    name: str = Field(max_length=120)
    email: EmailStr = Field(max_length=120)
    number: str = Field(min_length=11, max_length=11)
    address: str
    role: Literal["ADM"]

class UserCreate(UserBase) :
    password: str
    model_config = ConfigDict(from_attributes=True)
    
class UserResponse(UserBase) :    
    model_config = ConfigDict(from_attributes=True)
    
class UserUpdate(BaseModel) :
    name: Optional[str] = Field(default=None, max_length=120)
    email: Optional[EmailStr] = Field(default=None, max_length=120)
    number: Optional[str] = Field(default=None, min_length=11, max_length=11)
    address: Optional[str] = Field(default=None)
    role: Optional[Literal["ADM"]] = Field(default=None)
    password: Optional[str] = Field(default=None)
    
    model_config = ConfigDict(from_attributes=True)