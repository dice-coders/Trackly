from database import Base
from sqlalchemy.orm import Mapped, mapped_column

#Define as variações e as constraints do banco de dados (e define o nome)
class Lead(Base) :
    __tablename__ = "leads"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    genre: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    height: Mapped[int] = mapped_column()
