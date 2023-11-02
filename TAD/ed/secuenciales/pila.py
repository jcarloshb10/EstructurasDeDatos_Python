#!/usr/bin/env python
import sys
from ed.secuenciales.nodo import NodoLSE

class Pila():
    """Creamos la clase Pila con la cual podremos crear 
        una Pila con cualquier tipo de
        dato y usar sus diferentes métodos.

	Autor: JEAN CARLOS HERNANDEZ BENAVIDES
    """    

    def __init__(self):
        """__init__ se refiere al Constructor de un objeto de la clase Pila.
        --------------------------
        nodo_superior es el nodo que es la cima de la Pila, es una variable con un valor al inicio de None.
        """        

        self.nodo_superior = None

    def es_vacia(self):
        """es_vacia() es un método para determinar si la pila aún no ha recibido algún dato
            o se encuentra en un estado inicial sin valores.

            :return: el return me dará un valor después de verificar si está vacia o no la pila.
            :rtype: bool
        """        

        if self.nodo_superior is None:
            return True 
        else:
            return False

    def cima(self):
        """Este metodo nos permite mostrar el valor del nodo_superior o la cima de la Pila

        :return: Retorna el valor o dato al ser encontrado.
        si no encuentra nada también retornará que no lo halló o None
        :rtype: bool, si no lo halla y dato si lo encuentra en la Pila
        """        

        if self.es_vacia():
            return None
        else:
	        #le aumente abajo el .dato
            return self.nodo_superior.dato 

    def __len__(self):
        """Método que nos informa el calculo del tamaño de la pila completa.
        
        :return: Valor que representa el tamaño real de la pila con la variable tamanio.
        :rtype: int
        """ 
             
        tamanio = 0
        nodo_actual = self.nodo_superior
        while nodo_actual is not None:
            tamanio += 1
            nodo_actual = nodo_actual.sig
        return tamanio

    def apilar(self, nuevo_dato):
        """Este método permite insertar  o apilar un nuevo dato a la pila, tambien puede hacerlo cuando la pila está vacia.
            Este nuevo dato será la nueva cima de la pila. 
    
        :param nuevo_dato:  es el dato a insertarse o apilarse en la pila como la nueva cima.
        :type nuevo_dato: dato
        :return: retorno de variable de control para saber si se inserto o apiló el nuevo dato
        :rtype: bool
        """        

        nodo_nuevo = NodoLSE(nuevo_dato)
        if self.es_vacia():
            self.nodo_superior = nodo_nuevo
            return True
        else:
            if type(self.nodo_superior.dato) == type(nuevo_dato):
                nodo_nuevo.sig = self.nodo_superior
                self.nodo_superior = nodo_nuevo
                return True
            else:
                return False

    def desapilar(self):
        """desapilar() es un método para borrar o eliminar el valor considerado como la cima en la Pila.

            :return: el return me dará un valor después de verificar si se borró o no el valor de la cima.
            :rtype: bool
        """

        #aumente solo data_ret = self.top.data y cambie el true por data_ret y en el None de abajo era False
       
        if not self.es_vacia():          
            data_ret = self.nodo_superior.dato
            self.nodo_superior = self.nodo_superior.sig
            return data_ret
        else:         
            return None


    '''def recorrer(self):
        if not self.es_vacia():
            nodo_actual = self.nodo_superior
            while nodo_actual is not None:
                print(nodo_actual.dato)
                nodo_actual = nodo_actual.sig
            return "RECORRIDA"
        else:
            
            #return None
            return "PILA VACIA" '''
       

    def __str__(self):  # tarea
        cadena = "["
        nodo_actual = self.nodo_superior
        while nodo_actual is not None:
            cadena = cadena + str(nodo_actual.dato)
            nodo_actual = nodo_actual.sig
            if nodo_actual is None:
                break
            cadena = cadena + ","
        cadena = cadena + "]"
        return cadena


