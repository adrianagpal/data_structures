from ..node import Node

class LinkedList:
    def __init__(self):
        self._size = 0

    def add(self, data):
        new_node = Node(data)
        if self._size == 0:
            self.start = new_node
        else:
            self.last.assign_next(new_node)

        self.last = new_node
        self._size += 1

    def remove(self, index):
        if index < 0 or self._size == 0 or index > (self._size - 1):
            return False

        if self._size == 1 and index == 0:
            self.last == None
            self.start == None
            self._size == 0
            return True

        current = self.start
        y = 0

        while y != index:
            previous = current
            current = current.next
            y += 1

        if current.next == None:
            self.last = previous

        previous.assign_next(current.next)
        self._size -= 1
        return True

    def get(self, index):
        current = self.start
        y = 0

        if index > (self._size - 1) or index < 0:
            return None

        while y != index:
            previous = current
            current = current.next
            y += 1

        return current.data

    def count(self, data):

        if self._size == 0:
            return 0

        current = self.start
        size = self._size
        y = 0
        count = 0

        while y != size:
            previous = current
            current = current.next

            if previous.data == data:
                count += 1

            y += 1

        return count

    def find(self, data):

        if self._size == 0:
            return None

        current = self.start
        size = self._size
        y = 0

        while y != size:
            previous = current
            current = current.next

            if previous.data == data:
                return y

            y += 1

        return None

    def findall(self, data):
        if self._size == 0:
            return None

        current = self.start
        size = self._size
        y = 0
        list = []

        while y != size:
            previous = current
            current = current.next

            if previous.data == data:
                list.append(y)

            y += 1

        if len(list) != 0:
            return list
        else:
            return None

    @property
    def size(self):
        return self._size
