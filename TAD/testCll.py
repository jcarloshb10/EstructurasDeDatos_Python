#!/usr/bin/env python
from ed.secuenciales.listaCSE import ListaCSE
from ed.secuenciales.nodo import NodoLSE

if __name__ == "__main__":
	cll = ListaCSE()
	print("is empty", cll.es_vacia())

	print("r 2", cll.borrar(2))
	cll.recorrer('-')

	print('a 5', cll.adicionar(5))
	print('a 8', cll.adicionar(8))
	cll.adicionar("h")

	print("is empty", cll.es_vacia())
	cll.recorrer('-')

	print("i 0 0", cll.insertar(0, 0))
	cll.recorrer('-')
	print("i 9 3", cll.insertar(9, 3))
	cll.recorrer('-')
	print("i 18 2", cll.insertar(18, 2))
	cll.recorrer('-')
	print("i 'h' 2", cll.insertar("h", 3))
	cll.recorrer('-')
	print("i 3 18", cll.insertar(3, 18))
	cll.recorrer('-')
	print("i 1 -1", cll.insertar(1, -1))
	cll.recorrer('-')

	print('a 10', cll.adicionar(10))

	print("r 5", cll.borrar(5))
	cll.recorrer('-')

	print("r 0", cll.borrar(0))
	cll.recorrer('-')

	print("r -2", cll.borrar(-2))
	cll.recorrer('-')

	print("r 12", cll.borrar(12))
	cll.recorrer('-')

	cll = ListaCSE()
	cll.adicionar(1)
	cll.adicionar(2)
	cll.adicionar(3)
	cll.adicionar(3)
	cll.adicionar(4)
	cll.adicionar(5)
	cll.recorrer('-')

	print("d 1", cll.borrar(1))
	cll.recorrer('-')

	print("d 5", cll.borrar(5))
	cll.recorrer('-')

	print("d 3", cll.borrar(3))
	cll.recorrer('-')

	print("d 9", cll.borrar(9))
	cll.recorrer('-')

	cll = ListaCSE()
	cll.adicionar(1)
	cll.adicionar(2)
	cll.adicionar(3)
	cll.adicionar(4)
	cll.adicionar(5)
	cll.adicionar(3)
	cll.adicionar(2)
	cll.adicionar(3)
	cll.adicionar(4)
	cll.adicionar(5)
	cll.recorrer('-')

	print("d 1", cll.borrar(1, True))
	cll.recorrer('-')

	print("d 5", cll.borrar(5, True))
	cll.recorrer('-')

	print("d 3", cll.borrar(3, True))
	cll.recorrer('-')

	print("d 9", cll.borrar(9, True))
	cll.recorrer('-')

	cll = ListaCSE()
	cll.adicionar(1)
	cll.adicionar(2)
	cll.adicionar(3)
	cll.adicionar(4)
	cll.adicionar(5)
	cll.recorrer('-')

	print(cll.ruleta_rusa(0))
	print(cll.ruleta_rusa(2))
	print(cll.ruleta_rusa(4))
	print(cll.ruleta_rusa(10))
	print(cll.ruleta_rusa(-3))

	print(".", end="")

	cll = ListaCSE()

	print(cll.insertar(30, 1))
	cll.recorrer('-')
