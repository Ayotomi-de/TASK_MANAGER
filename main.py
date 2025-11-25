# main.py
"""
MAIN MODULE
-----------
Interactive Task Manager that demonstrates:
- Stack for undo actions
- Queue for processing tasks
- Singly Linked List for task history

This file follows:
- Modular design
- High cohesion (each function does ONE thing)
- Low coupling (imports interact through clean methods only)
- Clear naming conventions
- Well-documented, readable code
"""

from stack import Stack
from queue import Queue
from linkedlist import SinglyLinkedList


def handle_stack(undo_stack):
    #Allows the user to push or undo actions using a Stack.
    print("\n--- STACK (UNDO SYSTEM) ---")
    while True:
        print("\n1. Add an action")
        print("2. Undo last action")
        print("3. View undo stack")
        print("4. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            action = input("Enter action to store: ")
            undo_stack.push(action)
            print(f"[STACK] Stored: {action}")

        elif choice == "2":
            if undo_stack.is_empty():
                print("No actions to undo.")
            else:
                undone = undo_stack.pop()
                print(f"Undo successful → {undone}")

        elif choice == "3":
            print("Current undo stack:", undo_stack.items)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")


def handle_queue(task_queue):
    #Allows the user to add and process tasks using a Queue.
    print("\n--- QUEUE (TASK PROCESSING) ---")
    while True:
        print("\n1. Add task")
        print("2. Process next task")
        print("3. View waiting tasks")
        print("4. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            task_queue.enqueue(task)
            print(f"[QUEUE] Task added: {task}")

        elif choice == "2":
            if task_queue.is_empty():
                print("No tasks to process.")
            else:
                done = task_queue.dequeue()
                print(f"Processed → {done}")

        elif choice == "3":
            print("Tasks waiting:", task_queue.items)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")


def handle_linkedlist(history):
    #Allows the user to add completed tasks to a Linked List and view history.
    print("\n--- LINKED LIST (TASK HISTORY) ---")
    while True:
        print("\n1. Add completed task")
        print("2. View full task history")
        print("3. Return to main menu")

        choice = input("Choose: ")

        if choice == "1":
            completed = input("Completed task name: ")
            history.insert_tail(completed)
            print(f"[HISTORY] Added: {completed}")

        elif choice == "2":
            print("Task History:")
            history.display()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Try again.")


def main():
    # Main program — connects Stack, Queue, and Linked List together.
    print("==== INTERACTIVE TASK MANAGER ====")

    undo_stack = Stack()
    task_queue = Queue()
    history = SinglyLinkedList()

    while True:
        print("\nMAIN MENU")
        print("1. Undo System (Stack)")
        print("2. Task Processing (Queue)")
        print("3. Task History (Linked List)")
        print("4. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            handle_stack(undo_stack)

        elif choice == "2":
            handle_queue(task_queue)

        elif choice == "3":
            handle_linkedlist(history)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.")

    print("==== END OF APPLICATION ====")


if __name__ == "__main__":
    main()
