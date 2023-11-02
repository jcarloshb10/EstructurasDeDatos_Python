class NodoArbolBinario:
    """La clase NodoArbolBinario permite almacenar las claves dentro de un nodo.
    Autores: JEAN CARLOS HERNANDEZ | ANDRÉS ESPAÑA
    """  

    def __init__(self, clave):
        """Constructor de NodoArbolBinario

        Args:
            clave (objeto/valor): la clave es el contenido del nodo.
        """    

        self.clave = clave
        self.izq = None
        self.der = None

    def __str__(self):
        """Método que retorna los datos del nodo en forma de texto.

        Returns:
            str: retorna una cadena de caracteres con los datos/claves.
        """ 

        return str(self.clave)

    def tiene_hijos(self):
        """Método que evalua si un arbol tiene hijos.

        Returns:
            bool: retorna un valor booleano True / False según corresponda 
            a la evaluación de la busqueda de hijos.
        """       

        return self.izq is not None or self.der is not None