class SinglyLinkedNode():
    """docstring for SinglyLinkedNode."""

    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyLinkedNode():
    def __init__(self, data):
        self.next = None
        self.data = data
        self.prev_next = None
