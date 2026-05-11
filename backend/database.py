from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine 


class Base(DeclarativeBase) :
    pass

DATABASE_URL = "sqlite:///./trackly.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() :
    db = Session()
    try :
        yield db
    finally :
        db.close()