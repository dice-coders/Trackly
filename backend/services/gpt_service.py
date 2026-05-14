import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class GptService:
    def __init__(self) :
        self.gpt = OpenAI(api_key=os.getenv("API_KEY"))
        
    def prompt_receive(self, question: str) -> str:
        pass
    
    def message_generation(self, input: str) :
        return self.gpt.responses.create(
            model="gpt-5.2",
            instructions="Você é um analista de dados e metas",
            input=input
        )
    
    def data_analysis() :
        pass
        
        