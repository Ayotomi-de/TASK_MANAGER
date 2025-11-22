# main.py
"""
MAIN MODULE
-----------
This program demonstrates the use of three core data structures:
1. Stack
2. Queue
3. Singly Linked List

A SIMPLE TASK MANAGER USES THEM AS:
- Stack → Undo system
- Queue → Process tasks in order
- Linked List → Keep full task history

This file follows software construction principles:
- Modular design (separate modules)
- High cohesion (each function does one thing)
- Low coupling (minimal module interdependence)
- Clear naming conventions
- Readable, commented code
"""

from stack import Stack                 
from queue import Queue                 
from linkedlist import SinglyLinkedList 


def demonstrate_stack_operations():
    """Demonstrates how the Stack handles UNDO operations."""
    print("\n--- STACK DEMONSTRATION (Undo System) ---")

    undo_stack = Stack()  # Create a Stack object

    # Push actions (simulate user actions)
    undo_stack.push("Added Task A")
    undo_stack.push("Added Task B")

    print("Undo actions available:", undo_stack.items)

    # Perform an undo operation
    last_action = undo_stack.pop()
    print("Undoing last action:", last_action)

    print("Remaining actions after undo:", undo_stack.items)


def demonstrate_queue_operations():
    """Demonstrates how the Queue processes tasks in FIFO order."""
    print("\n--- QUEUE DEMONSTRATION (Task Processing) ---")

    task_queue = Queue()  # Create a Queue object

    # Add tasks
    task_queue.enqueue("Task 1: Clean room")
    task_queue.enqueue("Task 2: Write code")
    task_queue.enqueue("Task 3: Read book")

    print("Tasks waiting:", task_queue.items)

    # Process the first task
    processed = task_queue.dequeue()
    print("Processing:", processed)

    print("Remaining tasks:", task_queue.items)


def demonstrate_linkedlist_operations():
    """Demonstrates how the Linked List stores task history."""
    print("\n--- LINKED LIST DEMONSTRATION (Task History) ---")

    history = SinglyLinkedList()  # Create LinkedList object

    # Insert several completed tasks
    history.insert_tail("Task A completed")
    history.insert_tail("Task B completed")
    history.insert_tail("Task C completed")

    print("Full task history:")
    history.display()  # Display entire list


def main():
    """Main controller of the program."""
    print("==== SIMPLE TASK MANAGER APPLICATION ====")

    demonstrate_stack_operations()
    demonstrate_queue_operations()
    demonstrate_linkedlist_operations()

    print("==== END OF DEMO ====")


if __name__ == "__main__":
    main()
