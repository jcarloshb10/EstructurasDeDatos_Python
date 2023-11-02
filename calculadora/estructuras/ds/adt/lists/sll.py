from adt.lists.nodes import SinglyLinkedNode


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """if self.head is None:
            return True
        return False"""
        return self.head is None

    def append(self, new_data):
        new_node = SinglyLinkedNode(new_data)  # crea un nuevo nodo con el dato
        if self.is_empty():  # si esta vacio
            self.head = new_node  # asignar la referencia a head
            return True
        elif type(self.head.data) == type(new_data):

            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node  # SIGUIENTE SEA EL NUEVO NODO

            return True
        else:
            print("ERROR EL TIPO DEL DATO NO ES VALIDO")
        return False

    def explorer(self):#imptimir cada uno de los data presentes
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def __insert1(self, new_data, pos=0):  # no se puede usar fuera de la clase porque esta oculto __->oculto
        """INSERTAR UN NODO EN UNA POSICION"""
        current_node = self.head
        new_node = SinglyLinkedNode(new_data)  # CREAR UN NUEVO NODO CON EL NUEVO dato

        if pos == 0:
            aux_var = current_node
            self.head = new_node
            new_node.next = aux_var
        elif pos > 0:
            i = 0
            while i < pos - 1:
                i += 1
                current_node = current_node.next  # el nodo actual pasa al siguiente

            aux_var = current_node.next  # crear variable auxiliar
            current_node.next = new_node  # cambio la direccion al nodo SIGUIENTE
            new_node.next = aux_var

    def insert(self, new_data, pos=0):
        current_node = self.head  # comienza en la cabeza
        # new_node = SinglyLinkedNode(new_data)
        if pos >= 0:
            for i in range(len(self)):
                if i == pos:
                    current_node.data, aux_var = new_data, current_node.data

                    for j in range(pos + 1, len(self)):
                        current_node.next.data, aux_var = (aux_var, current_node.next.data)
                        current_node = current_node.next

                    new_node = SinglyLinkedNode(aux_var)
                    current_node.next = new_node
                    break

                current_node = current_node.next
            return True###
        return False###

    def delete(self, data,all=False):
        flag = False
        if not self.is_empty():
            if self.head.data == data:
                self.head = self.head.next
                flag = True###
            else:
                current_node = self.head
                while current_node is not None:
                    if current_node.next is not None:

                        if current_node.next.data == data:
                            current_node.next = current_node.next.next
                            flag = True
                            if not all:#al negarlo se convierte en verdadero
                                break  # elimina la primera coincidencia y sin el break eliminaria eliminaria todas las coincidencias
                    current_node = current_node.next
        return flag###

    def __remove1(self, pos):
        cont = 0
        if pos == cont:
            self.head = self.head.next
        elif pos > 0:
            current_node = self.head
            while current_node is not None:
                if pos - 1 == cont:
                    current_node.next = current_node.next.next
                    break
                cont += 1
                current_node = current_node.next

    def locate(self, pos):
        cont = 0
        current_node = self.head
        if pos >= 0:
            while current_node is not None:
                if pos == cont:
                    return current_node.data
                cont += 1
                current_node = current_node.next

    def __search1(self, data):
        current_node = self.head
        while current_node is not None:
            if data == current_node.data:
                return current_node.data
            current_node = current_node.next

    def __str__(self):#retornar la cadena con todos los data-> se llama a tarvez de un print() o un str()
        current_node = self.head
        acum = ""  # cadena de caracteres que funciona como acumulador
        while current_node is not None:
            aux_var = current_node.data
            acum += str(aux_var) + "\n"  # lo cancatena = aumentar
            current_node = current_node.next
        return acum

    def __len__(self):#retorna la cantidad de nodes que hay -> se llama a travez de la funcion len()
        cont = 0
        current_node = self.head
        while current_node is not None:
            cont += 1
            current_node = current_node.next
        return cont

    def __sort(self):
        for i in range(len(self) - 1, 0, -1):
            for j in range(i):
                if self.locate(j) > self.locate(j + 1):
                    k = 0  # un numero que aumenta en un ciclo es un iterador
                    current_node1 = self.head  # empieza desde la cabeza
                    while k < j:
                        k += 1
                        current_node1 = current_node1.next

                        l = 0  # un numero que aumenta en un ciclo es un iterador
                        current_node2 = self.head  # empieza desde la cabeza
                        while l < j + 1:
                            l += 1
                            current_node2 = current_node2.next

                            current_node1.data, current_node2.data = (current_node2.data, current_node1.data)

    def remove(self, pos):
        cr_pos = 0
        current_node = self.head
        previous_node = None
        while current_node is not None and pos > cr_pos:  # el!= como > dan el mismo resultado
            previous_node = current_node
            current_node = current_node.next
            cr_pos += 1
        if current_node is not None:  # si current_node is not node se encontro el nodo
            if pos == 0:  # pos pasada
                self.head = self.head.next
            else:
                previous_node.next = current_node.next
            # return True
        # return False
        return True if current_node is not None else False

    def search(self, data):
        current_node = self.head
        while current_node is not None and current_node.data != data:  #!= siga al siguiente
            current_node = current_node.next  # avanzarlo
            # si lo encontre devuelvo el valor del dato y si no devuelve encontre
        """if current_node is not None:
            return current_node.data
        return None """
        return current_node.data if current_node is not None else None


# def bubblesort(_list):
#     for i in range(len(_list)-1,0,-1):
#         for j in range(i):
#             if _list[j]>_list[j+1]:
#                 _list[j],_list[j+1]=_list[j+1],_list[j]
#                 # aux =_list[j]
#                 # _list[j]=_list[j+1]
#                 # _list[j+1] =aux
