from adt.lists.sll import SinglyLinkedList

if __name__ == "__main__":

    # list1 = [1,9,8,2,7,3,6,4,5]
    # print(list1)
    # bubblesort(list1)
    # print(list1)
# is para comparar referencias

    lista_num = SinglyLinkedList()  # invoca al constructor

    lista_num.append(1)
    lista_num.append(9)
    lista_num.append(2)
    lista_num.append(8)
    lista_num.append(3)
    lista_num.append(7)
    lista_num.append(4)
    lista_num.append(1)
    lista_num.append(2)
    lista_num.explorer()#mostrar
    print("-----------------------------------------------------")
    lista_num.delete(2,True)#con true elimina todas las coincidencias
    lista_num.explorer()
    #print(lista_num)

    # print("LISTA ORDENADA:\n"+str(lista_num))

     #print('-------------------------------------------------')
    # lista_num.remove(0)
    #lista_num.explorer()#mostrar
    #lista_num.remove(0)
    #lista_num.remove(4)
    #lista_num.remove(6)"""
    print ("Search(Busqueda):", lista_num.search(1))
    print('-------------------------------------------------')
    #lista_num.explorer()#mostrar

    # print('str: ', str(lista_num))
    # print('len: ', len(lista_num))  # SI RETORNA ALGO SE COLOCA PRINT PARA PODER MOSTRARLO
    # print ('search: ',lista_num.search(2))
    #
    # for i in range(len(lista_num)):
    #     print ('locate: ',lista_num.locate(i))

    print('-------------------------------------------------')
    # lista_num.insert(7, -5)  # no permite valores menores a 0
    # lista_num.insert(1)  # posicion cero se va areemplazar en la cabeza
    # lista_num.insert(3, 20)  # con una posicion entre 2 nodos se inserta igualmente
    #lista_num.insert(6, 5)  # se agregara al final siempre que la posicion sea igual al tamaño actual
    # lista_num.insert(7, 7)# si es mayor al tamaño actual muestra un ERROR

    # lista_num.explorer()
