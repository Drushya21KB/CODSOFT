# todo.py

def display_tasks(tasks):
    if not tasks:
        print("No tasks in your To-Do list.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added!")
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            display_tasks(tasks)
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
