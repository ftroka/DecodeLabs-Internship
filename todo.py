tasks = []
next_id = 1


def add_task():
    global next_id

    task = input("Enter the task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append({
        "id": next_id,
        "title": task,
        "completed": False
    })

    next_id += 1
    print(" Task added successfully!")


def view_tasks():

    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n========== YOUR TASKS ==========")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'ID: {task["id"]} | [{status}] {task["title"]}')

    print(f"\nTotal Tasks: {len(tasks)}")


def mark_completed():

    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("\nEnter task ID to mark as completed: "))

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(" Task marked as completed!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():

    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("\nEnter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print(" Task deleted successfully!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Please enter a valid number.")


def clear_tasks():

    if not tasks:
        print("No tasks available.")
        return

    confirm = input("Are you sure you want to clear all tasks? (y/n): ")

    if confirm.lower() == "y":
        tasks.clear()
        print("All tasks cleared.")
    else:
        print("Operation cancelled.")


while True:

    print("\n==============================")
    print("      TO-DO LIST MENU")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Clear All Tasks")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        mark_completed()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        clear_tasks()

    elif choice == "6":
        print("\nThank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")