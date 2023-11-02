#!/usr/bin/env python
import sys
from nodo import NodoLSE

class Cola:
    """Creamos la clase Cola con la cual podremos crear 
        una cola con cualquier tipo de
        dato y tabién usar sus diferentes métodos.

	Autor: JEAN CARLOS HERNANDEZ BENAVIDES
    """    

    def __init__(self):
        """__init__ se refiere al Constructor de un objeto de la clase Cola.
        --------------------------
        nodo_frente es el nodo que es el frente o primero en la cola, es una variable con un valor al inicio de None.
        nodo_cola es el nodo que es el final o último en la cola, es una variable con un valor al inicio de None.
        """

        self.nodo_frente = None
        self.nodo_cola = None

    def es_vacia(self):
        """es_vacia() es un método para determinar si la cola aún no ha recibido algún dato
            o se encuentra en un estado inicial sin valores.

        :return: el return me dará un valor después de verificar si está vacia o no la cola.
        :rtype: bool
        """        

        if self.nodo_cola is None:
            return True 
        else:
            return False

    def frente(self):
        """Este metodo nos permite mostrar el valor o dato del nodo_frente o la el primero de la cola.

        :return: Retorna el valor o dato al ser encontrado.
        si no encuentra nada también retornará que no lo halló o None.
        :rtype: bool, si no lo halla y dato si lo encuentra en la cola.
        """        

        if not self.es_vacia():
            return self.nodo_frente.dato
        else: 
            return None

    def __len__(self):
        """Método que nos informa el calculo del tamaño de la cola completa.
        
        :return: Valor que representa el tamaño real de la cola con la variable tamanio.
        :rtype: int
        """        

        tamanio = 0
        nodo_actual = self.nodo_frente
        while nodo_actual is not None:
            nodo_actual = nodo_actual.sig
            tamanio += 1
        return tamanio

    def encolar(self, nuevo_dato):
        """Este método permite insertar o encolar un nuevo dato a la cola
            tambien puede hacerlo cuando la cola está vacia.
            El primer dato de la cola es el nodo_frente el ultimo es el nodo_cola. 
    
        :param nuevo_dato:  es el dato a insertarse o a encolarse en la cola como la nueva cola.
        :type nuevo_dato: dato
        :return: retorno de variable de control para saber si se inserto o encoló el nuevo dato
        :rtype: bool
        """        

        if self.es_vacia():
            nodo_nuevo = NodoLSE(nuevo_dato)
            self.nodo_frente = nodo_nuevo
            self.nodo_cola = nodo_nuevo
            return True
        elif type(nuevo_dato) == type(self.nodo_frente.dato):
            nodo_nuevo = NodoLSE(nuevo_dato)
            self.nodo_cola.sig = nodo_nuevo
            self.nodo_cola = nodo_nuevo
            return True
        return False

    def desencolar(self):
        """desencolar() es un método para borrar o eliminar el valor considerado como nodo_frente que es
            el primero en entrar y el primero que debe salir. El nodo frente luego tomará el valor del siguiente nodo.

            :return: el return me dará un valor después de verificar si se borró o no el valor del nodo_frente.
            :rtype: bool
        """        
        
        if not self.es_vacia():  
            self.nodo_frente = self.nodo_frente.sig
            if self.nodo_frente == None:
                self.nodo_cola = self.nodo_frente
            return True
        else:
            return False

    def recorrer(self):
        if not self.es_vacia():
            nodo_actual = self.nodo_frente
            while nodo_actual is not None:
                print(nodo_actual.dato)
                nodo_actual = nodo_actual.sig
            return "RECORRIDA"
        else:           
            #return None
            return "COLA VACIA"

    def __str__(self):
        nodo_actual = self.nodo_frente
        string = ""
        while nodo_actual is not None:
            string += str(nodo_actual.dato)
            nodo_actual = nodo_actual.sig
            string += " "
        return string
