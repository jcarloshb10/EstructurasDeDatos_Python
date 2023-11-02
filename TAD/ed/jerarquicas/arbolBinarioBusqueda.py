from ed.jerarquicas.nodo import NodoArbolBinario
from ed.jerarquicas.arbolBinario import ArbolBinario
#from ed.jerarquicas.excepcion(no_se_necesita_aun) import DuplicateKeyException
from random import random

class ArbolBinarioBusqueda():
    """Creamos la clase ArbolBinarioBusqueda con la cuál podremos crear y manejar los diferentes 
    métodos de esta clase aplicandolos a las acciones que se pueden realizar con un arbol binario.
    
    Autores: JEAN CARLOS HERNANDEZ | MILER ANDRÉS ESPAÑA
    """

    def __init__(self):
        """__init__ es el Constructor de un objeto de tipo ArbolBinarioBusqueda.
        Éste creará inmediatamente un arbol con una raiz sin valor inicial (None)
        """        
        self.raiz = None

    def adicionar(self, nueva_clave):
        """El método adicioinar() recibe una nueva_clave el cuál será añadida al arbol
        ya creado sin valores iniciales o incluso cuando ya tenga más nodos.

        Args:
            nueva_clave (objeto/valor): es el dato que se recibe para ser almacenado en el arbol.
        """        
        print("a bin",nueva_clave)
        self.raiz = self.__adicionar(self.raiz, nueva_clave)

    def __adicionar(self, sub_arbol, nueva_clave):
        """El método __adicionar() es un método de recursividad para apoyar a adicionar() en el 
        momento de agregar una nueva_clave al nodo de un arbol. 

        Args:
            sub_arbol (arbol_bin): es el parametro que contiene el sub_arbol de un arbol u otro sub_arbol.
            nueva_clave (objeto/valor): es el dato que se recibe para ser almacenado en el arbol y se trae desde adicionar()

        Raises:
            DuplicateKeyException: es una excepcion para que no se repitan las claves
            ya que no permiten dos claves iguales al ser de busqueda.

        Returns:
            ArbolBinarioBusqueda: se retorna siempre un arbol/sub_arbol.
        """    

        if sub_arbol is None:
            #print("ENTRA AL VACIO")
            sub_arbol = NodoArbolBinario(nueva_clave)
        elif sub_arbol.clave > nueva_clave:
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        elif sub_arbol.clave < nueva_clave:
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)
        elif sub_arbol.clave == nueva_clave:
            #raise DuplicateKeyException(nueva_clave)
            raise "Ya existe"
        return sub_arbol

    def buscar(self, clave_buscar):
        """El método buscar() nos permite poder encontrar un dato o una clave dentro del arbol.

        Args:
            clave_buscar (objeto/valor): este dato contenido en un nodo nos permite 
            saber que clave necesitamos encontrar.

        Returns:
            sub_arbol: nos lleva a a la recursividad hasta que encuentre la clave o termine de recorrerlo.
        """        

        return self.__buscar(self.raiz, clave_buscar)

    def __buscar(self, sub_arbol, clave_buscar):
        """El método __buscar() es un método de recursividad para apoyar a buscar() en el 
        momento de buscar una clave_buscar en los nodos de un arbol.

        Args:
            sub_arbol (ArbolBinarioBusqueda): es el parametro que contiene el sub_arbol de un arbol u otro sub_arbol.
            clave_buscar (objeto/valor): este dato contenido en un nodo nos permite 
            saber que clave necesitamos encontrar, la traemos del método buscar()

        Returns:
            bool: Retorna True si encuentra la clave en el arbol o None si no lo hace.
        """        

        if sub_arbol is not None:
            if sub_arbol.clave == clave_buscar:
                return sub_arbol.clave
            elif clave_buscar < sub_arbol.clave:
                return self.__buscar(sub_arbol.izq, clave_buscar)
            elif clave_buscar > sub_arbol.clave:
                return self.__buscar(sub_arbol.der, clave_buscar)
        return None
    
    def buscar_minimo(self):
        """El método buscar_minimo() nos permite poder encontrar el valor minimo de una calave dentro
        del arbol binario.

        Args:
            arbol_minimo (ArbolBinarioBusqueda): este parametro contiene el arbol al que analizaremos.

        Returns:
            sub_arbol, nos lleva a a la recursividad hasta que encuentre la menor clave.
        """    

        return self.__buscar_minimo(self.raiz)
        

    def __buscar_minimo(self, sub_arbol):
        """El método __buscar_minimo() es un método de recursividad para apoyar a buscar_minimo() en el 
        momento de buscar la menor clave de los nodos de un arbol.

        Args:
            sub_arbol (ArbolBinarioBusqueda): es el parametro que contiene el sub_arbol de un arbol u otro sub_arbol.

        Returns:
            clave (objeto/valor): retorna la clave minima dentro del arbol.
        """   
        if sub_arbol is None:
            return None
        elif sub_arbol.izq is not None:
            return self.__buscar_minimo(sub_arbol.izq)
        return sub_arbol.clave
    
    def buscar_maximo(self):
        """El método buscar_maximo() nos permite poder encontrar el valor maximo de una clave dentro
        del arbol binario.

        Args:
            arbol_maximo (ArbolBinarioBusqueda): este parametro contiene el arbol al que analizaremos.

        Returns:
            sub_arbol, nos lleva a a la recursividad hasta que encuentre la mayor clave.
        """ 

        return self.__buscar_maximo(self.raiz)
    
    def __buscar_maximo(self, sub_arbol):
        """El método __buscar_maximo() es un método de recursividad para apoyar a buscar_maximo() en el 
        momento de buscar la mayor clave de los nodos de un arbol.

        Args:
            sub_arbol (ArbolBinarioBusqueda): es el parametro que contiene el sub_arbol de un arbol u otro sub_arbol.

        Returns:
            clave (objeto/valor): retorna la clave maxima dentro del arbol.
        """
        if sub_arbol is None:
            return None
        elif sub_arbol.der is not None:
            return self.__buscar_maximo(sub_arbol.der)
        return sub_arbol.clave

    def borrar(self, clave_borrar):
        """El método borrar nos permite encontrar una clave dentro de un arbol y quitarla del nodo.

        Args:
            clave_borrar (objeto/valor): es el parámetro que contiene en valor a eliminar.

        Returns:
            sub_arbol, nos lleva a a la recursividad hasta que encuentre y elimine la clave.
        """   

        return self.__borrar(self.raiz, clave_borrar)
        #usar la tecnica: El borrado sea para un Nodo con hijos, que sea reemplazado
        # por el menor de los mayores
        
    def __borrar(self, sub_arbol, clave_borrar):
        """El método __borrar() es un método de recursividad para apoyar a borrar() en el 
        momento de buscar la mayor clave de los nodos de un arbol.

        Args:
            sub_arbol (ArbolBinarioBusqueda): es el parametro que contiene el sub_arbol de un arbol u otro sub_arbol.
            clave_borrar ([type]): es el parámetro que contiene en valor a eliminar, la traemos de borrar().

        Returns:
            ArbolBinarioBusqueda: se retorna siempre un arbol/sub_arbol.
        """   

        if sub_arbol is not None:
            if clave_borrar < sub_arbol.clave:
                sub_arbol.izq = self.__borrar(sub_arbol.izq, clave_borrar)
            elif clave_borrar > sub_arbol.clave:
                sub_arbol.der = self.__borrar(sub_arbol.der, clave_borrar)
            else:
                if sub_arbol.izq is None and sub_arbol.der is None:
                    sub_arbol = None
                elif sub_arbol.izq is None:
                    if self.raiz.clave == clave_borrar:
                        self.raiz = self.raiz.der
                    else:
                        sub_arbol = sub_arbol.der
                elif sub_arbol.der is None:
                    if self.raiz.clave == clave_borrar:
                        self.raiz = self.raiz.izq
                    else:
                        sub_arbol = sub_arbol.izq
                else:
                    clave_aux = self.buscar_maximo(sub_arbol.izq)
                    clave_actual = sub_arbol.clave
                    sub_arbol.clave = clave_aux
                    if clave_aux < clave_actual:
                        sub_arbol.izq = self.__borrar(sub_arbol.izq, clave_aux)
                    elif clave_aux > clave_actual:
                        sub_arbol.der = self.__borrar(sub_arbol.der, clave_aux)
        return sub_arbol

    def __len__(self):
        return self.__numero_nodos(self.raiz)

    def __numero_nodos(self, sub_arbol):
        if sub_arbol is not None:
            return (1 + self.__numero_nodos(sub_arbol.izq) + self.__numero_nodos(sub_arbol.der))
        else:
            return 0
