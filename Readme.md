

# Basic Crud in Python

A simple command-line task manager written in Python. The app lets you create,
search, update, delete, and view tasks that are saved in a local JSON file.

## What It Does

When you run `main.py`, the program opens an interactive menu:

```text
===== TASK MANAGER =====
1. Search for task
2. Create new task
3. Delete a task
4. Update a task
5. View all tasks
6. Exit
```

Tasks are stored in `tasks.json`. If the file does not exist, the program creates
it automatically with an empty task list.

## Features

- Create a new task with a title, description, and random task ID.
- Search for a task by its task ID.
- Update an existing task by matching its title.
- Delete a task.
- View all saved tasks.
- Save task data locally in JSON format.
- Handle an empty or missing `tasks.json` file.

## Requirements

- Python 3.10 or newer

The project uses Python's `match` statement, which requires Python 3.10+.

## How To Run

Open a terminal in the project folder and run:

```bash
python main.py
```

Then enter a menu number from `1` to `6`.

## Task Data Format

Each task is saved in `tasks.json` like this:

```json
{
    "title": "test",
    "description": "This is test only!",
    "taskId": 12345 // 5 digit number using random
}
```

The full file contains a list of task objects:

```json
[
    {
        "title": "test",
        "description": "This is test only!",
        "taskId": 23456 // 5 digit number using random
    }
]
```

## Main Functions

- `load_tasks()` loads tasks from `tasks.json`.
- `save_tasks(tasks)` writes the task list back to `tasks.json`.
- `createTask()` asks for task details and adds a new task.
- `searchTask()` searches for a task by ID.
- `deleteTask()` deletes a task.
- `updateTask()` updates a task's title, description, and ID.
- `viewTasks()` prints all saved tasks.
- `main()` displays the menu and runs the selected action.

## Notes

The app is still in progress. Some parts of the current code may need cleanup,
especially the delete task logic and some input validation. The main purpose of
the project is to practice Python basics, file handling, JSON storage, and
command-line menus.