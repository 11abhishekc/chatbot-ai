import os
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.llms.ollama import Ollama


llm = Ollama(model="gemma3:4b", temperature=0.9)


def chat():
    chat_history = [
        ChatMessage(
            role=MessageRole.SYSTEM,
            content="You are a helpful chatbot. Be concise and accurate.",
        )
    ]

    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break

        # ✅ inside loop
        chat_history.append(ChatMessage(role=MessageRole.USER, content=user_input))

        response = llm.chat(chat_history)

        # ⚠️ response is an object → extract text
        print(f"Bot: {response.message.content}\n")

        chat_history.append(
            ChatMessage(role=MessageRole.ASSISTANT, content=response.message.content)
        )

        print("-" * 50)


chat()
