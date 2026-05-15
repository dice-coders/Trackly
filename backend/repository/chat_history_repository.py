from sqlalchemy.orm import Session
from models.chat_model import ChatHistory
class ChatHistoryRepository:
    def __init__(self, db: Session) :
        self.db = db
        
    def save_chat(self, chat: ChatHistory) :
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)