from sqlalchemy.orm import Session
from models.lead_model import Lead

class LeadRepository :
    def __init__(self, db: Session) :
        self.db = db
        
    def lead_add(self, lead: Lead) :
        self.db.add(lead)
        self.db.commit()
        self.db.refresh(lead)
        return lead