from sqlalchemy import func, select
from sqlalchemy.orm import Session
import models.user_model as user_model
import models.goal_model as goal_model


def get_total_users(db: Session) -> int:
    return db.scalar(select(func.count(user_model.User.id)))


def get_total_goals(db: Session) -> int:
    return db.scalar(select(func.count(goal_model.Goal.id)))


def get_users_by_date(db: Session) -> list:
    return db.execute(
        select(user_model.User.date_creation, func.count(user_model.User.id))
        .group_by(user_model.User.date_creation)
        .order_by(user_model.User.date_creation)
    ).all()


def get_users_by_role(db: Session) -> list:
    return db.execute(
        select(user_model.User.role, func.count(user_model.User.id))
        .group_by(user_model.User.role)
    ).all()


def get_goals_by_state(db: Session) -> list:
    return db.execute(
        select(goal_model.Goal.state, func.count(goal_model.Goal.id))
        .group_by(goal_model.Goal.state)
    ).all()