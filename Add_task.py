# Add_task.py

import json

def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    return tasks

def view_tasks(tasks):
    for index, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        print(f"{index + 1}. {task['task']} - [{status}]")