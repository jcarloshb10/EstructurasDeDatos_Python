#!/usr/bin/env python

"""Un nodo contiene diferentes datos de interes  para poder desplazarse y referenciar o
    que es lo mismo que poder fijar a un nodo.
    
    AUTHOR: JEAN CARLOS HERNANDEZ BENAVIDES 
"""

class NodoLSE:
    """La clase NodoLSE permite almacenar los datos dentro de un nodo
        y con una direccion de memoria
    """    

    def __init__(self, dato):   
        """Constructor de NodoLSE

        :param dato: Recibe este metodo constructor un dato para
        agregarlo en el nodo
        :type dato: objeto
        """        

        self.dato = dato
        self.sig = None 

    def __str__(self):
        """Método que retorna los datos del nodo en forma de texto

        :return: una cadena de caracteres con los datos
        :rtype: str
        """        
        
        return str(self.dato)


class NodoPrioridad():
    """La clase NodoPrioridad permite almacenar los datos dentro de un nodo además de la prioridad que
        tiene el dato almacenado.
    """ 

    def __init__(self, prioridad,dato):
        """Constructor de NodoPrioridad

        :param dato: Recibe este metodo constructor un dato para
        agregarlo en el nodo
        :type dato: objeto
        :param prioridad: Recibe este metodo constructor un entero como
        prioridad para tenerlo en cuenta al momento de agregarlo 
        :type prioridad: int
        """

        self.dato = dato
        self.sig = None
        self.prioridad = prioridad