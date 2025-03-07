# manage_tasks.py
import json

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
