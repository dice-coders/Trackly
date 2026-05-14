from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from datetime import date

#Define as variações e as constraints do banco de dados (e define o nome)
class User(Base) :
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(120))
    number: Mapped[str] = mapped_column(String(11))
    address: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column()
    date_creation: Mapped[date] = mapped_column(default=date.today)
    hash: Mapped[str] = mapped_column(String(128))
