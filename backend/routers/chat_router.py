from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_chat_history_service
from schemas.chat_history_schema import ChatResponse
from services.chat_history_service import ChatHistoryService

router = APIRouter(prefix="/chat", tags=["Chat defs"])

@router.post("/")
def create_requisition(prompt: str, service: ChatHistoryService = Depends(get_chat_history_service)) :
    return service.flow(prompt)