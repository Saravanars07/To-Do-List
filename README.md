# To-Do-List
A simple command-line To-Do List manager written in Python.
You can add tasks, view your list, and remove tasks by either their number or name.

***Features***
  - Add Task: Add a new task to your list.
  - View Tasks: Display all your current tasks.
  - Remove Task: Remove a task by its number or by its exact name.
  - Exit: Quit the application.

***How to Run***
  1. Make sure you have Python installed (version 3.x recommended).
  2. Copy the code below into a file named ```To Do List.py```.
  3. Open your terminal or command prompt.
  4. Run the script:
     
     ```
     python To Do List.py
     ```
***Usage***

When you run the script, you’ll see a menu with four options:

```
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
```
  - To add a task: Enter 1 and type your task.
  - To view tasks: Enter 2 to see all tasks with their numbers.
  - To remove a task: Enter 3 and then enter either the task number (as shown in the list) or the exact task name.
  - To exit: Enter 4.

***Example***

```
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Choose an option: 1
Enter a Task: Buy groceries
Task added

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Choose an option: 2
Your Tasks:
1. Buy groceries

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Choose an option: 3
Enter task number or task name remove: 1
Removed by number: Buy groceries

```

***Code***

```
def todo_list():
    tasks = []
    while True:
        print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter a Task: ")
            tasks.append(task)
            print("Task added\n")
        elif choice == '2':
            if tasks:
                print("Your Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                print()
            else:
                print("No tasks entered yet.\n")
        elif choice == '3':
            if tasks:
                remove_input = input("Enter task number or task name remove: ")
                # Try to remove by number
                try:
                    task_num = int(remove_input)
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Removed by number: {removed}\n")
                    else:
                        print("Invalid task number\n")
                except ValueError:
                    # Try to remove by name
                    if remove_input in tasks:
                        tasks.remove(remove_input)
                        print(f"Removed by name: {remove_input}\n")
                    else:
                        print("Task not found\n")
            else:
                print("No tasks to remove.\n")
        elif choice == '4':
            print("Good Bye!")
            break
        else:
            print("Invalid choice\n")

todo_list()

```

***License***

This project is open source and free to use.
