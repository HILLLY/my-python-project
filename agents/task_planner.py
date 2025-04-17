def plan_tasks(tasks):
    # You can use AI-based reordering later. For now, keep it simple.
    return sorted(tasks, key=lambda x: x.lower())
def plan_tasks(tasks: list[str]) -> list[str]:
    """
    Simulate planning by adding time estimates or grouping.
    """
    return [f"Plan for: {task} → Estimated time: 1 hour" for task in tasks]
