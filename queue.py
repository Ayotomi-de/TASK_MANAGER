"""
queue.py
This is a simple Queue implementation using a Python list.
FIFO = First In, First Out
"""

class Queue:
    """A basic queue using a list to store items."""

    def __init__(self):
        # Create an empty list that will hold our queue items
        self.items = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)  # remove first item

    def peek(self):
        """Look at the front item without removing it."""
        if self.is_empty():
            return None
        return self.items[0]  # first item is always at index 0

    def is_empty(self):
        """Check if the queue has no items."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items currently in the queue."""
        return len(self.items)

    def __str__(self):
        """Return a clear, readable string showing queue contents."""
        result = "Queue(front → rear): "
        
        # If queue has no items
        if self.items == []:
            return result + "EMPTY"
        
        # Add each item and an arrow
        for item in self.items:
            result += str(item) + " -> "
        
        # Show the end of the queue
        return result + "None"
