from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from database import Base
from datetime import date
class ChatHistory(Base) :
    __tablename__ = "chat_history"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    prompt: Mapped[str] = mapped_column(Text)
    message: Mapped[str] = mapped_column(Text)
    date_requisition: Mapped[date] = mapped_column(default=date.today)