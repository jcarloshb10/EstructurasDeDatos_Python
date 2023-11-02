from adt.stack_queue.nodes import StackNode


class Queue:
    def __init__(self):
        self._front = None
        self.tail = None

    def is_empty(self):
        return self._front == None and self.tail == None

    def enqueue(self, data):
        if self.is_empty():
            new_node = StackNode(data)
            self._front = new_node
            self.tail = new_node
            return True

        new_node = StackNode(data)
        self.tail.next = new_node
        self.tail = new_node
        return True
        

    def dequeue(self):
        if not self.is_empty():
            data = self._front.data
            self._front = self._front.next
            if self._front == None:
                self.tail = self._front
            return data

    def front(self):
        if not self.is_empty():
            data = self._front.data
            return data

    def __len__(self):
        i = 0
        current_node = self._front
        while current_node is not None:
            current_node = current_node.next
            i += 1
        return i

    def __str__(self):
        current_node = self._front
        string = ""
        while current_node is not None:
            string += str(current_node.data)
            current_node = current_node.next

        return string
