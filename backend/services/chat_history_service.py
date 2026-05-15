from repository.chat_history_repository import ChatHistoryRepository
from services.gpt_service import GptService
from models.chat_model import ChatHistory
class ChatHistoryService :
    def __init__(self, repo: ChatHistoryRepository, gpt: GptService) :
        self.repo = repo
        self.gpt = gpt
        
    def flow(self, prompt: str) :
        chat = self.get_response(prompt)
        self.save_chat_int_history(chat)
        return chat
    
    def save_chat_int_history(self, chat: ChatHistory) :
        self.repo.save_chat(chat)
        return chat
    
    def get_response(self, prompt: str) -> ChatHistory:
        return self.gpt.bot_response(prompt)