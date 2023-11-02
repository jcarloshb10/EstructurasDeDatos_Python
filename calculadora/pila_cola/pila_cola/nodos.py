class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
    def __str__(self):
        return str(self.dato)
class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    def __str__(self):
        return str(self.dato)
