class NodoListaSimplementeEnlazada:
    def __init__(self, dato):
        self.dato = dato
        self.sig: NodoListaSimplementeEnlazada = None

    def __str__(self):
        return str(self.dato)


class NodoListaDoblementeEnlazada(NodoListaSimplementeEnlazada):
    def __init__(self, dato):
        NodoListaSimplementeEnlazada.__init__(self, dato)
        self.sig: NodoListaDoblementeEnlazada = None
        self.ant: NodoListaDoblementeEnlazada = None
