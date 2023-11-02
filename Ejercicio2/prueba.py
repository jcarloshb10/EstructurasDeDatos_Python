from datetime import date
from tad.listas.lse import ListaSimplementeEnlazada

lista = ListaSimplementeEnlazada()
lista.añadir("0")
lista.añadir("1")
lista.añadir("2")
lista.añadir("3")
lista.añadir("4")
print(lista)
lista.suprimir("3")
print(lista)
print(date.today().year)
