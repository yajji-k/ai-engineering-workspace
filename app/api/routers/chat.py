from fastapi import APIRouter, Depends

from app.api.schemas import ChatRequest, ChatResponse
from app.application.chat.chat_service import ChatService
from app.api.dependencies import get_chat_service
from fastapi.responses import StreamingResponse

router = APIRouter(tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service)
):
    response = service.chat(request.message)
    
    return ChatResponse(response=response)


@router.post("/async-chat", response_model=ChatResponse)
async def achat(
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service)
):
    response = await service.achat(request.message)
    
    return ChatResponse(response=response)

@router.post("/stream")
def stream(    
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service),
):
    return StreamingResponse(
        service.stream(request.message),
        media_type="text/plain",
    )
    
@router.post("/async-stream")
async def astream(
    request: ChatRequest,
    service: ChatService = Depends(get_chat_service),
):
    return StreamingResponse(
        service.astream(request.message),
        media_type="text/plain",
    )