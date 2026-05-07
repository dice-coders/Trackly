from pydantic import BaseModel
from typing import Optional

class GoalBase(BaseModel):
    title: str
    description: str
    state: str

class GoalCreate(GoalBase):
    pass

class GoalResponse(GoalBase):
    pass

class GoalUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    state: Optional[str] = None