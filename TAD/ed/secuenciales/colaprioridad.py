#!/usr/bin/env python
from ed.secuenciales.nodo import NodoLSE,NodoPrioridad
     
class Cola:
    """Creamos la clase Cola con la cual podremos crear 
        una cola con cualquier tipo de
        dato y tabién usar sus diferentes métodos.

	Autores: MILER ANDRÉS ESPAÑA | JEAN CARLOS HERNANDEZ BENAVIDES
    """

    def __init__(self, prioridad = 1):
        """__init__ se refiere al Constructor de un objeto de la clase Cola.
        --------------------------
        nodo_frente es el nodo que es el frente o primero en la cola, es una variable con un valor al inicio de None.
        nodo_cola es el nodo que es el final o último en la cola, es una variable con un valor al inicio de None.
        prioridad es el numero entero de prioridad que lleva la cola
        """

        self.prioridad = prioridad
        self.nodo_frente = None
        self.nodo_cola = None

    def frente(self):
        """Este metodo nos permite mostrar el valor o dato del nodo_frente o la el primero de la cola.

        :return: Retorna el valor o dato al ser encontrado.
        si no encuentra nada también retornará que no lo halló o None.
        :rtype: bool, si no lo halla y dato si lo encuentra en la cola.
        """

        if not self.es_vacia():
            return self.nodo_frente.dato
        return None

    def es_vacia(self):
        """es_vacia() es un método para determinar si la cola aún no ha recibido algún dato
            o se encuentra en un estado inicial sin valores.

        :return: el return me dará un valor después de verificar si está vacia o no la cola.
        :rtype: bool
        """ 

        if self.nodo_cola is None:
            return True
        return False

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
            nuevo_nodo = NodoLSE(nuevo_dato)
            self.nodo_frente = nuevo_nodo
            self.nodo_cola = nuevo_nodo
            return True
        else:
            if type(nuevo_dato) == type(self.nodo_frente.dato):
                nuevo_nodo = NodoLSE(nuevo_dato)
                self.nodo_cola.sig = nuevo_nodo
                self.nodo_cola = self.nodo_cola.sig
                return True
            return False

    def desencolar(self):
        """desencolar() es un método para borrar o eliminar el valor considerado como nodo_frente que es
            el primero en entrar y el primero que debe salir. El nodo frente luego tomará el valor del siguiente nodo.

            :return: el return me dará un valor después de verificar si se borró o no el valor del nodo_frente con la variable r.
            :rtype: bool
        """ 

        if self.es_vacia(): return None
        r = self.nodo_frente.dato
        if self.nodo_frente == self.nodo_cola:
            self.nodo_cola, self.nodo_frente = None, None
            return r
        self.nodo_frente = self.nodo_frente.sig
        return r

    def __len__(self):
        """Método que nos informa el calculo del tamaño de la cola completa.
        
        :return: Valor que representa el tamaño real de la cola con la variable counter.
        :rtype: int
        """ 

        if self.es_vacia(): return 0
        counter = 1
        nodo_actual = self.nodo_frente
        while nodo_actual is not self.nodo_cola:
            counter += 1
            nodo_actual = nodo_actual.sig
        return counter

    def __str__(self):
        """Método que formatea o convierte en cadena las colas con los datos para su muestra.

        :return: Cadena de las colas con los datos en formato.
        :rtype: cadena String variable cad
        """

        cad = "|{}|:".format(self.prioridad)
        nodo_actual = self.nodo_frente
        if nodo_actual is None:
            cad = ""
            return cad 
        while nodo_actual is not None:            
            cad += str(nodo_actual.dato)+"->"
            nodo_actual = nodo_actual.sig
        return cad[:-2]
            
class NodoOrden:
    """Creamos la clase NodoOrden con la cual podremos crear 
        una cola con sus nodos en orden segun las prioridades colocandolos
        en su respectiva posicion.
        
	Autores: MILER ANDRÉS ESPAÑA | JEAN CARLOS HERNANDEZ BENAVIDES
    """
    def __init__(self, pos, dato) :
        """Constructor de NodoOrden

        :param dato: Recibe este metodo constructor un dato para
        agregarlo en el nodo
        :type dato: objeto
        :param pos: Recibe un entero llamado pos para ubicarlo en esa posicion
        :type pos: int 
        """ 

        self.pos = pos
        self.dato = dato
        self.sig = None

class ListaOrdenada:
    """La ListaOrdenada es una estructura de datos la cual contiene elementos 
    o datos en unos nodos enlazados de forma simple, estos tienen la caracteristica de apuntar al siguiente elemento.
    Los nodos son  objetos pertenecientes a la clase NodoOrden

    Autores: MILER ANDRÉS ESPAÑA | JEAN CARLOS HERNANDEZ BENAVIDES
    """
    
    def __init__(self):
        """__init__ se refiere al Constructor de un objeto de la clase ListaOrdenada.
        --------------------------
        primero es el nodo de cabecera de la lista Ordenada, es una variable con un valor al inicio de None.
        """ 

        self.primero = None

    def append(self, pos, dato):
        """Este método permite adicionar un nuevo dato de forma que ubica el nodo en la cola 
           en la posicion correspondiente.

        :param dato: es el dato a insertarse en alguna posicion de la lista ordenada.
        :type dato: dato
        :param pos: es el otro valor que el metodo recibe ademas del nuevo dato, esta posicion 
        se cuenta de izquierda a derecha desde 0, defaults to 0.
        :type pos: int
        :return: retorno de variable de control para saber si se inserto el nuevo dato correctamente
        :rtype: bool
        """ 

        if pos<1: return False
        if self.primero is None:
            self.primero = NodoOrden(pos, dato)
            return True
        nuevo = NodoOrden(pos,dato)
        if self.primero.pos > pos:
            nuevo.sig = self.primero
            self.primero = nuevo
            return True
        actual = self.primero
        while actual.sig is not None:
            if actual.sig.pos > pos:
                nuevo.sig = actual.sig
                actual.sig = nuevo
                return True
            actual = actual.sig
        if actual.sig is None:
            actual.sig = nuevo
            return True
    
    def __len__(self):
        """Método que nos informa el calculo del tamaño de cualquier lista Ordenanda de colas.
        
        :return: Valor que representa el tamaño real de la lista ordenada en la variable counter.
        :rtype: int
        """

        counter = 0
        n = self.primero
        while n is not None:
            counter += 1
            n = n.sig
        return counter

    def first(self):
        """Este metodo nos permite mostrar el valor o dato en primera posicion de la
        lista ordenada.

        :return: Retorna el valor o dato al ser encontrado.
        si no encuentra nada también retornará que no lo halló o None.
        :rtype: bool, si no lo halla y dato si lo encuentra en la lista Ordenada.
        """

        if self.primero is not None:
            return self.primero.dato
        return None

    def find(self, pos):
        """Este metodo nos permite buscar para encontrar la posicion que necesitemos, 
            puede apuntar o llegar al valor que queremos.

        :param pos: la posicion a encontrar en la lista ordenada para luego regresar el dato ahí ubicado
        :type pos: int al buscar por posicion 
        :return: Retorna el valor hallado en la posicion pos
        si no encuentra nada también retornará que no lo halló
        :rtype: dato si halla la posicion, None si la variable booleana no lo halló
        """ 

        n = self.primero
        while n is not None:
            if n.pos == pos: return n.dato
            n = n.sig
        return None

    def delete(self):
        """Metodo que permite borrar el primero de la lista Ordenada, luego el primero
        de esta pasará a ser el siguiente en la lista.

        :return: Valor que retorna si se eliminó o no el nodo
        :rtype: bool
        """ 

        if self.primero is None: return None
        dato = self.primero.dato
        self.primero = self.primero.sig
        return dato


class ColaDePrioridad:
    """Creamos la clase ColaDePrioridad con la cual podremos crear varias cantidades de
        colas con un nivel o valor de prioridad entre datos, esto con cualquier tipo de
        dato y también usar sus diferentes métodos.

    Autores: MILER ANDRÉS ESPAÑA | JEAN CARLOS HERNANDEZ BENAVIDES  
    """ 

    def __init__(self):
        """__init__ se refiere al Constructor de un objeto de la clase ColaDePrioridad.
        --------------------------
        colas es la creacion de una lista de colas del tipo ListaOrdenada. 
        type guarda cada tipo de objeto que se ingresa o adiciona a la Cola de prioridad
        """

        self.colas = ListaOrdenada() 
        self.type = None

    def es_vacia(self):
        """es_vacia() es un método para determinar si la cola aún no ha recibido algún dato
            o se encuentra en un estado inicial sin valores.

        :return: el return me dará un valor después de verificar si está vacia o no la cola de prioridad.
        :rtype: bool
        """ 

        return (len(self.colas) == 0)

    def encolar(self, prioridad, dato):
        """Este método permite insertar o encolar un nuevo dato a la cola
            tambien puede hacerlo cuando la cola está vacia.
            El primer dato de la cola es el nodo_frente el ultimo es el nodo_cola. 
    
        :param dato:  es el dato a insertarse o a encolarse en la cola como la nueva cola.
        :type dato: dato
        :param prioridad:  es la posicion a encolarse en la cola de prioridad.
        :type prioridad: int
        :return: retorno de variable de control para saber si se inserto o encoló el nuevo dato
        :rtype: bool
        """ 

        if prioridad<1: return False
        if self.type is None: self.type = type(dato)
        if type(dato) is not self.type: return False
        cola = self.colas.find(prioridad)
        if cola:
            cola.encolar(dato)
            return True
        else:
            caux = Cola(prioridad)
            caux.encolar(dato)
            self.colas.append(prioridad, caux)
            return True

    def desencolar(self):
        """desencolar() es un método para borrar o eliminar el valor considerado como primero o el frente de la Cola de prioridad, primero de la lista ordenada que es
            el primero en entrar y el primero que debe salir. El nodo first luego tomará el valor del siguiente nodo.

            :return: el return me dará un valor después de verificar si se borró o no el valor del nodo_frente.
            :rtype: bool
        """

        cola = self.colas.first()
        if cola is not None:
            dato = cola.desencolar()
            if cola.es_vacia():
                self.colas.delete()
            return dato
        return None

    def frente(self):
        """Este metodo nos permite mostrar el valor o dato del first o la el primero de la cola.

        :return: Retorna el valor o dato al ser encontrado.
        si no encuentra nada también retornará que no lo halló o None.
        :rtype: bool, si no lo halla y dato si lo encuentra en la cola de prioridad.
        """ 

        cola = self.colas.first()
        if cola is not None:
            return cola.frente()
        return None

    def __len__(self):
        """Método que nos informa el calculo del tamaño de la cola de prioridad completa.
        
        :return: Valor que representa el tamaño real de la cola de prioridad con la variable counter.
        :rtype: int
        """ 

        if len(self.colas)==0: return 0
        counter = 0
        c = self.colas.primero
        while c is not None:
            counter += len(c.dato)
            c = c.sig
        return counter    

    def __str__(self):
        """Método que formatea o convierte en cadena las colas que se encuentran con los datos en la lista Ordenada de colas para su muestra.

        :return: Cadena de las lista de colas con los datos en formato de cola de prioridad basado en Cola.
        :rtype: cadena string con datos llamada cad usando el formato en el metodo __str__ de la clase Cola
        """

        c = self.colas.primero
        cad = ""
        while c is not None:
            cad += str(c.dato)
            c = c.sig
        return cad
