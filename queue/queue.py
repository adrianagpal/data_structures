from node import Node

class Queue:

    def __init__(self):
        self.start = None
        self.last = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.start = new_node
            self.last = new_node

        else:
            self.last.next = new_node
            self.last = new_node

        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        data = self.start.data
        self.start = self.start.next
        self.size -= 1

        if self.size == 1:
            self.last = None

        return data

    def clear(self):
        self.start = None
        self.size = 0
