from adt.lists.nodes import SinglyLinkedNode


class CircularLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):  # calcular el total de elementos de una seleccion
        total_elementos = 0
        current_node = self.head
        while self.head is not None:
            if current_node == self.tail:
                total_elementos = total_elementos + 1
                break
            current_node = current_node.next
            total_elementos = total_elementos + 1
        return total_elementos

    # return True if current_node is not None else False
    def __str__(self):
        cadena = "["
        current_node = self.head
        while self.head is not None:
            cadena = cadena + str(current_node.data)
            if self.tail == current_node:
                break
            current_node = current_node.next
            cadena = cadena + ","
        cadena = cadena + "]"
        return cadena

    def __iter__(self):
        self.__i = 0
        self.current_node = self.head
        return self

    def __next__(self):
        if self.head is not None:
            if self.tail == self.current_node:
                raise StopIteration
            self.__i += 1
            if self.__i == 1:
                return self.head.data
            self.current_node = self.current_node.next
            return self.current_node.data

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def explorer(self):
        current_node = self.head
        while True and self.head is not None:
            if current_node == self.tail:
                print(current_node.data)
                break
            print(current_node.data)
            current_node = current_node.next
        return None

    def append(self, new_data):
        new_node = SinglyLinkedNode(new_data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return True
        else:
            current_node = self.head
            while True:
                if current_node == self.tail:
                    current_node.next = new_node
                    self.tail = new_node
                    new_node.next = self.head
                    break
                current_node = current_node.next
            return True
        return False

    def insert(self, new_data, pos):
        previous_node = None
        new_node = SinglyLinkedNode(new_data)
        cr_pos = 0
        current_node = self.head
        if self.is_empty() and pos == 0:
            new_node.next = new_node
            self.tail = new_node
            self.head = new_node
            return True
        else:
            if self.head is None:
                return False
            while cr_pos != pos:
                previous_node = current_node
                current_node = current_node.next
                cr_pos = cr_pos + 1
            if cr_pos == pos:
                if pos == 0:
                    self.head = new_node
                    new_node.next = current_node
                    self.tail.next = new_node
                    return True
                previous_node.next = new_node
                new_node.next = current_node
                if previous_node == self.tail:
                    self.tail = previous_node.next
                return True

    def remove(self, pos):
        cr_pos = 0
        current_node = self.head
        previos_node = None
        while pos > cr_pos and self.head is not None:
            previos_node = current_node
            current_node = current_node.next
            cr_pos += 1
        if self.head is not None:
            if pos == 0:
                self.head = self.head.next
            else:
                previos_node.next = current_node.next
                if current_node == self.tail:
                    self.tail = previos_node
                if current_node == self.head:
                    self.head = current_node.next
            if current_node.next == current_node:
                self.head = None
                self.tail = None
            return True
        return False

    def delete(self, data, all=False):
        boolea = False
        previos_node = None
        current_node = self.head
        while self.head is not None:
            if current_node.data == data:
                boolea = True
                if self.head == current_node:
                    self.head = current_node.next
                    self.tail.next = current_node.next
                    if self.tail == current_node:
                        self.tail = None
                        self.head = None
                else:
                    previos_node.next = current_node.next
                    if self.tail == current_node:
                        self.tail = previos_node
                if all is False:
                    return True
            if self.tail == current_node:
                break
            previos_node = current_node
            current_node = current_node.next
        return boolea

    def search(self, data):  # devuelve el dato o none
        current_node = self.head
        while self.head is not None and current_node.data != data:
            if current_node == self.tail:
                break
            current_node = current_node.next
        if self.head is not None and current_node.data == data:
            return current_node.data
        return None
        # return current_node.data if current_node is not None else None
        # tareax

    def locate(self, pos):
        current_node = self.head
        cr_pos = 0
        while current_node is not None and cr_pos != pos:
            current_node = current_node.next
            cr_pos = cr_pos + 1
        if current_node is not None:
            return current_node.data
        return None

    def roulette(self, rel_pos):
        current_node = self.head
        cr_pos = 0
        while self.head is not None and cr_pos != rel_pos:
            if self.tail == current_node:
                return None
            current_node = current_node.next
            cr_pos = cr_pos + 1

        if current_node is not None:
            return current_node.data
        return None
