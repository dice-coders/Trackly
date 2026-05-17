from pydantic import BaseModel, ConfigDict, Field

class ChatReceive(BaseModel) :
    prompt: str
    model_config = ConfigDict(from_attributes=True)
    
class ChatResponse(BaseModel) :
    message: str
    model_config = ConfigDict(from_attributes=True)