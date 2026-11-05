def show_menu():
    print("Todo List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.\n")
        return
    

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "DONE" if task["completed"] else "PENDING"
        print(f"{index}. {task['title']} [{status}]")

def add_task(tasks):
    '''allows the user to conitnously add tasks to the list until they choose to stop'''
    print("\n ----Adding Tasks----")
    print("(Type 'done' when you are finished adding tasks.)")
    while True:
        title = input("Enter a task name: ").strip()

        if title.lower() == "done":
            print("Finished adding tasks.")
            break

        # Add the task if it's not empty
        if title:
            tasks.append({"title":title, "completed":  False})
            print(f" '{title},' added to your to-do list.")
        else:
            print("Task name cannot be empty. Try again or type 'done' to exixt")
    

def mark_complete(tasks):
    ''' marks a specific task as completed based on its indec'''
    view_tasks(tasks)
    if not tasks:
        return 

    try:
        choice = int(input("Enter the task number to mark as completed: "))
        if 1<= choice <=len(tasks):
            tasks[choice -1]["completed"] = True
            print(f"! Task '{tasks[choice - 1]['title']}' marked as completed.")
        else:
            print("! Invalid task number.")
    except ValueError:
        print("! Please enter a valid task number.")


def delete_task(tasks):
    '''removes a specific task from the list'''
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("Enter the task number to remove: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            print(f"! Task '{removed_task['title']}' removed from your to-do list.")
        else:
            print("! Invalid task number.")

    except ValueError:
        print("! Please enter a valid task number.")


def main():
    # A list of dictionaries to store task data structurally
    tasks=[]

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print(" Goodbye!!! Thanks for using the To-Do List app.")
            break
        else:
            print("Invalid choice.Please pick a number between 1 and 5.")



if __name__ == "__main__":
    main()

        
