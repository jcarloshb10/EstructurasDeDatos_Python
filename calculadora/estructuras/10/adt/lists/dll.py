from adt.lists.nodes import DoublyLinkedNode


class DoublyLinkedList():

    def __init__(self):
        self.head = None
        self.ps = -1
        self._onward = True

    def __len__(self):
        total_elementos = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            total_elementos = total_elementos + 1
        return total_elementos

    @property
    def onward(self):
        return self._onward

    @onward.setter
    def onward(self, nuevo_onward):
        self._onward = nuevo_onward
        return None

    def __str__(self):
        cadena = "["
        current_node = self.head
        if self._onward:
            while current_node is not None:
                cadena = cadena + str(current_node.data)
                current_node = current_node.next
                if current_node is None:
                    break
                cadena = cadena + ","
        else:
            previous_node = None
            while current_node is not None:
                previous_node = current_node
                current_node = current_node.next
            while previous_node is not None:
                cadena = cadena + str(previous_node.data)
                previous_node = previous_node.prev_next
                if previous_node is None:
                    break
                cadena = cadena + ","
        cadena = cadena + "]"
        return cadena

    def __iter__(self):
        self.__i = 0
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node is not None:
            self.__i += 1
            if self.__i == 1:
                return self.head.data
            self.current_node = self.current_node.next
            if self.current_node is None:
                raise StopIteration
            return self.current_node.data

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def append(self, data):
        new_node = DoublyLinkedNode(data)
        if self.is_empty():
            self.head = new_node
            return True
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev_next = current_node
            return True
        return False

    def delete(self, data, all=False):
        bool = False
        previos_node = None
        current_node = self.head
        while current_node is not None:
            if current_node.data is data:
                bool = True
                if previos_node is None:
                    self.head = current_node.next
                else:
                    previos_node.next = current_node.next
                    if current_node.next is not None:
                        current_node.next.prev_next = previos_node
                    if all is False:
                        return True
            previos_node = current_node
            current_node = current_node.next
        return bool

    def insert(self, data, pos):
        previous_node = None
        new_node = DoublyLinkedNode(data)
        cr_pos = 0
        current_node = self.head
        if self.is_empty() and pos == 0:
            self.head = new_node
            return True
        while current_node is not None and cr_pos != pos:
            previous_node = current_node
            current_node = current_node.next
            cr_pos = cr_pos + 1
        if current_node is not None and cr_pos == pos:
            if pos == 0:
                self.head = new_node
                new_node.next = current_node
                current_node.prev_next = new_node
                return True
            previous_node.next = new_node
            new_node.prev_next = previous_node
            new_node.next = current_node
            current_node.prev_next = new_node
            return True
        if self.__len__() == pos:
            self.append(data)
            return True

    def forward(self):
        current_node = self.head
        cr_pos = 0
        if self.head is None:
            return None
        if self.ps == -1:
            self.ps = 0
            return current_node.data
        while current_node is not None and cr_pos != self.ps:
            current_node = current_node.next
            cr_pos += 1
        if cr_pos == self.ps:
            if current_node.next is not None:
                self.ps += 1
                return current_node.next.data
            return current_node.data

    def backward(self):
        current_node = self.head
        cr_pos = 0
        if self.ps == -1:
            return None
        while current_node is not None and cr_pos != self.ps:
            current_node = current_node.next
            cr_pos += 1
        if cr_pos == self.ps:
            if current_node.prev_next is not None:
                self.ps -= 1
                return current_node.prev_next.data
            return current_node.data
# 33

    def remove(self, pos):
        cr_pos = 0
        current_node = self.head
        previos_node = None
        while current_node is not None and pos > cr_pos:
            previos_node = current_node
            current_node = current_node.next
            cr_pos += 1
        if current_node is not None:
            if pos == 0:
                current_node.next.prev_next = None
                self.head = self.head.next
            else:
                previos_node.next = current_node.next
                if current_node.next is not None:
                    current_node.next.prev_next = previos_node
            return True
        return False
    # return True if current_node is not None else Falsed

    def locate(self, pos):
        current_node = self.head
        cr_pos = 0
        while current_node is not None and cr_pos != pos:
            current_node = current_node.next
            cr_pos = cr_pos + 1
        if current_node is not None:
            return current_node.data
        return None
# hacer modulo eliminacion modulo Listado

    def explorer(self):
        current_node = self.head
        if self._onward:
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
        else:
            previous_node = None
            while current_node is not None:
                previous_node = current_node
                current_node = current_node.next
            while previous_node is not None:

                print(previous_node.data)
                previous_node = previous_node.prev_next
