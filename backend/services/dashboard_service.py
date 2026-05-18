from repository.dashboard_repository import DashboardRepository

class DashboardService :
    def __init__(self, repo: DashboardRepository) :
        self.repo = repo
        
    def get_dashboard(self) -> dict:
        return {
            "total_leads": self.repo.get_total_leads(),
            "leads_by_age": [
                {"age": row[0], "count": row[1]}
                for row in self.repo.get_leads_by_age()
            ],
            "leads_by_genre": [
                {"genre": row[0] or "undefined", "count": row[1]}
                for row in self.repo.get_leads_by_genre()
            ],
            "lead_by_height": [
                {"height": row}
                for row in self.repo.get_leads_by_height()
            ]
        }
        
    def get_lead_data(self) -> dict :
        return {
            "lead": [
                {
                    "genre": lead.genre,
                    "age": lead.age,
                    "height": lead.height
                }
                for lead in self.repo.get_all_leads()
                    ]
                }