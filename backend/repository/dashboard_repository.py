from sqlalchemy import func, select
from sqlalchemy.orm import Session
from models.lead_model import Lead

class DashboardRepository:
    def __init__(self, db: Session) :
        self.db = db
        
    def get_total_leads(self) -> int:
        return self.db.scalar(select(func.count(Lead.id)))

    def get_leads_by_age(self) -> list:
        return self.db.execute(
            select(Lead.age, func.count(Lead.id))
            .group_by(Lead.age)
            .order_by(Lead.age)
        ).all()

    def get_leads_by_genre(self) -> list:
        return self.db.execute(
            select(Lead.genre, func.count(Lead.id))
            .group_by(Lead.genre)
        ).all()
    
    def get_leads_by_height(self) -> list:
        return self.db.execute(
            select(Lead.height)
        ).scalars().all()
        
    def get_all_leads(self) -> list :
        return self.db.execute(
            select(Lead)
        ).scalars().all()