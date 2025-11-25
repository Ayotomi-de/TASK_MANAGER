# SIMPLE TASK MANAGER (Python Project)

This project is a simple **Task Manager Application** built for the SEN
306 -- Software Construction lab assessment.
It demonstrates the real-life use of three major data structures:

-   **Stack** -- Handles undo actions
-   **Queue** -- Handles task processing in order
-   **Singly Linked List** -- Stores completed task history

The application is **interactive**, allowing users to enter their own
actions and tasks through the terminal while the system uses all three
data structures behind the scenes.

------------------------------------------------------------------------

## Project Structure

    TASK_MANAGER/
    │
    ├── stack.py              # Stack implementation (LIFO)
    ├── queue.py              # Queue implementation (FIFO)
    ├── linkedlist.py         # Singly Linked List implementation
    ├── main.py               # Interactive application (uses all structures)
    └── README.md             # Project documentation

------------------------------------------------------------------------

# Project Overview

This application shows how the Stack, Queue, and Linked List structures
can work together in a real-life scenario:

### 1. Stack -- Undo System

Used to reverse the last action performed.
Example actions:
- Added Task A
- Added Task B

Users can undo the most recent action using the stack.

### 2. Queue -- Task Processing

Tasks are processed in the exact order they were added.
Example queue:
- Task 1: Clean room
- Task 2: Write code

Users process tasks one at a time following the FIFO rule.

### 3. Linked List -- Task History

Every completed task is recorded in a linked list, forming a clean,
ordered history of all tasks done.

------------------------------------------------------------------------

# Interactive Features (Dynamic main.py)

Running `main.py` displays an interactive menu:

    1. Add an action (Stack)
    2. Undo last action (Stack)
    3. Add a task (Queue)
    4. Process next task (Queue)
    5. Add completed task (Linked List)
    6. View task history (Linked List)
    7. Exit

Users can provide inputs directly from the terminal, making the
application dynamic and practical.

------------------------------------------------------------------------

# How to Run the Program

1.  Open the project folder in VS Code or any terminal.\
2.  Run the following command:

```{=html}
<!-- -->
```
    python main.py

3.  Follow the on-screen options to interact with the system.

No frontend or GUI is required.
The entire application runs in the terminal using the three implemented
data structures.

------------------------------------------------------------------------

# Software Construction Principles Applied

### Modular Design

Each data structure is implemented in its own module.

### High Cohesion

Every class and method focuses on a single responsibility.

### Low Coupling

`main.py` interacts with the structures only through exposed methods,
not their internal implementations.

### Meaningful Naming

All names clearly describe their purpose.

### Readable Code

-   Proper indentation
-   Docstrings
-   Inline comments
-   Organized logic

------------------------------------------------------------------------

# Group Work Section

A total of 10 members contributed to this project, with at least 3
members participating in each module.

------------------------------------------------------------------------

# Summary

This project is:

-   Simple
-   Modular
-   Interactive
-   Beginner-friendly
-   Fully aligned with SEN 306 requirements

It demonstrates how Stack, Queue, and Linked List structures are used in
a real-life task management scenario with clean, well-documented Python
code.

------------------------------------------------------------------------

### Built for SEN 306 -- Software Construction
