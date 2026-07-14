from app.agents.support_agent import create_support_agent
from app.memory.history import ConversationHistoryManager


class ChatService:
    def __init__(self):
        self.agent = create_support_agent()
        self.history_manager = ConversationHistoryManager()

    def send_message(self, conversation_id: str, user_input: str):
        # Get (or create) the conversation history
        history = self.history_manager.get_history(conversation_id)

        # Store the user's message
        history.add_user_message(user_input)

        # Invoke the agent with the full conversation history
        response = self.agent.invoke(
            {
                "messages": history.messages
            }
        )

        # Store the assistant's final response
        final_message = response["messages"][-1]
        history.add_message(final_message)

        return response