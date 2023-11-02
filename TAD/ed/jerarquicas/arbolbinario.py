from ed.jerarquicas.nodo import NodoArbolBinario
from random import random

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        return self.raiz is None

    def adicionar(self, nueva_clave):
        self.raiz = self.__adicionar(self.raiz, nueva_clave)
    
    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbolBinario(nueva_clave)
        elif random() <= 0.5:  #Izquierda
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        else: #derecha
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)

        return sub_arbol

    def buscar(self, clave_buscar):
        return self.__buscar(self.raiz, clave_buscar)

    def __buscar(self, sub_arbol, clave_buscar):
        if sub_arbol is not None:
            if sub_arbol.clave == clave_buscar:
                return clave_buscar
            else:
                busc_izq = self.__buscar(sub_arbol.izq, clave_buscar)
                if busc_izq is not None:
                    return busc_izq
                else:
                    busc_der = self.__buscar(sub_arbol.der, clave_buscar)
                    if busc_der is not None:
                        return busc_der
        return None

    def __len__(self):
        return self.__numero_nodos(self.raiz)

    def __numero_nodos(self, sub_arbol):
        if sub_arbol is not None:
            return (1 + self.__numero_nodos(sub_arbol.izq) + self.__numero_nodos(sub_arbol.der))
        else:
            return 0
    
    def hojas(self):
        return self.__hojas(self.raiz)
        #pass cuantas hojas hay

    def __hojas(self, sub_arbol):
        if sub_arbol is not None:
            if sub_arbol.izq is None and sub_arbol.der is None:
                return 1
            else:
                return self.__hojas(sub_arbol.izq) + self.__hojas(sub_arbol.der)
        return 0

    def internos(self):
        return self.__internos(self.raiz)
        #cantidad de nodos internos que tiene

    def __internos(self, sub_arbol):
        if sub_arbol is not None:
            if sub_arbol.izq is not None and sub_arbol.der is not None:
                return 1
            else:
                return self.__internos(sub_arbol.izq) + self.__internos(sub_arbol.der)
        return 0

    def altura(self):
        return self.__altura(self.raiz)
        #pass altura del arbol completa #un arbol vacio tiene altura 0

    def __altura(self, sub_arbol):
        if sub_arbol is not None:
            profundidad_izq = self.__altura(sub_arbol.izq)
            profundidad_der = self.__altura(sub_arbol.der)
            if profundidad_izq > profundidad_der:
                return profundidad_izq + 1
            else:
                return profundidad_der + 1
        else:
            return 0
            




    