from adt.lists.nodes    import SinglyLinkedNode

class SinglyLinkedList():
    """docstring for SingleLinkedList."""

    def __init__(self):
        self.head=None

    def __str__(self):
        cadena="["
        current_node=self.head
        while current_node is not None:
            cadena = cadena + str(current_node.data)
            current_node=current_node.next
            if current_node is None:
                break
            cadena = cadena + ","
        cadena = cadena + "]"
        return cadena

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def append(self,new_data):
        new_node=SinglyLinkedNode(new_data)

        if self.is_empty() :
            self.head=new_node
            return True
        else:
            current_node=self.head

            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=new_node
            return True
        return False

    def explorer(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next



    def remove(self,pos):
        cr_pos=0
        current_node=self.head
        previos_node=None
        while current_node is not None and pos > cr_pos:
            previos_node=current_node
            current_node=current_node.next
            cr_pos+=1
        if current_node is not None:
            if pos==0:
                self.head=self.head.next
            else:
                previos_node.next=current_node.next
            return True
        return False
        #return True if current_node is not None else False

    def search(self,data):#devuelve el dato o none
            current_node=self.head
            while current_node is not None and current_node.data != data:
                current_node=current_node.next
            if current_node is not None:
                return current_node.data
            return None
            #return current_node.data if current_node is not None else None
            #tareax

    def delete(self,data,all=False):
        previos_node=None
        current_node=self.head
        while current_node is not None :
            if current_node.data==data:
                if previos_node==None:
                    self.head=current_node.next
                else:
                    if all==False:
                        previos_node.next=current_node.next
                        break
                    else:
                        previos_node.next=current_node.next
            previos_node=current_node
            current_node=current_node.next

    def locate(self,pos):
        current_node=self.head
        cr_pos=0
        while current_node is not None and cr_pos!=pos:
            current_node=current_node.next
            cr_pos=cr_pos+1
        if current_node is not None:
            return current_node.data
        return None

    def __len__(self): #calcular el total de elementos de una seleccion
        total_elementos=0
        current_node=self.head
        while current_node is not None:
            current_node=current_node.next
            total_elementos=total_elementos+1
        return total_elementos

    def insert(self,new_data,pos=0):
        previous_node=None
        new_node = SinglyLinkedNode(new_data)
        cr_pos=0
        current_node=self.head
        if self.is_empty() and pos==0:
            self.head=new_node
            return True
        while current_node is not None and cr_pos != pos:
            previous_node=current_node
            current_node=current_node.next
            cr_pos=cr_pos+1
        if current_node is not None and cr_pos==pos :
            if pos==0:
                self.head=new_node
                new_node.next=current_node
                return True
            previous_node.next=new_node
            new_node.next=current_node
            return True
        if self.__len__()==pos:
            self.append(new_data)
            return True
