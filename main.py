import time
import json
import os
import random

FILE_NAME = "tasks.json"

#Load all task in json
def load_tasks():
    # Create file if it doesn't exist
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([], file)

        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            content = file.read().strip()

            # Handle empty file
            if not content:
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted. Resetting task list.")
        return []

#Save task in json file
def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def main():
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Search for task")
        print("2. Create new task")
        print("3. Delete a task")
        print("4. Update a task")
        print("5. View all tasks")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        match choice:
            case 1:
                searchTask()

            case 2:
                createTask()

            case 3:
                deleteTask()

            case 4:
                updateTask()

            case 5:
                viewTasks()

            case 6:
                print("Exiting...")
                time.sleep(2)
                break

            case _:
                print("Please input the right choice!")

#Create new task
def createTask():
    tasks = load_tasks()

    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    taskId = random.randint(10000, 99999)
    print(taskId)

    if not title or not description:
        print("Title and description cannot be empty!")
        return

    # Prevent duplicate titles
    for task in tasks:
        if task["taskId"] == taskId:
            print("Task already exists!")
            return

    task = {
        "title": title,
        "description": description,
        "taskId": taskId
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Successfully created new task!")
    time.sleep(1)

#search for the id
def searchTask():
    tasks = load_tasks()

    keywordId = int(input("Enter task name to search: "))

    found = False
    for task in tasks:
       if keywordId == task["taskId"]:
            print("\nTask Found:")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"taskId: {task['taskId']}")
            found = True

    if not found:
        print("No matching task found.")
        print(tasks["taskId"])
#Delete task
def deleteTask():
    tasks = load_tasks()

    title = input("Enter task id to delete: ").strip().lower()

    updated_tasks = [
        task for task in tasks
        if task["taskId"].lower() != taskId
    ]

    if len(updated_tasks) == len(tasks):
        print("Task not found.")
    else:
        save_tasks(updated_tasks)
        print("Task deleted successfully!")

#Update task
def updateTask():
    tasks = load_tasks()

    title = input("Enter task title to update: ").strip().lower()

    for task in tasks:
        if task["title"].lower() == title:

            new_title = input("Enter new title: ").strip()
            new_description = input("Enter new description: ").strip()
            new_id = int(input("Enter new id: "))

            if new_title:
                task["title"] = new_title

            if new_description:
                task["description"] = new_description
            if new_id:
                task["taskId"] = new_id

            save_tasks(tasks)

            print("Task updated successfully!")
            return

    print("Task not found.")


#Print all task
def viewTasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    print("\n===== TASK LIST =====")

    for index, task in enumerate(tasks, start=1):
        print(f"\nTask {index}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"id: {task['taskId']}")


if __name__ == "__main__":
    main()