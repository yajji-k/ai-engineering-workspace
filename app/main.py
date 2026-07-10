from fastapi import FastAPI

from app.api.routers.chat import router as chat_router

app = FastAPI(
    title="AI Engineering Workspace",
    version="0.1.0",
)

app.include_router(chat_router)