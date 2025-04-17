from agents.task_breaker import break_goal_into_tasks
from agents.task_planner import plan_tasks
from agents.task_executor import execute_task
from agents.web_search import search_web

def handle_taskgenie_query(goal: str, use_web: bool = True):
    broken_tasks = break_goal_into_tasks(goal)
    plan = plan_tasks(broken_tasks)
    execution_results = [execute_task(task) for task in broken_tasks]

    trigger_keywords = ["research", "latest", "trending", "find", "explore", "current", "top"]
    if use_web and any(word in goal.lower() for word in trigger_keywords):
        research = search_web(goal)
    else:
        research = "No research needed for this goal."

    return {
        "goal": goal,
        "broken_tasks": broken_tasks,
        "plan": plan,
        "execution_results": execution_results,
        "research": research,
    }
