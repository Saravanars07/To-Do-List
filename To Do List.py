def todo_list():
    tasks = []
    while True:
        print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice=input("Choose an option: ")
        if choice=='1':
            task=input("Enter a Task: ")
            tasks.append(task)
            print("Task added\n")
            
        elif choice=='2':
            if tasks:
                print("Your Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                print()
            else:
                print("No tasks entered yet.\n")
                
        elif choice=='3':
            if tasks:
                remove_input=input("Enter task number or task name remove: ")
                # Try to remove by number
                try:
                    task_num=int(remove_input)
                    if 1<=task_num<=len(tasks):
                        removed=tasks.pop(task_num-1)
                        print(f"Removed by number:{removed}\n")
                    else:
                        print("Invalid task number\n")
                        
                except ValueError:
                    # Try to remove by name
                    if remove_input in tasks:
                        tasks.remove(remove_input)
                        print(f"Removed by name:{remove_input}\n")
                    else:
                        print("Task not found\n")
            else:
                print("No tasks to remove.\n")
                
        elif choice=='4':
            print("Good Bye!")
            break
        
        else:
            print("Invalid choice\n")

todo_list()
