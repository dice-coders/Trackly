from pydantic import BaseModel, ConfigDict, Field

class ChatReceive(BaseModel) :
    prompt: str
    model_config = ConfigDict(from_attributes=True)
    
class ChatResponse(BaseModel) :
    response: str
    model_config = ConfigDict(from_attributes=True)