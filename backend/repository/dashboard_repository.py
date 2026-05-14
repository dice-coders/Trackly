from sqlalchemy import func, select
from sqlalchemy.orm import Session
import models.lead_model as lead_model

def get_total_leads(db: Session) -> int:
    return db.scalar(select(func.count(lead_model.Lead.id)))

def get_leads_by_age(db: Session) -> list:
    return db.execute(
        select(lead_model.Lead.age, func.count(lead_model.Lead.id))
        .group_by(lead_model.Lead.age)
        .order_by(lead_model.Lead.age)
    ).all()

def get_leads_by_genre(db: Session) -> list:
    return db.execute(
        select(lead_model.Lead.genre, func.count(lead_model.Lead.id))
        .group_by(lead_model.Lead.genre)
    ).all()