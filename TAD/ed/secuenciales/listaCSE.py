#!/usr/bin/env python
import sys
from ed.secuenciales.nodo import NodoLSE

class ListaCSE:
    """Creamos la clase ListaCSE Lista circular simplemente enlasada con la cual podremos crear 
        una lista con cualquier tipo de
        dato y usar sus diferentes métodos.

	Autor: JEAN CARLOS HERNANDEZ BENAVIDES
    """    

    def __init__(self):
        """__init__ se refiere al Constructor de un objeto de la clase ListaCSE.
        --------------------------
        nodo_cab es el nodo de cabecera, es una variable con un valor al inicio de None.
        nodo_cola es el nodo final o el ultimo en la lista con un valorinicial de None.
        """                
        self.nodo_cab  = None
        self.nodo_cola = None
       
    
    def es_vacia(self):
        """es_vacia() es un método para determinar si la lista circular aún no ha recibido algún dato
            o se encuentra en un estado inicial sin valores.

            :return: el return me dará un valor después de verificar si está vacia o no la lista.
            :rtype: bool
        """        
        return self.nodo_cab == None

    def adicionar(self, nuevo_dato):
        """El metodo adicionar() recibe un nuevo_dato el cuál será añadido a la lista  circular de forma consecutiva.
        
            :param nuevo_dato: dato que recibe el metodo para que lo agregue a la lista.
            :type nuevo_dato: dato
            :return: es quien me verificará si se agregó o no el nuevo_dato a la lista.
            :rtype: bool
        """        
        nodo_nuevo =NodoLSE(nuevo_dato)
        if self.es_vacia():         
            self.nodo_cab = nodo_nuevo
            self.nodo_cola = nodo_nuevo
            nodo_nuevo.sig = self.nodo_cab
            return True
        elif type(nuevo_dato) == type(self.nodo_cab.dato):
            self.nodo_cola.sig = nodo_nuevo
            nodo_nuevo.sig = self.nodo_cab
            self.nodo_cola = nodo_nuevo
        else:        
            return False
        return True

    def insertar(self, pos=0, nuevo_dato=0):
        """Este método permite insertar un nuevo dato de unas maneras ya que se puede insertar o al 
            inicio, medio, final o incluso cuando la lista está vacia. Si la lista circular esta vacia 
            sin importar la posicion el primer nuevo_dato ocupará la posicion 0.
    
        :param nuevo_dato:  es el dato a insertarse en alguna posicion de la lista
        :type nuevo_dato: dato
        :param pos: es el otro valor que el metodo recibe ademas del nuevo dato, esta posicion 
        se cuenta de izquierda a derecha desde 0, defaults to 0.
        :type pos: int
        :return: retorno de variable de control para saber si se inserto el nuevo dato
        :rtype: bool
        """    

        nodo_nuevo = NodoLSE(nuevo_dato)
        if self.es_vacia():
            if pos == 0:
                return self.adicionar(nuevo_dato)
        #elif isinstance(nuevo_dato, type(self.nodo_cab.dato)):
        elif type(nuevo_dato) == type(self.nodo_cab.dato) and type(pos) == type(nuevo_dato):
            if pos == 0:
                nodo_nuevo.sig = self.nodo_cab
                self.nodo_cab = nodo_nuevo
                self.nodo_cola.sig = nodo_nuevo
                return True
            #elif pos == len(self):
                #return self.adicionar(nuevo_dato)
            elif pos > 0:
                nodo_actual = self.nodo_cab
                i = 0
                while i < pos - 1:
                    i += 1
                    nodo_actual = nodo_actual.sig
                if nodo_actual.sig == self.nodo_cab:
                    nodo_nuevo.sig = self.nodo_cab
                    self.nodo_cab = nodo_nuevo
                    self.nodo_cola.sig = nodo_nuevo
                    return True
                else:
                    nodo_auxiliar = nodo_actual.sig
                    nodo_actual.sig = nodo_nuevo
                    nodo_nuevo.sig = nodo_auxiliar
                    return True
        return False
        
    def recorrer(self, sep = " "):
        """Este metodo recorre completamente la lista y en su paso forma una cadena tipo string
            con la cuál va a ser retornada paramostrar la lista circular completa con separadores.

        :return: valor que verifica si se recorrio la lista completa
        :rtype: bool
        :sep: por defectpo es un espacio pero es el delimitador entre cada valor de la lista circular
        :rtype: str
        """        
        
        string  = ""
        nodo_actual = self.nodo_cab
        while self.nodo_cab is not None:
            if nodo_actual == self.nodo_cola:
                string += str(self.nodo_cola.dato)
                
                break
            string += str(nodo_actual.dato) + sep      
            nodo_actual = nodo_actual.sig   
        
        return string

    def buscar(self, dato_buscar):
        """Este metodo nos permite buscar para encontrar un dato que necesitemos.

        :param dato_buscar: el dato a encontrar
        :type dato_buscar: dato al ser buscado en la lista
        :return: Retorna el valor o dato al ser encontrado.
        si no encuentra nada también retornará que no lo halló o None
        :rtype: bool si no lo halla y dato si lo encuentra en la lista
        """        
        nodo_actual = self.nodo_cab
        while self.nodo_cab is not None and nodo_actual.dato != dato_buscar:
            if nodo_actual == self.nodo_cola:
                break
            nodo_actual = nodo_actual.sig
        if self.nodo_cab is not None and nodo_actual.dato == dato_buscar:
            return nodo_actual.dato
        return None
  
    def buscar_cuantos(self, dato_buscar):
        
        """Este método permite encontrar y contar la cantidad total de veces que un dato_buscar o 
        el dato que queremos se encuentra en la lista circular.

        :return: cantidad es la variable booleana que retorna el numero de veces que se encuentra 
        el dato_buscar en la lista circcular.
        :rtype: bool
       :cantidad: es un contador usado para incrementaarse en una unidad cada vezque 
       encuentre coincidencias con el dato en la lista circular. 
       :rtype: int
        """        

        cantidad = 0
        nodo_actual = self.nodo_cab
        for _ in range(len(self)):
            if self.nodo_cab == self.nodo_cola:
                if dato_buscar == nodo_actual.dato:
                    cantidad += 1
            else:
                if nodo_actual.dato == dato_buscar:
                    cantidad += 1

            nodo_actual = nodo_actual.sig
        
        return cantidad


    def borrar(self, item, por_pos=False):

        """El método borrar dontiene dos formas para eliminar un elemento de la lista circular.
        Por posicion recibiendo el metodo ademas un dato entero que sería la posicion del nodo 
        a eliminar o tambien, por item, siendo en ese caso falsa la condicion del por_pos y simplemente 
        buscará en la lista todas las coincidencias con el item y las borrará.

        :return: retorna si el metodo ha borrado el nodo con True o False si no lo ha hecho
        :rtype: bool
        """

        if  not self.es_vacia():
            #por_pos
            if por_pos is True:
                if item == 0:
                    if len(self) != 1:
                        self.nodo_cab = self.nodo_cab.sig
                        self.nodo_cola.sig = self.nodo_cab
                        return True
                    else:
                        self.nodo_cab = None
                        return True
                elif item > 0:
                    nodo_actual = self.nodo_cab
                    cont = 0
                    while cont < item - 1:
                        nodo_actual = nodo_actual.sig
                        cont += 1
                    if item == len(self) - 1:
                        self.nodo_cola = nodo_actual
                    if nodo_actual.sig == self.nodo_cab:
                        self.nodo_cab = self.nodo_cab.sig
                        self.nodo_cola.sig = self.nodo_cab
                    else:
                        nodo_actual.sig = nodo_actual.sig.sig
                        self.nodo_cola.sig = self.nodo_cab
                        return True
            else:
                #por dato
                cont = 0
                cont2 = 0
                if self.nodo_cab.dato == item:
                    self.nodo_cab = self.nodo_cab.sig
                    self.nodo_cola.sig = self.nodo_cab        
                    if len(self) == 1:
                        self.nodo_cab = None
                        self.nodo_cola = self.nodo_cab
                    cont2 += 1     
                if self.nodo_cab != self.nodo_cola:              
                    nodo_actual = self.nodo_cab
                    while nodo_actual != self.nodo_cola  :                 
                        if nodo_actual.sig.dato == item :                      
                            if nodo_actual.sig == self.nodo_cola:
                                self.nodo_cola = nodo_actual
                            nodo_actual.sig = nodo_actual.sig.sig
                            self.nodo_cola.sig = self.nodo_cab
                            cont2 += 1
                            if nodo_actual.sig.dato == item:
                                if nodo_actual.sig == self.nodo_cola:
                                    self.nodo_cola = nodo_actual
                                nodo_actual.sig = nodo_actual.sig.sig
                                self.nodo_cola.sig = self.nodo_cab
                                cont2 += 1
                        else:
                            cont += 1                       
                        nodo_actual = nodo_actual.sig
                    if (cont == len(self) -1):
                        print(len(self))
                        return False
                            
                if cont2 != 0:
                    return True
        else:            
            return False

    
    def ruleta_rusa(self, pos):

        """El metodo de la ruleta_rusa muestra el valor que se encuentra en la posicion de la lista circular que el
        metodo ha recibido.

        :return: retorna el dato en caso de encontrar esa posicion en la lista circular, del caso contrario retorna None
        :rtype: bool
        """

        nodo_actual = self.nodo_cab
        cont = 0       
        while self.nodo_cab is not None and cont != pos:
            if self.nodo_cola == nodo_actual:
                return None
            nodo_actual = nodo_actual.sig
            cont += 1
        if nodo_actual is not None:
            return nodo_actual.dato
        return None


    def __len__(self):
        """Método que nos informa el calculo del tamaño de la lista circular.
        
        :return: Valor que representa el tamaño real de la lista.
        :rtype: int
        """        

        cont = 0
        if not self.es_vacia():
            cont += 1
            nodo_actual = self.nodo_cab.sig
            while nodo_actual is not None and nodo_actual != self.nodo_cab:
                cont += 1
                nodo_actual = nodo_actual.sig
        return cont


    def __str__(self):
        """Método que formatea o convierte en cadena la lista con los datos para su muestra.

        :return: Cadena de la lista con los datos en formato.
        :rtype: dato
        """        
        string = ""
        for i in self:
            string += str(i) + "\n"
        return string


    def __iter__(self):
        """Método que nos da una direccion que por medio de esas unidades pueden entrar en los nodos
        de una lista circular y recorrerla como un ciclo for sin problema, para luego tambien extraer la informacion.

        :return: variable que indica si se recorrio la lista.
        :rtype:  generador
        :yield: variable yield que nos retorna un generadoor o un espacio en la memoria.
        """    
        if not self.es_vacia():
            yield self.nodo_cab.dato
            nodo_actual = self.nodo_cab.sig
            while nodo_actual != self.nodo_cab:
                yield nodo_actual.dato
                nodo_actual = nodo_actual.sig

        

'''#MI TEST LISTACSE
if __name__ == "__main__":
    
    lista_numeros = ListaCSE()
    print(lista_numeros.adicionar(10))
    print(lista_numeros.adicionar(70))
    print(lista_numeros.adicionar(70))
    print(lista_numeros.adicionar(80))
    print(lista_numeros.adicionar(70))
    print(lista_numeros.adicionar(90))
    print(lista_numeros.recorrer('-'))
    #print(lista_numeros.ruleta_rusa(4))
    print(lista_numeros.borrar(70, False))
    print(lista_numeros.recorrer('-'))
    #print(lista_numeros.borrar(30,False))
    #print(lista_numeros.recorrer('-'))
    #print(lista_numeros.borrar(30,False))
    #print(lista_numeros.recorrer('-'))
    print(lista_numeros.adicionar(40))
    print(lista_numeros.adicionar(25))
    print(lista_numeros.adicionar(45))
    print(lista_numeros.adicionar(35))
    print(lista_numeros.adicionar(25))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.borrar(2, False))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.borrar(25, False))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.buscar(25))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.buscar(40))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.ruleta_rusa(5))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.ruleta_rusa(30))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.__iter__())
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.buscar_cuantos(35))
    print(lista_numeros.recorrer('-'))
    print(lista_numeros.borrar(35, False))
    print(lista_numeros.recorrer('-'))'''