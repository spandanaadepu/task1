class TodoItem:
    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

class TodoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(TodoItem(task))
        print("Task added successfully!")

    def list_tasks(self):
        print("\nTodo List:")
        for index, todo in enumerate(self.todos, start=1):
            status = "Done" if todo.completed else "Pending"
            print(f"{index}. [{status}] {todo.task}")

    def mark_task_completed(self, index):
        if 1 <= index <= len(self.todos):
            self.todos[index - 1].completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 1 <= index <= len(self.todos):
            del self.todos[index - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: "))
            todo_list.mark_task_completed(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
