from sqlalchemy.orm import Session
from sqlalchemy import select
from models.chat_model import ChatHistory
from schemas.chat_history_schema import ChatResponse
class ChatHistoryRepository:
    def __init__(self, db: Session) :
        self.db = db
        
    def save_chat(self, chat: ChatHistory) :
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)
    
    def get_history(self) -> list :
        records = self.db.execute(
            select(ChatHistory)
        ).scalars().all()
        
        return [ChatResponse.model_validate(record).model_dump()
                for record in records
                ]
        