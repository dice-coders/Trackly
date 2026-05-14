from sqlalchemy.orm import Session
import repository.dashboard_repository as repo

def get_dashboard(db: Session) -> dict:
    return {
        "total_leads": repo.get_total_leads(db),
        "leads_by_age": [
            {"age": row[0], "count": row[1]}
            for row in repo.get_leads_by_age(db)
        ],
        "leads_by_genre": [
            {"genre": row[0] or "undefined", "count": row[1]}
            for row in repo.get_leads_by_genre(db)
        ],
    }