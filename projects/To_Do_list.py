tasks = []

while True:
    print("\n------- Menu -------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Search Task")
    print("5. Update Task")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added!")

        case 2:
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i in range(len(tasks)):
                    print(f"{i+1}. {tasks[i]}")

        case 3:
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num-1)
                    print(f"Task '{removed}' removed.")
                else:
                    print("Invalid task number!")

        case 4:
            search = input("Enter task to search: ")
            if search in tasks:
                print("Task found at position:", tasks.index(search) + 1)
            else:
                print("Task not found.")

        case 5:
            if len(tasks) == 0:
                print("No tasks to update.")
            else:
                num = int(input("Enter task number to update: "))
                if 1 <= num <= len(tasks):
                    new_task = input("Enter new task: ")
                    tasks[num-1] = new_task
                    print("Task updated successfully!")
                else:
                    print("Invalid task number!")

        case 6:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Try again.")