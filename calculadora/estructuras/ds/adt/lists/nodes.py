class SinglyLinkedNode:
    def __init__(self, data):
        self.data = data  # almacena los datos para el nodo
        self.next = None  # almacena la referencia al siguiente nodo


class DoubleLinkedNode(SinglyLinkedNode):
    def __init__(self, data):
        super().__init__(data)
        self.previous = None  # almacena la referencia al nodo anterior
