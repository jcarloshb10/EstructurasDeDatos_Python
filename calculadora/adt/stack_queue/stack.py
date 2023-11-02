from adt.stack_queue.nodes import StackNode


class Stack:
    def __init__(self) -> None:
        self.top = None

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, data) -> bool:
        new_node = StackNode(data)
        if self.is_empty():
            self.top = new_node
        elif type(data) == type(self.top.data):
            new_node.next = self.top
            self.top = new_node
        else:
            return False
        return True

    def pop(self) -> object:
        if not self.is_empty():
            data_ret = self.top.data
            self.top = self.top.next
            return data_ret

    def peek(self) -> object:
        if not self.is_empty():
            return self.top.data

    def __str__(self) -> str:
        current_node = self.top
        string = ""
        while current_node is not None:
            string += str(current_node.data) + "\n"
            current_node = current_node.next
        return string

    def __len__(self) -> int:
        cnt = 0
        current_node = self.top
        while current_node is not None:
            cnt += 1
            current_node = current_node.next
        return cnt
