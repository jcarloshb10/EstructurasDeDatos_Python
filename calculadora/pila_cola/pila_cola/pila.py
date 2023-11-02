from tad.pila_cola.nodos import NodoPila


class Pila:
    def __init__(self):
        self.inicio = None
        self.type = None
        self.iterador = None

    def es_vacia(self):
        return True if self.inicio is None else False

    def apilar(self, dato):
        if self.es_vacia():
            self.type = type(dato)
            self.inicio = NodoPila(dato)
            return True

        if self.type != type(dato):
            return False
        nodo = NodoPila(dato)
        nodo.anterior = self.inicio
        self.inicio = nodo
        return True

    def desapilar(self):
        if self.es_vacia():
            return None
        nodo = self.inicio
        self.inicio = self.inicio.anterior
        return nodo.dato

    @property
    def cima(self):
        if self.es_vacia:
            return None
        return self.inicio.dato

    def __len__(self):
        len = 0
        nodo_actual = self.inicio
        while nodo_actual is not None:
            len += 1
            nodo_actual = nodo_actual.anterior
        return len

    def __str__(self):
        cadena = ""
        nodo_actual = self.inicio
        while nodo_actual is not None:
            cadena += str(nodo_actual)
            nodo_actual = nodo_actual.anterior
            if nodo_actual is not None:
                cadena += "-p-"
        return cadena

    def __iter__(self):
        self.iterador = self.inicio
        return self

    def __next__(self):
        if self.iterador is not None:
            nodo = self.iterador
            self.iterador = self.iterador.anterior
            return nodo.dato
        else:
            raise StopIteration
