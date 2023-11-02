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

    '''def adicionar(self,prioridad,nuevo_dato):
        """El metodo adicionar() recibe un nuevo_dato el cuál será añadido a la lista de forma consecutiva.
        
            :param nuevo_dato: dato que recibe el metodo para que lo agregue a la lista.
            :type nuevo_dato: dato
            :return: es quien me verificará si se agregó o no el nuevo_dato a la lista.
            :rtype: bool
        """        
        
        if self.es_vacia():
            #print("adicionado inicio")
            self.nodo_cab = NodoPrioridad(prioridad,nuevo_dato)
            return True

        elif type(self.nodo_cab.dato) == type(nuevo_dato):
            print("AAAA")
            nodo_actual = self.nodo_cab
            #ciclo que permite recorrear  lista hasta final
            while nodo_actual.sig is not None:
                nodo_actual = nodo_actual.sig
                
            nodo_actual.sig = NodoPrioridad(prioridad,nuevo_dato)
            #agregado
            return True
        else:
            #"ERROR! TIPO DE DATO NO HOMOGENEO"
            return False
        return False'''

    def insertar(self,prioridad, nuevo_dato):
        """Este método permite insertar un nuevo dato de unas maneras ya que se puede insertar o al 
            inicio, medio, final o incluso cuando la lista está vacia. Si la lista esta vacia ocupará el dato la posicion 0.

        :param nuevo_dato:  es el dato a insertarse en alguna posicion de la lista
        :type nuevo_dato: dato
        :param pos: es el otro valor que el motodo recibe ademas del nuevo dato, esta posicion 
        se cuenta de izquierda a derecha desde 0, defaults to 0.
        :type pos: int
        :return: retorno de variable de control para saber si se inserto el nuevo dato
        :rtype: bool
        """        
        #self.lista_colas = ListaE()
        
        if type(prioridad) == int and prioridad >= 1:
            nodo_nuevo = NodoPrioridad(prioridad,nuevo_dato)
            if self.es_vacia():
                self.nodo_cab = self.nodo_cola = nodo_nuevo
                return True
            elif type(nuevo_dato) == type(self.nodo_cab.dato):
                self.__insertar(prioridad,nuevo_dato)
                return True
        return False

    def __insertar(self,prioridad,nuevo_dato):
        nodo_actual = self.nodo_cab
        cnt = 0
        while nodo_actual:
            if prioridad < nodo_actual.prioridad:
                break
            else:
                nodo_actual = nodo_actual.sig
                cnt += 1

        nodo_nuevo = NodoPrioridad(prioridad,nuevo_dato)
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
        
    def recorrer(self):
        """Este metodo recorre completamente la lista y en su paso los muestra en pantalla

        :return: valor que verifica si se recorrio la lista completa
        :rtype: bool
        """        

        nodo_actual = self.nodo_cab
        #ciclo que permite recorrer  lista hasta final
        while nodo_actual is not None:      
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.sig                
        return True         

    def buscar(self, item, por_dato=False):
        """Este metodo nos permite buscar para encontrar un dato o la posicion que necesitemos, 
            puede apuntar o llegar al valor que queremos.

        :param item: la posicion o el dato a encontrar
        :type item: int al buscar por posicion ; dato al buscar por dato
        :param por_dato: Es la variable que controla la forma de la busqueda o avisa que
        esta se ha por dato o item, defaults to False
        :type por_dato: bool
        :return: Retorna el valor hallado de ambas formas, ya sea un item o una posicion
        si no encuentra nada también retornará que no lo halló
        :rtype: dato si es por dato o posicion, None si la variable booleana no lo halló
        """        

        if por_dato: 
            nodo_actual = self.nodo_cab
            #print(type(item))
            while nodo_actual:
                if nodo_actual and str(nodo_actual.dato)  != str(item):                
                    #print(nodo_actual)
                    nodo_actual = nodo_actual.sig                
                else:
                    #print(nodo_actual.dato)
                    nodo_actual = None
                    return True
            return None
        
        if item < 0:
            return None

        else:
            cont = 1
            nodo_actual = self.nodo_cab
            if item == 0:
                return nodo_actual.dato
            else:
                item = item + 1
                while cont < item and nodo_actual:
                    cont += 1
                    nodo_actual = nodo_actual.sig
                try:
                    return nodo_actual.dato
                except:                    
                    print("Posicion no valida")
                    return False
                
            return None

    '''def borrar_pos(self, pos):
        """Metodo que permite borrar con la posicion que le llega un nodo con cualquier dato.

        :param pos: Posicion que recibe el metodo para eliminar despues de buscarla en la lista.
        :type pos: int
        :return: Valor que retorna si se eliminó o no el nodo
        :rtype: bool
        """        

        nodo_actual = self.nodo_cab
        cr_pos = 0
        
        while cr_pos < pos and nodo_actual:
            cr_pos += 1
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig

        if nodo_actual:
            if self.nodo_cab is nodo_actual:
                self.nodo_cab = self.nodo_cab.sig
            else:
                nodo_anterior.sig = nodo_actual.sig
            return True
        return False

    def borrar(self, dato_borrar):
        """Metodo que me permite eliminar un nodo con toda la informacion con el dato que contiene

        :param dato_borrar: dato a borrar dentro de la lista
        :type dato_borrar: dato
        :return: Valor que retorna con la informacion verdadera o falsa de la eliminacion
        :rtype: bool
        """        

        bandera = False
        if not self.es_vacia():
            if self.nodo_cab.dato == dato_borrar:
                self.nodo_cab = self.nodo_cab.sig
                bandera = True
            else:
                nodo_actual = self.nodo_cab
                while nodo_actual is not None:
                    if nodo_actual.sig is not None:
                        if nodo_actual.sig.dato == dato_borrar:
                            nodo_actual.sig = nodo_actual.sig.sig
                            bandera = True
                            if not all:
                                break
                    nodo_actual = nodo_actual.sig
        return bandera'''

    def __len__(self):
        """Método que nos informa el calculo del tamaño de cualquier lista.
        
        :return: Valor que representa el tamaño real de la lista.
        :rtype: int
        """        

        cont = 0
        nodo_actual = self.nodo_cab
        while nodo_actual is not None:
            cont += 1
            nodo_actual = nodo_actual.sig
        return cont

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

    def __iter__(self):
        """Método que nos da una direccion que por medio de esas unidades pueden entrar en los nodos
        de una lista y recorrerla sin problema, para luego tambien extraer la informacion.

        :return: variable que indica si se recorrio la lista.
        :rtype:  generador
        :yield: variable yield que nos retorna un generadoor o un espacio en la memoria.
        """        
        nodo_actual = self.nodo_cab
        while nodo_actual:
            yield nodo_actual
            nodo_actual = nodo_actual.sig
        return True

        
#Mi Test
if __name__ == "__main__":
    
    lista_numeros = ListaE()
    print("HHH")
    print(lista_numeros.insertar(5,10))
    #print(lista_numeros.insertar(6,10,1))
    print(lista_numeros.insertar(6,15))
    print(lista_numeros.insertar(1,100))
    print(lista_numeros.insertar(4,50))
    print(lista_numeros.recorrer())

    print(lista_numeros.insertar(3,35))
    print(lista_numeros.insertar("HOLA",5))
    print(lista_numeros.insertar(9.45,5))
    print(lista_numeros.insertar(6,20))
    print(lista_numeros.recorrer())
    print(lista_numeros.insertar(10, 1))
    print(lista_numeros.recorrer())
    '''print(lista_numeros.adicionar(20))
    print(lista_numeros.insertar(15, 1))
    print(lista_numeros.adicionar(1))
    print(lista_numeros.recorrer())
    #print(lista_numeros.insertar(9, 2))
    #print(lista_numeros.recorrer())
    print(lista_numeros.buscar(6,True))
    print(lista_numeros.recorrer())
    print(lista_numeros.borrar_pos(3))
    print(lista_numeros.recorrer())
    print(lista_numeros.borrar(15))
    print(lista_numeros.recorrer())
    print(lista_numeros.__len__())
    print(lista_numeros.__str__())
    print(lista_numeros.__iter__())'''