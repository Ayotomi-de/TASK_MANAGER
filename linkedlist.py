"""linkedlist.py
Singly linked list implementation for the assignment.
"""

class Node:
    """Represents a single node in a singly linked list."""
    def __init__(self, data):
        self.data = data      # value stored in the node
        self.next = None      # pointer to the next node


class SinglyLinkedList:
    """Simple implementation of a singly linked list with basic operations."""

    def __init__(self):
        self.head = None      # the head (first node) of the list

    def insert_head(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head   # new node points to current head
        self.head = new_node        # update head to new node

    def insert_tail(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)

        # If list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, walk to the end
        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node  # link last node to new node

    def find(self, value):
        """Return the first node whose data matches `value`.
        If not found, return None.
        """
        cur = self.head
        while cur:
            if cur.data == value:
                return cur
            cur = cur.next
        return None

    def delete_value(self, value):
        """Delete the first node with matching value.
        Return True if deletion succeeded, False otherwise.
        """
        cur = self.head
        prev = None

        while cur:
            if cur.data == value:
                # If deleting the head
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next  # bypass the node
                return True

            prev = cur
            cur = cur.next

        return False  # value not found

    def to_list(self):
        """Return a Python list containing all node data."""
        elements = []
        cur = self.head
        while cur:
            elements.append(cur.data)
            cur = cur.next
        return elements

    def __str__(self):
        """Return a readable string representation of the list."""
        return "LinkedList: " + " -> ".join(repr(x) for x in self.to_list()) + " -> None"

    def display(self):
        """Display the entire linked list as a python list."""
        print(self.to_list())