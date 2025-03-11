class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """
    MAX_SIZE = 5

    def __init__(self):
        """Initialize the stack with an empty state."""

        self.head = None
        self.tail = None
        self.size = 0


    def push(self, distance):
        """Add a new Temperature object to the stack, replacing the oldest entry if full."""
        new_dist = Node(distance)

        if(self.size == 0):
            self.head = new_dist
            self.tail = new_dist
            new_dist.next = new_dist
            self.size = 1

        elif self.size < self.MAX_SIZE:
            new_dist.next = self.head
            self.head = new_dist
            self.tail.next = new_dist
            self.size + 1
        else:
            self.tail.data = distance  #overrides oldest node's data, the tail is now the newest distance val
            self.head = self.tail.next
            self.tail = self.tail.next



    def pop(self):
        """Remove the oldest entry from the stack."""

        if self.is_empty:
            print("Stack is empty")
            return None

        temp = self.tail.data #oldest node's data

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.next
            self.head.next = self.tail

        self.size -= 1
        return temp


    def peek(self):
        """Return the most recent temperature entry without removing it."""
        if self.is_empty():
            print ("Stack is empty")
            return None
        else:
            return self.head.data

    def print_stack(self):
        """Print all stored readings in order from oldest to newest."""
        if self.is_empty():
            print("Stack is empty")
            return

        value = self.tail
        count = 0

        while count < self.size:
            print(value.data)  # print from oldest to newest
            value = value.next
            count += 1


    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        if self.size == 0:
            return True
        else:
            return False


