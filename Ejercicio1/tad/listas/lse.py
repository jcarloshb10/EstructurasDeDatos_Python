from tad.listas.nodos import NodoListaSimplementeEnlazada as Nodo


class ListaSimplementeEnlazada:
    def __init__(self):
        self.cab: Nodo = None
        self.fin: Nodo = self.cab

    def __iter__(self):
        nodo = self.cab
        while nodo:
            yield nodo.dato
            nodo = nodo.sig

    def __str__(self):
        cadena = ''
        for i in self:
            cadena += str(i) + ' '
        return cadena[: len(cadena) - 1]

    def __len__(self):
        len = 0
        for i in self:
            len += 1
        return len

    def es_vacia(self):
        return self.cab is None

    def añadir(self, dato, final: bool = True, pos: int = 0):
        if self.es_vacia():
            self.cab = Nodo(dato)
            self.fin = self.cab
            return True
        elif isinstance(dato, type(self.cab.dato)):
            if final:
                self.fin.sig = Nodo(dato)
                self.fin = self.fin.sig
                return True
            elif pos == 0:
                self.cab, self.cab.sig = Nodo(dato), self.cab
                return True
            elif pos > 0:

                nodo = self.cab
                for i in range(pos - 1):
                    nodo = nodo.sig

                nuevo_nodo = Nodo(dato)
                if nodo.sig == self.fin.sig:
                    self.fin = nuevo_nodo
                nodo.sig, nodo.sig.sig = nuevo_nodo, nodo.sig

                return True
        return False

    def suprimir(self, item, dato=True):
        if not self.es_vacia():
            if dato:  # suprimir por dato
                nodo = self.cab

                if nodo.dato == item:
                    self.cab = nodo.sig
                    return True

                while nodo.sig:
                    if nodo.sig.dato == item:

                        if nodo.sig == self.fin:
                            self.fin = nodo

                        nodo.sig = nodo.sig.sig
                        return True
                    else:
                        nodo = nodo.sig
            else:  # suprimir por posicion
                # pos = item
                # c = 0
                # if pos != 0:
                #     node = self.cab
                #     while node:
                #         if c == pos - 1 and node.sig:
                #             node.sig = node.sig.sig
                #             break
                #         else:
                #             c += 1
                #             node = node.sig
                # else:
                #     self.cab = self.cab.sig
                pos = item
                nodo = self.cab
                for i in range(pos - 1):
                    nodo = nodo.sig
                if nodo.sig == self.fin:
                    self.fin = nodo
                nodo.sig = nodo.sig.sig
                return True
        return False

    def explorar(self):
        for i in self:
            print(i)

    def localizar(self, dato):
        for i in self:
            if i == dato:
                return i
