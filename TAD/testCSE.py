#!/usr/bin/env python
#import sys
from ed.secuenciales.listaCSE import ListaCSE
from ed.secuenciales.nodo import NodoLSE


#MI TEST LISTACSE
if __name__ == "__main__":
    
    lista_numeros = ListaCSE()
    print(lista_numeros.adicionar(10))
    print(lista_numeros.adicionar(35))
    print(lista_numeros.adicionar(20))
    print(lista_numeros.adicionar(25))
    print(lista_numeros.adicionar(30))
    print(lista_numeros.recorrer())
    print(lista_numeros.insertar(1,35))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.borrar(2,True))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.adicionar(40))
    print(lista_numeros.adicionar(25))
    print(lista_numeros.adicionar(45))
    print(lista_numeros.adicionar(35))
    print(lista_numeros.insertar(100,2))
    print(lista_numeros.adicionar(25))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.borrar(2, False))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.borrar(25, False))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.buscar(25))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.buscar(40))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.ruleta_rusa(5))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.ruleta_rusa(30))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.__iter__())
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.buscar_cuantos(35))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.borrar(0, True))
    print(lista_numeros.recorrer('-'))

    print("\n##### RULETA ######\n")
    print(lista_numeros.ruleta_rusa(5))