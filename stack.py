class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
        print(f"[STACK] Pushed: {item}")

    def pop(self):
        """Remove and return the top item."""
        if not self.is_empty():
            item = self.items.pop()
            print(f"[STACK] Popped: {item}")
            return item
        print("[STACK] Stack is empty.")
        return None

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Check if stack has no items."""
        return len(self.items) == 0

    def size(self):
        """Return number of elements in the stack."""
        return len(self.items)

    def display(self):
        """Show items from top to bottom."""
        if self.is_empty():
            print("[STACK] No items in stack.")
            return

        print("\n--- Stack (Top to Bottom) ---")
        for item in reversed(self.items):
            print(item)
        print("-----------------------------")


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Top item:", s.peek())
    print("Size:", s.size())
    s.display()

    s.pop()
    s.display()
