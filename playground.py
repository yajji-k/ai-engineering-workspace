import time, asyncio
from app.application.chat.chat_service import ChatService
from app.application.extraction.extraction_service import ExtractionService
from langchain_core.messages import HumanMessage, AIMessage

def test_chat() -> None:
    service = ChatService()

    messages = []

    while True:
        user_input = input("User Chat > ")
        messages.append(HumanMessage(content = user_input))
        
        response = service.chat(messages=messages)

        print("\n===== Response =====\n")
        print(response)
        print("\n====================\n")
        
        messages.append(AIMessage(content=response))

async def test_achat() -> None:
    service = ChatService()

    messages = []

    while True:
        user_input = input("User Chat > ")
        messages.append(HumanMessage(content = user_input))
        
        response = await service.achat(messages=messages)

        print("\n===== Response =====\n")
        print(response)
        print("\n====================\n")
        
        messages.append(AIMessage(content=response))
        
def test_stream() -> None:
    service = ChatService()
    messages = []
    
    while True:
        user_input = input("User Chat > ")
        messages.append(HumanMessage(content = user_input))
        
        response = ""

        for chunk in service.stream(messages=messages):
            # print(chunk.content, end = "", flush=True)
            response += chunk.content
            
            for char in chunk.content:
                print(char, end="", flush=True)
                time.sleep(0.03)  # only added to simulate stream cause it super fast remove it will make no difference
            
        print("\n\n====================\n")

        messages.append(AIMessage(content=response))

async def test_astream() -> None:
    service = ChatService()
    messages = []
    
    while True:
        user_input = input("User Chat > ")
        messages.append(HumanMessage(content = user_input))
        
        response = ""

        async for chunk in service.astream(messages=messages):
            # print(chunk.content, end = "", flush=True)
            response += chunk.content
            
            for char in chunk.content:
                print(char, end="", flush=True)
                await asyncio.sleep(0.03)  # only added to simulate stream cause it super fast remove it will make no difference
                
        print("\n\n====================\n")

        messages.append(AIMessage(content=response))
        
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

    # Future experiments:
    # test_streaming()
    # test_prompt_template()
    # test_structured_output()
    # test_tools()
    # test_rag()
    # test_agent()
    # test_langgraph()


if __name__ == "__main__":
    asyncio.run(main())