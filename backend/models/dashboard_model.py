from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

class Data(Base):
    __tablename__ = "data"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    total_leads: Mapped[int] = mapped_column()
    genre: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    height: Mapped[int] = mapped_column()
    date_creation: Mapped[date] = mapped_column(default=date.now)