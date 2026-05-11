from fastapi import FastAPI
from routers.goal_router import router as goal_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(goal_router)

