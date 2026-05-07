from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text

import database as db

class Goal(db.Base) :
    __tablename__ = "goals"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(120))
    description: Mapped[str] = mapped_column(Text)
    state: Mapped[str] = mapped_column(String(20))
    