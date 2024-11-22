tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def delete_task(task_index):
    if 0 < task_index <= len(tasks):
        tasks.pop(task_index - 1)
    else:
        print("Invalid index.")

if __name__ == "__main__":
    while True:
        print("\n1. Add task")
        print("\n2. View tasks")
        print("\n3. Delete task")
        print("\n4. Exit \n")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to delete: "))
            delete_task(task_index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
