from tad.listas.nodos import NodoListaDoblementeEnlazada as Nodo


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cab: Nodo = None
        self.actual: Nodo = None

    def es_vacia(self) -> bool:
        return self.cab is None

    def anadir(self, nuevo_dato, final=True, pos=0) -> bool:
        if self.es_vacia():
            self.cab = Nodo(nuevo_dato)
            self.actual = self.cab
            return True
        elif isinstance(nuevo_dato, type(self.cab.dato)):
            if final:
                return self.__anadir_al_final(nuevo_dato)
            elif pos == 0:
                return self.__anadir_al_inicio(nuevo_dato)
            elif pos > 0:
                nodo = self.cab
                for i in range(pos - 1):
                    nodo = nodo.sig

                nuevo_nodo = Nodo(nuevo_dato)
                nuevo_nodo.ant = nodo
                nuevo_nodo.sig = nodo.sig

                if nodo.sig == self.actual:
                    self.actual = nuevo_nodo

                nodo.sig.ant = nuevo_nodo
                nodo.sig = nuevo_nodo

                return True

    def __ultimo(self):
        ultimo = None
        for i in self:
            ultimo = i
        return ultimo

    def __anadir_al_final(self, nuevo_dato):
        ultimo = self.__ultimo()

        nuevo_nodo = Nodo(nuevo_dato)
        nuevo_nodo.ant = ultimo
        ultimo.sig = nuevo_nodo

        return True

    def __anadir_al_inicio(self, nuevo_dato):
        nuevo_nodo = Nodo(nuevo_dato)
        nuevo_nodo.sig = self.cab
        self.cab.ant = nuevo_nodo

        if self.cab == self.actual:
            self.actual = nuevo_nodo

        self.cab = nuevo_nodo
        return True

    def suprimir(self, item, por_dato=False, todos=True) -> bool:
        suprimido = False

        if not self.es_vacia():
            if por_dato:
                if todos:
                    while self.__suprimir_por_dato(item):
                        suprimido = True
                else:
                    suprimido = self.__suprimir_por_dato(item)
            else:
                suprimido = self.__suprimir_por_posicion(pos)

        return suprimido

    def __suprimir_por_dato(self, dato) -> bool:
        nodo = self.cab

        if nodo.dato == dato:
            self.cab = nodo.sig
            return True

        while nodo.sig:
            if nodo.sig.dato == dato:
                nodo.sig.sig.ant = nodo
                nodo.sig = nodo.sig.sig
                return True
            nodo.sig = nodo.sig.sig

        return False

    def __suprimir_por_posicion(self, pos) -> bool:
        if pos == 0:
            pass
        elif 0 < pos < len(self):
            nodo = self.cab
            for i in range(pos - 1):
                nodo = nodo.sig
            nodo.sig.sig.ant = nodo
            nodo.sig = nodo.sig.sig

        return False

    def localizar(self, dato) -> object:
        for i in self:
            if i.dato == dato:
                return i.dato

    def explorar(self) -> None:
        for i in self:
            print(i)

    def avanzar(self) -> object:
        if self.actual.sig:
            self.actual = self.actual.sig
        return self.actual

    def retroceder(self) -> object:
        if self.actual.ant:
            self.actual = self.actual.ant
        return self.actual

    def __str__(self) -> str:
        cadena = ''
        for i in self:
            cadena += str(i)
            if i != self.__ultimo():
                cadena += ' '
        return cadena

    def __len__(self) -> int:
        len = 0
        for i in self:
            len += 1
        return len

    def __iter__(self):
        nodo = self.cab
        while nodo:
            yield nodo
            nodo = nodo.sig
