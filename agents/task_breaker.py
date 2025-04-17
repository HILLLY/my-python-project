import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.schema import SystemMessage, HumanMessage

# Load environment variables
load_dotenv()

def break_goal_into_tasks(goal: str):
    llm = ChatOllama(model="tinyllama", temperature=0.3)
    messages = [
        SystemMessage(content="You are a helpful assistant that breaks down goals into actionable software development tasks."),
        HumanMessage(content=f"Break down the goal: '{goal}' into detailed steps.")
    ]
    response = llm.invoke(messages)
    tasks = response.content.strip().split("\n")
    return [task.strip("0123456789.:- ") for task in tasks if task.strip()]
