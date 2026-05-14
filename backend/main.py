from fastapi import FastAPI
from routers.goal_router import router as goal_router
from routers.user_router import router as user_router
from routers.lead_router import router as lead_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(goal_router)
app.include_router(user_router)
app.include_router(lead_router)
