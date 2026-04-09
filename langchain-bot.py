import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3:4b", temperature=0.9)

parser = StrOutputParser()


def chat():
    chat_history = [
        {
            "role": "system",
            "content": "You are a helpful chatbot.Be concise and accurate.",
        },
    ]


  print("Type 'exit' to quit.\n")

  while True:
    user_input = input("You:").strip()
    if user_input.lower() == "exit":
        break

    chat_history.append({"role": "user", "content": user_input})

    prompt = ChatPromptTemplate.from_messages(chat_history)

    chain = prompt | llm | parser

    response = chain.invoke({})

    print(f"Bot: {response}\n")

    chat_history.append({"role": "assistant", "content": response})

    print("-" * 50)

chat()
