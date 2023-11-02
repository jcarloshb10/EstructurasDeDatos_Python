#!/usr/bin/env python
from ed.secuenciales.listaSE import ListaSE


"""Un conjunto es una secuencia de elementos, todos ellos del mismo tipo sin
duplicidades. En este módulo se implementa la clase Conjunto, para evaluar la
utilización de la librería 'ed.secuenciales.listaSE'

Author : JEAN CARLOS HERNANDEZ BENAVIDES
"""

class Conjunto:
    """Esta clase representa e identifica a un conjunto de cualquier tipo de
    dato, cuya implementación se realiza a través de una Lista Simplemente
    Enlazada
    """    

    def __init__(self, nombre):
        """Constructor de la clase Conjunto
        Parameters
        ----------
        nombre : str
        El nombre que identifica al conjunto
        """
        
        self.lista_enlazada = ListaSE()
        #Todo nombre de conjunto va en mayuscula
        self.nombre = nombre
        self.nombre = self.nombre.upper()
        #print(self.nombre)
        
    def agregar(self, *args):
        """Método que permite agregar cualquier cantidad de elementos del mismo
        tipo al conjunto, validando además que no se encuentren repetidos.
        Ejm: Para adicionar los números enteros 4, 78, 5 y 10
        al conjunto A sería de la forma:
        conjuntoA.agregar(4, 78, 5, 10)
        Es posible adicionar al mismo conjunto el valor 7 y 10 de la forma:
        conjuntoA.agregar(7, 10)
        En el caso de imprimir el conjunto A el resultado sería:
        'A = {4, 78, 5, 10, 7}'
        Parameters
        ----------
        parámetro_consulta : ?????
        ????? ????????? ??????? ?????? ????????? ????????? ??????????? ????
        """
        for value in args:
            if self.pertenencia(value) == False:             
                self.lista_enlazada.adicionar(value)
                return True
            #print(self.lista_enlazada.recorrer())
           
    
    def cardinal(self):
        """Método que representa al número de elementos que tiene un conjunto.
        Cardinal (D)= n (D)= número de elementos.
        Ejm: El número Cardinal del conjunto D = {8, 15, -85, 26, 19} es = 5
        Returns
        -------
        int
        Número de elementos del conjunto
        """
        #print(self.lista_enlazada.recorrer())
        return self.lista_enlazada.__len__()

    def pertenencia(self, un_elto):
        """Se dice que todo elemento de un conjunto pertenece a dicho conjunto
        si forma parte del conjunto en mención y para indicar esto lo
        representamos de la siguiente manera ∈ y en contrario de no
        pertenencia ∉
        Ejm: Si tenemos A = {7, 25, 32, 10}
        Se dice que 32 ∈ A: Se lee '32 pertenece al conjunto A'
        y también se dice que 14 ∉ A: Se lee '14 no pertenece al conjunto A'
        Parameters
        ----------
        un_elto : object
        Un valor, del mismo tipo de los elementos del conjunto, que se
        analiza si pertenece o no al conjunto
        Returns
        -------
        bool
        True, si 'un_elto' pertenece al conjunto. False, en caso contrario
        """
        existe_elto = False

        for conj in self.lista_enlazada:
            if conj.dato == un_elto: #Buscando un_elto en los conjuntos
                existe_elto = True
        return existe_elto

    def es_subconjunto(self, otro_cjto):
        """En general si A y B son dos conjuntos cualesquiera, decimos que B es
        un subconjunto de A si todo elemento de B lo es de A también.
        Sean los conjuntos A = {0, 1, 2, 3, 5, 8} y B = {1, 2, 5}
        Decimos que B esta contenido en A, o que B es un subconjunto de A
        Parameters
        ----------
        otro_cjto : Conjunto
        El conjunto con el cual se compara y se determina si todos los
        elementos del conjunto estan en ese conjunto
        Returns
        -------
        bool
        True, si todos los elementos de conjunto forman parte de
        'otro_conjunto'. False, en caso contrario
        """
        nuevo_conjunto = Conjunto("nuevo_x")
        #print(self.cardinal())
        #print(self.lista_enlazada.__len__())
        #print(otro_cjto.lista_enlazada.__len__()

        for i in self.lista_enlazada: 
            for j in otro_cjto.lista_enlazada:
                if i.dato == j.dato:
                    nuevo_conjunto.lista_enlazada.adicionar(i.dato)
         
        if nuevo_conjunto.lista_enlazada.__len__() == self.lista_enlazada.__len__():      
            print(nuevo_conjunto)
            #print("es subconjunto o True")
            return True
        else:
            print(nuevo_conjunto)
            #print("No es subconjunto o FALSE")
            return False
        
    
    def union(self, otro_cjto):
        """La unión de conjuntos A y B es el conjunto formado por los elementos
        que pertenecen a A, a B o a ambos
        Sean los conjuntos A = {10, 14, 32} y B = {1, 2, 5}
        A ∪ B = {10, 14, 32, 1, 2, 5}
        Parameters
        ----------
        otro_cjto : Conjunto
        El conjunto con el cual se realiza la unión
        Returns
        -------
        Conjunto
        Un nuevo conjunto que tendrá como nombre:
        'nombre_conjunto U nombre_otro_conjunto'
        y que contendrá los elementos producto de la unión entre ambos
        """
        nombre = self.nombre + " U " + otro_cjto.nombre
        nuevo_conjunto = Conjunto(nombre)
        #print(otro_cjto)
        for i in self.lista_enlazada:
            nuevo_conjunto.lista_enlazada.adicionar(i.dato)
        for j in otro_cjto.lista_enlazada:
            if self.pertenencia(j.dato) is False:
                nuevo_conjunto.lista_enlazada.adicionar(j.dato)
        nuevo_conjunto.cardinal()
        return nuevo_conjunto

    def intersection(self, otro_cjto):
        """Dados lo conjuntos A y B, se llama intersección al conjunto formado
        por los elementos que pertenecen a A y B a la vez; es decir, es el
        conjunto formado por los elementos comunes a A y B.
        Sean los conjuntos A = {5, 12, 28, 6} y B = {6, 50, 12, 77}
        A ∩ B = {12, 6}
        Parameters
        ----------
        otro_cjto : Conjunto
        El conjunto con el cual se realiza la intersección
        Returns
        -------
        Conjunto
        Un nuevo conjunto que tendrá como nombre:
        'nombre_conjunto I nombre_otro_conjunto'
        y que contendrá los elementos producto de la intersección entre
        ambos
        """
        nombre = self.nombre + " y " + otro_cjto.nombre
        nuevo_conjunto = Conjunto(nombre)
        #print(nombre)
        #print(otro_cjto)
        for i in self.lista_enlazada:
            for j in otro_cjto.lista_enlazada:

                if i.dato == j.dato:
                    nuevo_conjunto.lista_enlazada.adicionar(i.dato)
        #print(nuevo_conjunto)
        nuevo_conjunto.cardinal()
        return nuevo_conjunto


    def diferencia(self, otro_cjto):
        """Sean A y B dos conjuntos. La diferencia de A y B se denota por A-B y
        es el conjunto de los elementos de A que no están en B
        Sea A = {5, 10, 15, 20} y B = {25, 5, 15, -21, 30, 17}
        A - B = {10, 20}
        Parameters
        ----------
        otro_cjto : Conjunto
        El conjunto con el cual se realiza la diferencia
        Returns
        -------
        Conjunto
        Un nuevo conjunto que tendrá como nombre:
        'nombre_conjunto - nombre_otro_conjunto'
        y que contendrá los elementos producto de la diferencia entre
        ambos
        """
        
        nombre_conjunto = self.nombre + " - " + otro_cjto.nombre
        nuevo_conjunto = Conjunto(nombre_conjunto)
        for k in self.lista_enlazada:
            if otro_cjto.pertenencia(k.dato) == False:
                nuevo_conjunto.agregar(k.dato)
                
        if nuevo_conjunto.lista_enlazada.es_vacia() == True:
            return print("Conjunto vacío")    
        #print(nuevo_conjunto)
        return nuevo_conjunto
               



    def __str__(self):
        """Devuelve una cadena con la presentación del conjunto
        Returns
        -------
        str
        Una cadena con la presentación del conjunto, en el formato:
        'NOMBRE_DEL_CONJUNTO_EN_MAYUS = {elemento1, elemento2, elementoN}'
        Ejms: 'A = {45, 78, 30}', 'C U D = {10, 8, 7, 12, 100}',
        'B I C = {4, 0, 8}', 'D - A = {34, 6}'
        """
        devolver_lista = ""
        
        for k in self.lista_enlazada:
            if  self.lista_enlazada.nodo_cab == k and self.lista_enlazada.__len__() == 1:
                devolver_lista += "{" + str(k.dato) + "}"

            elif self.lista_enlazada.nodo_cab == k:
                devolver_lista += "{" + str(k.dato) + ", "      

            elif k.sig == None:
                devolver_lista += str(k.dato) + "}"

            else: 
                devolver_lista += str(k.dato) + ","

        cadena = self.nombre + " = " + devolver_lista
        return cadena