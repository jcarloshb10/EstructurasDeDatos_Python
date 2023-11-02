#!/usr/bin/env python
#import sys
from ed.secuenciales.pila import Pila
from ed.secuenciales.cola  import Cola

#MI TEST listaPila
if __name__ == "__main__":
    
    cola_numeros = Cola()
    print(cola_numeros.es_vacia())
    print(cola_numeros.__str__())
    print(cola_numeros.frente())
    print(cola_numeros.recorrer())
    print(cola_numeros.encolar(10))
    print(cola_numeros.__len__())

    print(cola_numeros.es_vacia())
    print(cola_numeros.recorrer())
    print(cola_numeros.desencolar())
    print(cola_numeros.recorrer())
    print(cola_numeros.es_vacia())

    print(cola_numeros.encolar(20))
    print(cola_numeros.__len__())
    print(cola_numeros.recorrer())
    print(cola_numeros.encolar(30))
    print(cola_numeros.encolar(40))
    print(cola_numeros.encolar(20))
    print(cola_numeros.encolar(50))
    print(cola_numeros.__str__())
    print(cola_numeros.__len__())
    print(cola_numeros.frente())

    print(cola_numeros.desencolar())
    print(cola_numeros.recorrer())
    print(cola_numeros.desencolar())
    print(cola_numeros.recorrer())
    print(cola_numeros.desencolar())
    print(cola_numeros.__len__())
    print(cola_numeros.recorrer())

    print(cola_numeros.desencolar())
    print(cola_numeros.recorrer())
    print(cola_numeros.desencolar())
    print(cola_numeros.frente())
    print(cola_numeros.desencolar())
    print(cola_numeros.es_vacia())

