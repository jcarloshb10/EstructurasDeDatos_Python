from adt.stack_queue import StackNode


class Stack():
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
# push stack homogeneo

    def push(self, data):
        new_node = StackNode()
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        return True

    def pop(self):
        if not self.is_empty():
            data_ret = self.top.data
            self.top = self.top.next
            return data_ret
        return None

    def peek(self):
        if not self.is_empty:
            return self.top.data
        return None

    def __str__():  # tarea
        cadena = "["
        current_node = self.top
        while current_node is not None:
            cadena = cadena + str(current_node.data)
            current_node = current_node.next
            if current_node is None:
                break
            cadena = cadena + ","
        cadena = cadena + "]"
        return cadena
# tarea hacer queue igual a este

    def __len__():  # tarea
        total_elementos = 0
        current_node = self.top
        while current_node is not None:
            total_elementos += 1
            current_node = current_node.next
