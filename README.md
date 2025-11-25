# SIMPLE TASK MANAGER (Python Project)

This project is a simple **Task Manager Application** built for the SEN 306 – Software Construction lab assessment.  
It demonstrates the real-life use of three major data structures:

- **Stack** → Handles undo actions  
- **Queue** → Handles task processing in order  
- **Singly Linked List** → Stores completed task history  

The application is **interactive**, meaning users can enter their own actions and tasks through the terminal while the system uses all three data structures behind the scenes.

---

## Project Structure


TASK_MANAGER/
│
├── stack.py              # Stack implementation (LIFO)
├── queue.py              # Queue implementation (FIFO)
├── linkedlist.py         # Singly Linked List implementation
├── main.py               # Interactive application (uses all structures)
└── README.md             # Project documentation

```

# Project Overview

This application shows how Stack, Queue, and Linked List can work together inside a simple, real-life scenario:

### ✔ Stack → Used for UNDO  
Example:  
- “Added Task A”  
- “Added Task B”  
User can undo the last action.

### ✔ Queue → Used for Processing Tasks  
Example:  
- Task 1: Clean room  
- Task 2: Write code  
User can process tasks in the order they were added.

### ✔ Linked List → Used for Task History  
Every completed task is recorded in a linked list.

---

# Interactive Features (Dynamic main.py)

When you run `main.py`, you get a menu like this:

```

1. Add an action (Stack)
2. Undo last action (Stack)
3. Add a task (Queue)
4. Process next task (Queue)
5. Add completed task (Linked List)
6. View task history (Linked List)
7. Exit

```

This allows users to enter their own values instead of fixed demo data.

---

# ⚙️ How to Run the Program

1. Open the folder in VS Code or any terminal
2. Run:

```

python main.py

```

3. Follow the on-screen instructions.

No frontend is required.  
Everything happens in the terminal using your 3 data structures.

---

# 🧠 Software Construction Principles Applied

### **Modular Design**
Each data structure lives in its own module (`stack.py`, `queue.py`, `linkedlist.py`).

### **High Cohesion**
Every class and method performs one clear function only.

### **Low Coupling**
`main.py` interacts with the data structures through method calls only.

### **Meaningful Naming**
Variables and functions have clear, descriptive names.

### **Readable Code**
- Proper indentation  
- Docstrings  
- Inline comments  
- Simple structure that any reader can follow  

---

# Group Work Section

A total of 10 members contributed to the project with at least 3 members contributing in a module.


# Summary

This project is:
- Simple  
- Modular  
- Interactive  
- Easy to understand  
- Fully aligned with SEN 306 requirements  

It clearly demonstrates how Stack, Queue, and Linked List can be applied in a real-life scenario using clean Python code.

---

### Built for SEN 306 – Software Construction  
```
