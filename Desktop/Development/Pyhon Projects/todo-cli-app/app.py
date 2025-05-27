import json

def delete_task():
    global tasks
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f'Task "{removed["title"]}" deleted.')
            save_tasks()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
print ("Welcome to You To-Do List App")

tasks = []
load_tasks()

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{index}. {task['title']} [{status}]")

def add_task():
    global tasks
    task_name = input ("Enter the task: ")
    task = {"title": task_name, "done": False}
    tasks.append(task)
    print (f'Task "{task_name}" added.')
    save_tasks()

def complete_task():
    global tasks
    if not tasks:
        print("No tasks to complete.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f'Task "{tasks[task_num - 1]["title"]}" marked as complete.')
            save_tasks()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print ("\nPlease choose an option:")
    print ("1. Add Task")
    print ("2. View Tasks")
    print ("3. Complete Task")
    print ("4. Delete Task")
    print ("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice =="3":
        complete_task()
    elif choice =="4":
        delete_task()
    elif choice =="5":
        print("You chose: Goodbye")            
        break
    else:
        print ("Invalid choice. Please try again.")    
