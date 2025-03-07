# Add_task.py

def add_task(tasks, task_name):
    task = {
        'name': task_name,
        'completed': False
    }
    tasks.append(task)
    return tasks

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "✘"
            print(f"{idx}. {task['name']} [{status}]")
