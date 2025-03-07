# cli.py
import sys
from Add_task import add_task, view_tasks
from manage_task import complete_task, delete_task, load_tasks, save_tasks

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions: add | view | complete | delete | exit")
        command = input("Enter a command: ").strip().lower()

        if command == "add":
            task_name = input("Enter the task: ")
            tasks = add_task(tasks, task_name)
            print("Task added successfully.")
        
        elif command == "view":
            view_tasks(tasks)

        elif command == "complete":
            index = int(input("Enter task number to complete: ")) - 1
            complete_task(tasks, index)
            print("Task marked as completed.")
        
        elif command == "delete":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
            print("Task deleted successfully.")
        
        elif command == "exit":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        
        else:
            print("Invalid command! Please try again.")

if __name__ == "__main__":
    main()
