from tad.listas.nodos import NodoListaSimplementeEnlazada as Nodo


class ListaCircularSimplementeEnlazada:
    def __init__(self):
        self.cab: Nodo = None
        self.cola: Nodo = self.cab

    def es_vacia(self) -> bool:
        """Retorna True si la lista esta vacia, de lo contrario False"""
        return self.cab is None

    def añadir(self, nuevo_dato, final=True, pos_rel=0) -> bool:
        """Añade un nuevo nodo con un dato, lo hace al final por posicion"""
        if self.es_vacia():
            if final or (not final and pos_rel == 0):
                self.cab = Nodo(nuevo_dato)
                self.cola = self.cab
                self.cola.sig = self.cab
                return True

        elif isinstance(nuevo_dato, type(self.cab.dato)):
            if final:
                return self.__añadir_al_final(nuevo_dato)
            elif pos_rel == 0:
                return self.__añadir_al_inicio(nuevo_dato)
            elif pos_rel > 0:
                nodo = self.cab

                for i in range(pos_rel - 1):
                    nodo = nodo.sig

                nuevo_nodo = Nodo(nuevo_dato)
                nodo.sig, nodo.sig.sig = nuevo_nodo, nodo.sig

                if nuevo_nodo.sig == self.cab:
                    self.cab = nodo.sig
                return True

        return False

    def __añadir_al_final(self, nuevo_dato):
        nodo = Nodo(nuevo_dato)
        nodo.sig = self.cab
        self.cola.sig = nodo
        self.cola = nodo
        return True

    def __añadir_al_inicio(self, nuevo_dato):
        nodo = Nodo(nuevo_dato)
        nodo.sig = self.cab
        self.cab = nodo
        self.cola.sig = self.cab
        return True

    def suprimir(self, item, por_dato=True, todos=True) -> bool:
        """Elimina el o los nodos con el dato o en la posicion indicada"""
        suprimido = False

        if por_dato:
            if todos:
                while not self.es_vacia() and self.__suprimir_por_dato(item):
                    suprimido = True
            elif not self.es_vacia():
                suprimido = self.__suprimir_por_dato(item)
        elif not self.es_vacia():
            suprimido = self.__suprimir_por_posicion(item)

        return suprimido

    def __suprimir_por_dato(self, dato) -> bool:
        """Elimina el nodo indicado por el dato"""
        if self.cab.dato == dato:
            if self.cab == self.cola:
                self.cab = None
                self.cola = self.cab
            else:
                self.cab = self.cab.sig
                self.cola.sig = self.cab
            return True

        nodo = self.cab

        while nodo.sig:
            if nodo.sig.dato == dato:
                aux = nodo.sig
                nodo.sig = nodo.sig.sig

                if aux == self.cola:
                    self.cola = nodo

                return True

            if nodo.sig == self.cola.sig:
                break
            nodo = nodo.sig

        return False

    def __suprimir_por_posicion(self, pos) -> bool:
        """Elimina el nodo indicado por la posicion"""
        nodo = self.cab

        if pos == 0:
            if self.cab == self.cola:
                self.cab = None
                self.cola = self.cab
            else:
                self.cab = nodo.sig
            return True
        elif pos > 0:
            for i in range(pos - 1):
                nodo = nodo.sig

            aux = nodo.sig
            nodo.sig = nodo.sig.sig

            if aux == self.cola:
                self.cola = nodo
            return True

        return False

    def localizar(self, dato) -> object:
        """Retorna el nodo si esta en la lista"""
        for i in self:
            if i.dato == dato:
                return i.dato

    def suerte(self, pos_rel) -> object:
        """Retorna el nodo si la posicion existe en la lista"""
        if pos_rel >= 0:
            nodo = self.cab
            for i in range(pos_rel):
                nodo = nodo.sig
            return nodo.dato

        return None

    def explorar(self) -> None:
        """Imprime en consola los nodos convertidos a cadena"""
        for i in self:
            print(i)

    def __str__(self) -> str:
        """Retorna una cadena de caracteres con todos sus nodos"""
        cadena = ''
        for nodo in self:
            cadena += str(nodo)
            # if nodo != self.cola:
            #     cadena += ' '
        return cadena

    def __len__(self) -> int:
        """Retorna la cantidad de nodos en la lista"""
        len = 0
        for i in self:
            len += 1
        return len

    def __iter__(self) -> object:
        """Permite que la lista sea iterable: retorna cada uno de sus nodos"""
        nodo = self.cab

        if nodo and nodo == self.cola:
            yield nodo
        else:
            while nodo:
                yield nodo
                nodo = nodo.sig
                if nodo == self.cola.sig:
                    break
