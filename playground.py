import time, asyncio
from app.application.chat.chat_service import ChatService
from app.application.extraction.extraction_service import ExtractionService
from langchain_core.messages import HumanMessage, AIMessage
from app.domain.conversation import Conversation
from app.infrastructure.conversation import InMemoryConversationRepository
from app.application.conversation import ConversationService

def test_chat() -> None:
    conv_service = ConversationService()
    conversation = Conversation()

    respository = InMemoryConversationRepository()
    respository.save(conversation)
    
    while True:
        user_input = input("User Chat > ")
        
        response = conv_service.chat(
            conversation=conversation,
            user_input=user_input
        )

        print("\n===== Response =====\n")
        print(response)
        print("\n====================\n")

async def test_achat() -> None:
    conv_service = ConversationService()
    conversation = Conversation()

    respository = InMemoryConversationRepository()
    respository.save(conversation)
        
    while True:
        user_input = input("User Chat > ")
        response = await conv_service.achat(
            conversation=conversation,
            user_input=user_input
        )

        print("\n===== Response =====\n")
        print(response)
        print("\n====================\n")
        
def test_stream() -> None:
    service = ChatService()
    
    repository = InMemoryConversationRepository()
    
    conversation = Conversation()
    repository.save(conversation)
        
    while True:
        user_input = input("User Chat > ")
        conversation.add_message(HumanMessage(content = user_input))
        
        response = ""

        for chunk in service.stream(messages=conversation.messages):
            # print(chunk.content, end = "", flush=True)
            response += chunk.content
            
            for char in chunk.content:
                print(char, end="", flush=True)
                time.sleep(0.03)  # only added to simulate stream cause it super fast remove it will make no difference
            
        print("\n\n====================\n")

        conversation.add_message(AIMessage(content=response))

async def test_astream() -> None:
    service = ChatService()

    repository = InMemoryConversationRepository()
    
    conversation = Conversation()
    repository.save(conversation)
    
    while True:
        user_input = input("User Chat > ")
        conversation.add_message(HumanMessage(content = user_input))
        
        response = ""

        async for chunk in service.astream(messages=conversation.messages):
            # print(chunk.content, end = "", flush=True)
            response += chunk.content
            
            for char in chunk.content:
                print(char, end="", flush=True)
                await asyncio.sleep(0.03)  # only added to simulate stream cause it super fast remove it will make no difference
                
        print("\n\n====================\n")

        conversation.add_message(AIMessage(content=response))
        
def test_extraction():
    service = ExtractionService()

    result = service.extract(
        "Hi, my name is Yajnesh and I am 24 years old."
    )

    print(result)
    print(type(result))

async def main() -> None:
    mode = input("Mode (chat/stream): ").strip().lower()

    if mode == "chat":
        # test_chat()
        test_achat()
    elif mode == "stream":
        # test_stream()
        test_astream()
    elif mode == "extract":
        test_extraction()


if __name__ == "__main__":
    asyncio.run(main())