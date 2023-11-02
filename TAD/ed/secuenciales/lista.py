from nodo import NodoPrioridad
#from listadecolas import ColaDePrioridad

"""La ListaE es una estructura de datos la cual contiene elementos 
    o datos en unos nodos enlazados de forma simple, estos tienen la caracteristica de apuntar al siguiente elemento.
    Los nodos son  objetos pertenecientes a la clase NodoPrioridad

    Autores: TU NOMBRE COMPLETO | JEAN CARLOS HERNANDEZ BENAVIDES
"""
class ListaE:
    """Creamos la clase ListaE con la cual podremos crear una lista de colas con cualquier tipo de
        dato (prioridad y nodo de un cola) y usar sus diferentes métodos.
    """    
    def __init__(self):
        """__init__ se refiere al Constructor de un objeto de la clase ListaE.
        --------------------------
        nodo_cab es el nodo de cabecera de la lista de colas, es una variable con un valor al inicio de None.
        """ 
                       
        self.nodo_cab = None
    
    def es_vacia(self):
        """es_vacia() es un método para determinar si la lista aún no ha recibido algún dato
            o se encuentra nuevamente en un estado inicial sin valores.

            :return: el return me dará un valor después de verificar si está vacia o no la lista de colas.
            :rtype: bool
        """        
        return self.nodo_cab is None

    def insertar(self,prioridad, nuevo_dato):
        """Este método permite insertar un nuevo dato de forma que ubica el nodo en la cola 
           de la prioridad correspondiente.

        :param nuevo_dato:  es el dato a insertarse en alguna posicion de la lista dentro de una cola.
        :type nuevo_dato: dato
        :param prioridad: es el otro valor que el metodo recibe ademas del nuevo dato, esta posicion 
        se cuenta de izquierda a derecha desde 0, defaults to 0.
        :type prioridad: int
        :return: retorno de variable de control para saber si se inserto el nuevo dato correctamente
        :rtype: bool
        """        
        
        if type(prioridad) == int and prioridad >= 1:
            nodo_nuevo = NodoPrioridad(prioridad,nuevo_dato)
            if self.es_vacia():
                self.nodo_cab = self.nodo_cola = nodo_nuevo
                return True
            elif type(nuevo_dato) == type(self.nodo_cab.dato):
                nodo_actual = self.nodo_cab
                cnt = 0
                while nodo_actual:
                    if prioridad < nodo_actual.prioridad:
                        break
                    else:
                        nodo_actual = nodo_actual.sig
                        cnt += 1
                if cnt == 0:
                    nodo_nuevo.sig = self.nodo_cab
                    self.nodo_cab = nodo_nuevo
                elif 0 < cnt < len(self):
                    nodo_actual = self.nodo_cab
                    for i in range(cnt - 1):
                        nodo_actual = nodo_actual.sig
                    nodo_actual.sig, nodo_nuevo.sig = nodo_nuevo, nodo_actual.sig
                elif cnt == len(self):
                    self.nodo_cola.sig = nodo_nuevo
                    self.nodo_cola = nodo_nuevo
                return True
        return False

    #METODO __LEN__
    def __len__(self):
        """Método que nos informa el calculo del tamaño de cualquier lista de colas.
        
        :return: Valor que representa el tamaño real de la lista de colas.
        :rtype: int
        """        

        cont = 0
        nodo_actual = self.nodo_cab
        while nodo_actual is not None:
            cont += 1
            nodo_actual = nodo_actual.sig
        return cont

    #METODO __STR__
    def __str__(self):
        """Método que formatea o convierte en cadena la lista con los datos para su muestra.

        :return: Cadena de la lista con los datos en formato.
        :rtype: dato
        """        

        nodo_actual = self.nodo_cab
        cadena = ""
        while nodo_actual is not None:
            if nodo_actual.sig is None:
                cadena += "[" + str(nodo_actual.dato) + "]"
                nodo_actual = nodo_actual.sig
            else:
                cadena += "[" + str(nodo_actual.dato) + "]" + "\n!\n"
                nodo_actual = nodo_actual.sig
        return cadena


        
#Mi Test
if __name__ == "__main__":
    
    lista_numeros = ListaE()
    print("HHH")
    print(lista_numeros.insertar(5,10))
    #print(lista_numeros.insertar(6,10,1))
    print(lista_numeros.insertar(6,15))
    print(lista_numeros.insertar(2,100))
    print(lista_numeros.insertar(4,50))
    #print(lista_numeros.recorrer())

    print(lista_numeros.insertar(3,35))
    print(lista_numeros.insertar("HOLA",5))
    print(lista_numeros.insertar(9.45,5))
    print(lista_numeros.insertar(6,20))
    #print(lista_numeros.recorrer())
    print(lista_numeros.insertar(10, 1))
    #print(lista_numeros.recorrer())
    print(lista_numeros.insertar(1,11))
    print(lista_numeros.__len__())
    print(lista_numeros.__str__())