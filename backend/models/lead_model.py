from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Lead(Base) :
    __tablename__ = "leads"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    genre: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    height: Mapped[int] = mapped_column()
