from sqlalchemy import func, select
from sqlalchemy.orm import Session
import models.lead_model as lead_model

class DashboardRepository:
    def __init__(self, db: Session) :
        self.db = db
        
    def get_total_leads(self) -> int:
        return self.db.scalar(select(func.count(lead_model.Lead.id)))

    def get_leads_by_age(self) -> list:
        return self.db.execute(
            select(lead_model.Lead.age, func.count(lead_model.Lead.id))
            .group_by(lead_model.Lead.age)
            .order_by(lead_model.Lead.age)
        ).all()

    def get_leads_by_genre(self) -> list:
        return self.db.execute(
            select(lead_model.Lead.genre, func.count(lead_model.Lead.id))
            .group_by(lead_model.Lead.genre)
        ).all()