#!/usr/bin/env python
from ed.secuenciales.pila import Pila

class Postfija:
    """ Creamos la clase Postfija con la cual se puede crear un 
    objeto con una expresión infija escrita de cualquier manera
    valida para convertir, calcular y también usar sus diferentes métodos.

	Autores: MILER ANDRÉS ESPAÑA | JEAN CARLOS HERNANDEZ BENAVIDES
    """    

    def __init__(self, expresión_infija):
        """__init__ se refiere al Constructor de un objeto de la clase Postfija.
        --------------------------
        expresión_infija es la expresion matematica infija a evaluar.
        prioridad es la prioridad de evakuacin de los signos en una expresión.

        Args:
            eval ([expresión_infija]): Se usa  para evaluar cadenas de texto 
            que pueden contener expresiones infijas.

        :raises ValueError: Indica que se ha ingresado una expresion infija invalida.
        """        
        try:
            eval(expresión_infija.replace("^", "**"),
                 {"__builtins__": None}, {})
        except:           
            raise ValueError("La expresión no es valida.") 
            
        self.expresión_infija = expresión_infija.replace(" ", "")
        self.prioridad = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.pila = Pila()


    def __mayor_prioridad(self, i):
        """Este metodo nos permite ordenar en el atributo de prioridades
        los operadores para su correcto calculo matematico.

        Args:
            i (int): variable que es el elemento de una expresion infija.

        Returns:
            bool: Retorna True si ordena por prioridad los operadores.
        """        

        try:
            a = self.prioridad[i]
            b = self.prioridad[self.pila.cima()]
            return True if a <= b else False
        except KeyError:
            return False

    def __lista_infija(self):
        """Este método nos permite crear una expresion infija listada para poder 
        proximamente convertirla y calcularla.
        
        Returns:
            list: la variable lis_infija es retornada al método de infija()
            la variable contiene la expresion aritmética lista para convertir.
        """  

        lis_infija = []
        aux_ch = ""
        exp_temporal = self.expresión_infija
        operador = ['+', '-', '*', '/', '^', '(', ')']
        while len(exp_temporal) > 0:
            if exp_temporal[0] in operador:
                lis_infija.append(exp_temporal[0])
                exp_temporal = exp_temporal[1:]
            else:
                aux_ch += exp_temporal[0]
                exp_temporal = exp_temporal[1:]
                if (len(exp_temporal) > 0 and exp_temporal[0] in operador) or len(exp_temporal) == 0:
                    lis_infija.append(aux_ch)
                    aux_ch = ""
        return lis_infija

    def infija(self):
        """Este método nos permite acceder al submetodo que retorna de manera de lista
        la cadena o expresion infija. Además en este método se interpone entre
        cada elemento de la lista un espacio.


        Returns:
            str: Se retorna la cadena obtenida en el submetodo de __lista_infija()
            separando cada caracter con un espacio.
        """     

        return " ".join(self.__lista_infija())

    def __lista_postfija(self):
        """Este método nos permite crear una expresion postfija listada para poder 
        calcularla segun la prioridad de los operandos. Este metodo ordena de manera
        polaca inversa la expresion infija.
        -----------------------------------
        pila es una variable global que se usa en varios metodos y permite guardar
        los elementos de la expresion en un respectivo orden.
        
        Returns:
            list: la variable lis_postfija es retornada al método de postfija()
            la variable contiene la expresion arítmética lista para calcular.
        """ 

        self.pila = Pila()
        lis_postfija = []
        for i in self.__lista_infija():
            ctrl = bool
            try:
                float(i)
                ctrl = True
            except:
                ctrl = False
            if ctrl is True:
                lis_postfija.append(i)

            elif i == '(':
                self.pila.apilar(i)

            elif i == ')':
                while((not self.pila.es_vacia()) and self.pila.cima() != '('):
                    a = self.pila.desapilar()
                    lis_postfija.append(a)
                if (not self.pila.es_vacia() and self.pila.cima() != '('):
                    return -1
                else:
                    self.pila.desapilar()

            else:
                while(not self.pila.es_vacia() and self.__mayor_prioridad(i)):   
                    lis_postfija.append(self.pila.desapilar())       
                self.pila.apilar(i)

        while not self.pila.es_vacia():
            lis_postfija.append(self.pila.desapilar())

        return lis_postfija
        
    def postfija(self):
        """Este método nos permite acceder al submetodo que retorna de manera de lista
        la expresion postfija. Además en este método se interpone entre
        cada elemento de la lista un espacio.


        Returns:
            str: Se retorna la cadena obtenida en el submetodo de __lista_postfija()
            separando cada caracter con un espacio.
        """     

        return " ".join(self.__lista_postfija())

    def eval_expr_aritm(self):
        """Este método nos permite calcular la expresion matematica
        con el uso de la lista ordenada de manera polaca inversa, aquí 
        se operan las operaciones segun la prioridad y entre los numeros
        relacionan dicha operacion.

        Returns:
            float: retorno de un valor flotante que finalmente es la respuesta
            de la expresion completa.
        """     
           
        self.pila = Pila()
        exp = self.__lista_postfija()
        for i in exp:
            ctrl = bool
            try:
                float(i)
                ctrl = True
            except:
                ctrl = False
            if ctrl is True:
                self.pila.apilar(i)
            else:
                val1 = self.pila.desapilar()
                val2 = self.pila.desapilar()
                operador = i if i != '^' else '**'
                self.pila.apilar(str(eval(val2 + operador + val1)))

        return float(self.pila.desapilar())
