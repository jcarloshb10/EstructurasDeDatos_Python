from tad.pila_cola.nodos import NodoCola


class Cola:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.type = None
        self.iterador = None

    def es_vacia(self):
        return True if self.inicio is None else False

    def encolar(self, dato):
        if self.es_vacia():
            self.type = type(dato)
            self.inicio = NodoCola(dato)
            self.final = self.inicio
            return True

        if self.type != type(dato):
            return False

        self.final.siguiente = NodoCola(dato)
        self.final = self.final.siguiente
        return True

    def desencolar(self):
        if self.es_vacia():
            return None
        nodo = self.inicio
        self.inicio = self.inicio.siguiente
        return nodo.dato

    @property
    def frente(self):
        if self.es_vacia:
            return None
        return self.inicio.dato

    def __len__(self):
        len = 0
        nodo_actual = self.inicio
        while nodo_actual is not None:
            len += 1
            nodo_actual = nodo_actual.siguiente
        return len

    def __str__(self):
        cadena = ""
        nodo_actual = self.inicio
        while nodo_actual is not None:
            cadena += str(nodo_actual)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual is not None:
                cadena += "-c-"
        return cadena

    def __iter__(self):
        self.iterador = self.inicio
        return self

    def __next__(self):
        if self.iterador is not None:
            nodo = self.iterador
            self.iterador = self.iterador.siguiente
            return nodo.dato
        else:
            raise StopIteration
