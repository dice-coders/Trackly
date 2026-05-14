from repository.lead_repository import LeadRepository
from schemas.lead_schemas import LeadReceive
from models.lead_model import Lead
class LeadService :
    def __init__(self, repo: LeadRepository) :
        self.repo = repo

    def receive_data(self, schema: LeadReceive) :
        lead = self.parse_receive_lead(schema)
        return self.repo.lead_add(lead)
    
    #Transforma o schema em objeto
    def parse_receive_lead(self, schema: LeadReceive) -> Lead:
        lead = Lead(
            genre = schema.genre,
            age = schema.age,
            height = schema.height
        )
        return lead
    