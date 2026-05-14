from pydantic import BaseModel

class UsersByDate(BaseModel):
    date: str
    count: int

class UsersByRole(BaseModel):
    role: str
    count: int

class GoalsByState(BaseModel):
    state: str
    count: int

class DashboardResponse(BaseModel):
    total_users: int
    total_goals: int
    users_by_date: list[UsersByDate]
    users_by_role: list[UsersByRole]
    goals_by_state: list[GoalsByState]