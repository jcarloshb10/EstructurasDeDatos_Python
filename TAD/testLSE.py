#!/usr/bin/env python
from ed.secuenciales.listaSE import ListaSE
from conjunto import Conjunto

if __name__ == "__main__":

    #TEST ListaSE
    lista_numeros = ListaSE()
    #print(lista_numeros.insertar(0))
    print(lista_numeros.recorrer())
    print(lista_numeros.adicionar(5))
    print(lista_numeros.adicionar("HOLA"))
    print(lista_numeros.adicionar(9.45))
    print(lista_numeros.adicionar(6))
    print(lista_numeros.recorrer())
    print(lista_numeros.insertar(10, 1))
    print(lista_numeros.recorrer())
    print(lista_numeros.adicionar(20))
    print(lista_numeros.insertar(15, 2))
    print(lista_numeros.adicionar(1))
    print(lista_numeros.recorrer())
    #print(lista_numeros.insertar(9, 2))
    #print(lista_numeros.recorrer())
    print(lista_numeros.buscar(6,True))
    print(lista_numeros.recorrer())
    print(lista_numeros.borrar_pos(3))
    print(lista_numeros.recorrer())
    print(lista_numeros.borrar(15))
    print(lista_numeros.recorrer())
    print(lista_numeros.__len__())
    print(lista_numeros.__str__())
    print(lista_numeros.__iter__())

    #Pruebas Conjunto

    '''lista_numeros = Conjunto('a')
    lista_numeros2 = Conjunto('b')
    lista_numeros3 = Conjunto('c')
    
    lista_numeros.agregar(4)
    lista_numeros.agregar(7)
    lista_numeros.agregar(10)
    lista_numeros.agregar(13)
    lista_numeros.agregar(15)

    print(lista_numeros.pertenencia(15))
    
    print(lista_numeros.cardinal())
    
    lista_numeros2.agregar(7)
    lista_numeros2.agregar(10)
    lista_numeros2.agregar(15)
    lista_numeros2.agregar(20)

    print(lista_numeros2.cardinal())

    print(lista_numeros2.es_subconjunto(lista_numeros))
    print(lista_numeros.es_subconjunto(lista_numeros2))
    
    print(lista_numeros2.union(lista_numeros))
    print(lista_numeros.cardinal())
    print(lista_numeros2.cardinal())
    print(lista_numeros2.union(lista_numeros))
    print(lista_numeros2.intersection(lista_numeros))
    print(lista_numeros2.diferencia(lista_numeros))
    
    lista_numeros3.agregar(7)
    lista_numeros3.agregar(10)
    lista_numeros3.agregar(15)

    print(lista_numeros3.es_subconjunto(lista_numeros))'''