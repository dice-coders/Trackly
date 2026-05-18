import os, json
from openai import OpenAI
from dotenv import load_dotenv
from models.chat_model import ChatHistory
from services.dashboard_service import DashboardService
load_dotenv()

class GptService:
    def __init__(self, service: DashboardService) :
        self.gpt = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))
        self.service = service
        
        
    def bot_response(self, prompt: str, history: list = []) -> ChatHistory:
        contexto = f"""
        dados filtrados para analise : {json.dumps(self.service.get_dashboard(), ensure_ascii=False, indent=2)}.
        leads brutos : {json.dumps(self.service.get_lead_data(), ensure_ascii=False, indent=2)}
        historico de conversa: {json.dumps(history, ensure_ascii=False, indent=2)}
        Pergunta do usuário : {prompt}.
        """

        requisicao = ChatHistory(
            prompt = prompt,
            message = self.gpt.chat.completions.create(
                model="gemini-2.5-flash",
                messages=[
                    {"role": "system", "content": os.getenv("INSTRUCTIONS")},
                    {"role": "user", "content": contexto}
                        ]
            ).choices[0].message.content
        )
        return requisicao
        
        