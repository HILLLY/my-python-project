import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.task_breaker import break_goal_into_tasks

goal = "Build a full-stack blog platform"
tasks = break_goal_into_tasks(goal)

for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")

from agents.task_breaker import break_goal_into_tasks
from agents.task_planner import plan_tasks
from agents.task_executor import execute_task

def main():
    print("🧠 Welcome to TaskGenie!")
    goal = input("👉 Enter your software project goal: ")

    print("\n📌 Breaking down the goal into tasks...")
    tasks = break_goal_into_tasks(goal)

    print("\n📋 Raw Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    print("\n📐 Planning task order...")
    planned_tasks = plan_tasks(tasks)

    print("\n✅ Planned Tasks:")
    for i, task in enumerate(planned_tasks, 1):
        print(f"{i}. {task}")

    print("\n🚀 Executing tasks (mock mode):")
    for task in planned_tasks:
        execute_task(task)

if __name__ == "__main__":
    main()
