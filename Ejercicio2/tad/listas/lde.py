from tad.listas.nodos import NodoListaDoblementeEnlazada


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cab = None
        self.fin = None
        self.iterador = None
        self.actual = None
        self.type = None

    def es_vacia(self):  # bool
        return self.cab is None

    def añadir(self, nuevo_dato, final=True, pos=0):  # bool
        if self.es_vacia():
            self.cab = NodoListaDoblementeEnlazada(nuevo_dato)
            self.fin = self.cab
            self.type = type(nuevo_dato)
            return True
        if self.type == type(nuevo_dato) and pos >= 0 and pos < self.__len__():
            if final:
                self.fin.siguiente = NodoListaDoblementeEnlazada(nuevo_dato)
                self.fin.siguiente.anterior = self.fin
                self.fin = self.fin.siguiente
            else:
                if pos == 0:
                    tmp = self.cab
                    self.cab = NodoListaDoblementeEnlazada(nuevo_dato)
                    tmp.anterior = self.cab
                    self.cab.siguiente = tmp
                else:
                    indice = 0
                    nodo_anterior = self.cab
                    while indice < pos:
                        nodo_anterior = nodo_anterior.siguiente
                        indice = indice+1

                    nodo_siguiente = nodo_anterior.siguiente
                    nodo_anterior.siguiente = NodoListaDoblementeEnlazada(nuevo_dato)
                    nodo_anterior.siguiente.siguiente = nodo_siguiente
                    nodo_siguiente.anterior = nodo_anterior.siguiente
                    nodo_siguiente.anterior.anterior = nodo_anterior
            return True
        else:
            return False

    def suprimir(self, item, por_dato=False, todos=True):  # bool
        nodo_anterior = None
        nodo_eliminar = self.cab

        if self.es_vacia():
            return False

        if por_dato:
            nodo_eliminar = self.__locNodo(item)
            nodo_anterior = nodo_eliminar.anterior if nodo_eliminar is not None else None
        else:
            indice = 0
            while nodo_eliminar is not None and indice != item:
                nodo_eliminar = nodo_eliminar.siguiente
                indice = indice+1
            nodo_anterior = nodo_eliminar.anterior if nodo_eliminar is not None else None
        if nodo_eliminar is not None:
            while nodo_eliminar is not None:
                if nodo_eliminar is self.fin and self.cab is self.fin:
                    self.cab = None
                    self.fin = None
                    self.iterador = None
                    self.actual = None
                    self.type = None
                elif nodo_eliminar is self.fin:
                    if nodo_eliminar is self.actual:
                        self.retroceder()
                    nodo_anterior.siguiente = None
                    self.fin = nodo_anterior
                elif nodo_eliminar is self.cab:
                    if nodo_eliminar is self.actual:
                        self.avanzar()
                    self.cab = nodo_eliminar.siguiente
                    nodo_eliminar.siguiente.anterior = None
                else:
                    if nodo_eliminar is self.actual:
                        self.avanzar()
                    nodo_anterior.siguiente = nodo_eliminar.siguiente
                    nodo_eliminar.siguiente.anterior = nodo_anterior
                if todos:
                    nodo_eliminar = self.__locNodo(item)
                    nodo_anterior = nodo_eliminar.anterior if nodo_eliminar is not None else None
                else:
                    break
            return True
        else:
            return False

    def __locNodo(self, dato_localizar):
        nodo_localizar = self.cab
        while nodo_localizar is not None and nodo_localizar.dato != dato_localizar:
            nodo_localizar = nodo_localizar.siguiente
        return nodo_localizar

    def localizar(self, dato_localizar):  # object/None
        return self.__locNodo(dato_localizar).dato

    def explorar(self, inversa=False):  # None
        nodo_actual = self.cab
        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = nodo_actual.siguiente

    def avanzar(self):  # object/None
        if self.actual is self.fin:
            return self.actual.dato
        elif self.actual is None:
            self.actual = self.cab
        else:
            self.actual = self.actual.siguiente
        return self.actual.dato

    def retroceder(self):  # object/None
        if self.actual is not self.cab and self.actual is not None:
            self.actual = self.actual.anterior
        return self.actual.dato

    def __str__(self):  # str
        cadena = ""
        nodo_actual = self.cab
        while nodo_actual is not None:
            cadena = cadena+str(nodo_actual.dato)
            if nodo_actual is not self.fin:
                cadena = cadena+" "
            nodo_actual = nodo_actual.siguiente
        return cadena

    def __len__(self):  # int
        len = 0
        nodo_actual = self.cab
        while nodo_actual is not None:
            nodo_actual = nodo_actual.siguiente
            len = len+1
        return len

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
