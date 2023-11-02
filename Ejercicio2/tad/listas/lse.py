from tad.listas.nodos import NodoListaSimplementeEnlazada


class ListaSimplementeEnlazada:
    def __init__(self):
        self.cab = None
        self.fin = None
        self.iterador = None
        self.type = None

    def es_vacia(self):
        return self.cab is None

    def añadir(self, nuevo_dato, final=True, pos=0):
        if self.es_vacia():
            self.cab = NodoListaSimplementeEnlazada(nuevo_dato)
            self.fin = self.cab
            self.type = type(nuevo_dato)
            return True
        if self.type != type(nuevo_dato):
            return False
        if final or pos >= self.__len__()-1:
            self.fin.siguiente = NodoListaSimplementeEnlazada(nuevo_dato)
            self.fin = self.fin.siguiente
            return True
        if pos > self.__len__():
            return False

        anterior = self.cab
        indice = 0
        while indice < pos:
            anterior = anterior.siguiente
            indice = indice+1
        tmp = anterior.siguiente
        anterior.siguiente = NodoListaSimplementeEnlazada(nuevo_dato)
        anterior.siguiente.siguiente = tmp
        return True

    def explorar(self):
        nodo_actual = self.cab
        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = nodo_actual.siguiente

    def suprimir(self, item, por_dato=True):
        nodo_anterior = None
        nodo_eliminar = self.cab

        if self.es_vacia():
            return False

        if por_dato:
            while nodo_eliminar is not None and nodo_eliminar.dato != item:
                if nodo_eliminar.siguiente is not None and nodo_eliminar.siguiente.dato == item:
                    nodo_anterior = nodo_eliminar
                nodo_eliminar = nodo_eliminar.siguiente
        else:
            indice = 0
            while nodo_eliminar is not None and indice != item:
                if nodo_eliminar.siguiente is not None and indice+1 == item:
                    nodo_anterior = nodo_eliminar
                nodo_eliminar = nodo_eliminar.siguiente
                indice = indice+1

        if nodo_eliminar is not None:
            if nodo_eliminar is self.fin:
                self.fin = nodo_anterior
            if nodo_anterior is None:
                self.cab = nodo_eliminar.siguiente
            else:
                nodo_anterior.siguiente = nodo_eliminar.siguiente
            return True
        else:
            return False

    def localizar(self, dato_localizar):
        nodo_localizar = self.cab
        while nodo_localizar is not None and nodo_localizar.dato != dato_localizar:
            nodo_localizar = nodo_localizar.siguiente
        return nodo_localizar if nodo_localizar is not None else None

    def __str__(self):
        cadena = ""
        nodo_actual = self.cab
        while nodo_actual is not None:
            cadena = cadena+str(nodo_actual.dato)
            if nodo_actual is not self.fin:
                cadena = cadena+" "
            nodo_actual = nodo_actual.siguiente
        return cadena

    def __iter__(self):
        self.iterador = self.cab
        return self

    def __next__(self):
        if self.iterador is not None:
            nodo = self.iterador
            self.iterador = self.iterador.siguiente
            return nodo.dato
        else:
            raise StopIteration

    def __len__(self):
        len = 0
        nodo_actual = self.cab
        while nodo_actual is not None:
            len += 1
            nodo_actual = nodo_actual.siguiente
        return len
