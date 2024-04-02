import os

# Function to display the to-do list
def display_todo_list(todo_list):
    if not todo_list:
        print("Your Todo_List : []")
    else:
        for index, task in enumerate(todo_list):
            print(f"{index + 1}. {task}")


# Function to add a task to the to-do list
def task_add(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")


# Function to remove a task from the to-do list
def task_remove(todo_list, task_number):
    if 1 <= task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task number.")


# Main function
def main():
    todo_list = []
    print("To-Do List:")
    display_todo_list(todo_list)

    while True:
        os.system("clear" if os.name == "posix" else "cls")  # Clear the console
    #    print("To-Do List:")
    #    display_todo_list(todo_list)

        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Display Task")
        print("4. Quit")

        option = input("Enter your choice: ")

        if option == "1":
            task = input("Enter the task: ")
            task_add(todo_list, task)
        elif option == "2":
            task_number = int(input("Enter the task number to remove: "))
            task_remove(todo_list, task_number)
        elif option == "3":
            print("To-Do List:")
            display_todo_list(todo_list)
        elif option == "4":
            print("Quiting the To-Do List Program.")
            display_todo_list(todo_list)
            print("<---- Thank you for using ---->")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
