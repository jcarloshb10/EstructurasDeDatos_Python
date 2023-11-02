class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class PriorityNode(StackNode):
    def __init__(self, data, priority):
        StackNode.__init__(self, data)
        self.priority = priority
