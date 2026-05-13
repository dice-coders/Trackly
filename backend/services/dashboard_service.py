from sqlalchemy.orm import Session
import repository.dashboard_repository as repo
from schemas.dashboard_schema import (
    DashboardResponse, UsersByDate, UsersByRole, GoalsByState
)

def get_dashboard(db: Session) -> DashboardResponse:
    return DashboardResponse(
        total_users=repo.get_total_users(db),
        total_goals=repo.get_total_goals(db),
        users_by_date=[
            UsersByDate(date=str(row[0]), count=row[1])
            for row in repo.get_users_by_date(db)
        ],
        users_by_role=[
            UsersByRole(role=row[0] or "undefined", count=row[1])
            for row in repo.get_users_by_role(db)
        ],
        goals_by_state=[
            GoalsByState(state=row[0] or "undefined", count=row[1])
            for row in repo.get_goals_by_state(db)
        ],
    )