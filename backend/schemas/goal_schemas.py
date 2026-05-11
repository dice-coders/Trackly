from pydantic import BaseModel, ConfigDict
from typing import Optional
class GoalBase(BaseModel):
    title: str
    description: str
    state: str
    

class GoalCreate(GoalBase):
    model_config = ConfigDict(from_attributes=True)

class GoalResponse(GoalBase):
    model_config = ConfigDict(from_attributes=True)

class GoalUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    state: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
    
