"""Task 1: To-Do List (command-line) - tasks are saved to tasks.json."""
import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
        return
    print("\n--- Your To-Do List ---")
    for i, t in enumerate(tasks, 1):
        mark = "X" if t["done"] else " "
        print(f"{i}. [{mark}] {t['title']}")


def get_index(tasks, prompt):
    try:
        n = int(input(prompt))
        if 1 <= n <= len(tasks):
            return n - 1
    except ValueError:
        pass
    print("Invalid task number.")
    return None


def main():
    tasks = load_tasks()
    while True:
        print("\n==== TO-DO LIST ====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark task as done")
        print("5. Delete task")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter new task: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                i = get_index(tasks, "Task number to update: ")
                if i is not None:
                    new = input("New title: ").strip()
                    if new:
                        tasks[i]["title"] = new
                        save_tasks(tasks)
                        print("Task updated.")
        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                i = get_index(tasks, "Task number to mark done: ")
                if i is not None:
                    tasks[i]["done"] = True
                    save_tasks(tasks)
                    print("Task marked as done.")
        elif choice == "5":
            show_tasks(tasks)
            if tasks:
                i = get_index(tasks, "Task number to delete: ")
                if i is not None:
                    removed = tasks.pop(i)
                    save_tasks(tasks)
                    print(f"Deleted: {removed['title']}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
