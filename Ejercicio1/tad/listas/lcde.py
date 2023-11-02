from tad.listas.nodos import NodoListaDoblementeEnlazada as Nodo


class ListaCircularDoblementeEnlazada:
    def __init__(self):
        self.cab: Nodo = None
        self.cola: Nodo = self.cab

    def es_vacia(self):
        return self.cab is None

    def añadir(self, nuevo_dato):
        pass

    def suprimir(self, item, por_dato=True, todos=True):
        pass

    def localizar(self, dato):
        pass

    def explorar(self):
        for i in self:
            print(i)

    def avanzar(self):
        pass

    def retroceder(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass
