#!/usr/bin/env python
from ed.secuenciales.listaCSE import ListaCSE

"""La Loteria se realiza con la participación de uno o varios concursantes, que
compran una boleta, para poder ganar un único premio.
En este módulo se implementan las clases Premio, Concursante y Loteria, para
evaluar la utilización del módulo 'ed.secuenciales.listaCSE'
Author : JEAN CARLOS HERNANDEZ BENAVIDES
"""
class Premio:
    """Esta clase representa un premio a ser entregado a un feliz ganador, el
    cual tiene como características el nombre y valor
    """
    def __init__(self, nombre, valor):
        """Consructor de la clase Premio
        Parameters
        ----------
        nombre : str
        El nombre del premio
        valor : float
        El valor del premio
        """

        self.nombre = nombre
        self.valor = valor
        

    def __eq__(self, otro_premio):
        """Método de comparación por igualdad con otro objeto de tipo Premio,
        según el nombre y el valor
        Parameters
        ----------
        otro_premio : Premio
        El premio con el cual se realiza la comparación de igualdad
        Returns
        -------

        bool
        True, si los dos premios son iguales. False, en caso contrario
        """
        return self.nombre == otro_premio.nombre and self.valor == otro_premio.valor    


    def __repr__(self):
        """Método que retorna una cadena de presentación del premio
        Returns
        -------
        str
        Una cadena con la presentación del premio, en el formato:
        '[nombre : $ valor_con_separador_de_miles_y_una_cifra_decimal]'
        El valor del premio se tiene que mostrar con separador de miles de
        su localidad (.), en este caso de Colombia, y una cifra decimal
        separadas por coma (,)
        Ejm: '[TV LG 45 pulgadas : $ 1.250.000,0]'
        """    
        string = ""
        val = '{:,.1f}'.format(self.valor).replace(",", "@").replace(".", ",").replace("@", ".")   
        string += "[" + str(self.nombre) + ": $ " + val + "]"
       
        return string


class Concursante:
    """Esta clase representa al Concursante que participa en un sorteo, y si
    tiene buena suerte, ganará un premio. El concursante solamente se
    identificará a través de su nombre
    """
    def __init__(self, nombre):
        """Consructor de la clase Concursante
        Parameters
        ----------
        nombre : str
        El nombre del Concursante
        """
        self.nombre = nombre


    def __eq__(self, otro_concursante):
        """Método de comparación por igualdad con otro objeto de tipo
        Concursante, según el nombre
        Parameters
        ----------
        otro_concursante : Concursante
        El Concursante con el cual se realiza la comparación de igualdad
        Returns
        -------
        bool
        True, si los dos Concursantes son iguales. False, en caso contrario
        """
        if type(otro_concursante) == type(self):
            return self.nombre == otro_concursante.nombre
        else:
            return False

    def __repr__(self):
        """Método que retorna una cadena de presentación del Concursante
        Returns
        -------
        str
        Una cadena con la presentación del Concursante, en el formato:
        '(nombre_del_concursante)'
        Ejm: '(Juan Pérez)'
        """
        string = ""
        string = "'(" + self.nombre + ")'"
        return string



class Loteria:
    """La Loteria se puede representar como una lista de premios a ser
    sorteados entre una lista de concursantes.
    
    """
    def __init__(self, precio_boleta):
        """Construir la Loteria, con nuevos premios y nuevos concursantes. Es
        necesario conocer el precio de la boleta que tendrá que pagar cada
        concursante
        Parameters
        ----------
        precio_boleta : float
        El precio de la boleta que paga cada concursante
        """
        self.precio_boleta = precio_boleta
        self.lista_premios = ListaCSE()
        self.lista_concursantes = ListaCSE()
        self.valor_total_entregado = 0
        self.total_de_concursantes_ganadores = 0


    def agregar_premio(self, nuevo_premio):
        """Método que adiciona un nuevo premio al final de la lista de premios
        Parameters
        ----------
        nuevo_premio : Premio
        El nuevo premio a ser adicionado
        Returns
        -------
        bool
        True, si el premio es realmente válido y pudo ser adicionado a la
        lista de premios. False, en caso contrario
        """
        return self.lista_premios.adicionar(nuevo_premio)
        

    def quitar_premios(self, el_premio):

        """Método que permite quitar todos los premios coincidentes con el
        premio
        Parameters
        ----------
        el_premio : Premio
        El premio que se quita de la lista de premios
        Returns
        -------
        bool
        True, si al menos se elimina un premio de la lista. False, en caso
        contrario
        """

        return self.lista_premios.borrar(el_premio)

    def agregar_concursante(self, nuevo_concursante):
        """Método que adiciona un nuevo concursante al final de la lista de
        concursantes, teniendo en cuenta que el nuevo concursante no debe estar
        registrado con anterioridad en la lista
        Parameters
        ----------
        nuevo_concursante : concursante
        El nuevo concursante a ser adicionado
        Returns
        -------
        bool
        True, si el concursante es realmente válido y pudo ser adicionado
        a la lista de concursantes. False, en caso contrario
        """
        if not self.lista_concursantes.buscar(nuevo_concursante):
            return self.lista_concursantes.adicionar(nuevo_concursante)          
        else: 
            #print("YA EXISTE EL CONCURSANTE")
            return False

    def pozo(self):
        """Método que permite cuantificar el valor total de los premios que
        ofrece la loteria
        Returns
        -------
        float
        El valor total acumulado de los premios que tiene la loteria
        """
        
        nodo_actual = self.lista_premios.nodo_cab
        total = 0.0
        for _ in range(self.lista_premios.__len__()):
            total += float(nodo_actual.dato.valor)
            nodo_actual = nodo_actual.sig
        return total

    def cuantos_premios(self, un_premio):
        """Método que determina cuántos premios existen de un determinado
        premio
        Parameters
        ----------
        un_premio : Premio
        El premio que se cuantifica, según el número de veces que se
        encuentre en la lista de premios
        Returns
        -------
        int
        El número de veces que un premio se encuentra en la lista de
        premios
        """

        return self.lista_premios.buscar_cuantos(un_premio)

            
    def sortear(self, pos_conc, pos_premio):
        """Método que permite realizar el sorteo de un premio entre el grupo de
        concursantes. Para maximizar las ganancias del sorteo, hay que tener en
        cuenta que cada sorteo es posible realizarlo cuando el valor sumado de
        todas las boletas vendidas es igual o supera en un 20% el valor total
        de premios.
        Ejm: Si el total de premios suma $101 y el total vendido por boletas
        suma $120 (cuando el costo de la boleta es $10 y el número de boletas
        vendidas o de concursantes es de 12), entonces no es posible realizar
        el sorteo. En cambio, si el total de premios suma $100 y el total de
        vendido por boletas suma $120, entonces si es posible realizar el
        sorteo.
        En el caso de que el premio sea entregado al concursante, ese premio y
        el concursante ganador deberán salir de la lista correspondiente
        Parameters
        ----------
        pos_conc : int
        Un valor entero que determina la posición del concursante en la
        lista
        pos_premio : int
        Un valor entero que determina la posición del premio en la
        lista
        Returns
        -------
        tuple
        Retorna una tupla (concursante, premio), indicando el concursante
        que gano el premio. Puede retornar (None, None) en el caso de que
        no sea posible entregar el premio al concursante
        ATENCIÓN: Nunca sera posible retornar (None, premio) o
        (concursante, None)
        """

        valor_total_premios = self.pozo()
        valor_cada_boleta = self.precio_boleta
        valor_total_boletas = (valor_cada_boleta * self.lista_concursantes.__len__())
        diferencia = valor_total_premios * 0.2

        if diferencia <= ( valor_total_boletas - valor_total_premios):
            if self.lista_concursantes.ruleta_rusa(pos_conc):
                conc_ganador = self.lista_concursantes.ruleta_rusa(pos_conc)
                self.lista_concursantes.borrar(pos_conc,True)
            else:
                conc_ganador = None
            if self.lista_premios.ruleta_rusa(pos_premio):
                premio_dado = self.lista_premios.ruleta_rusa(pos_premio)
                self.lista_premios.borrar(pos_premio,True)
            else: 
                premio_dado = None         
            if conc_ganador is not None and premio_dado is not None:
                
                self.valor_total_entregado += self.lista_premios.ruleta_rusa(pos_premio).valor
                self.total_de_concursantes_ganadores += 1
                
                return (conc_ganador,premio_dado)
            else:
                return (None, None)        
        else:
            return False

        
    def __str__(self):
        """Método que construye y retorna una cadena con información de los
        premios y los concursantes actuales
        Returns
        -------
        str
        Una cadena con la presentación del los premios y los concursantes
        en juego, de la forma:
        'Premios: {[premio : $ valor] [premio : $ valor]}
        [$ total_dinero_entregado_en_premios]
        Concursantes: {(concursante) (concursante)}
        [total_de_concursantes_ganadores]'
        Ejms:
        'Premios: {[TV LG : $ 1.000.000,0] [Blu-ray LG : $ 800.000,0]}
        [$ 0]
        Concursantes: {(Pedro) (María) (Juan)}
        [0]'
        'Premios: {}
        [$ 1800000]
        Concursantes: {(Juan)}
        [2]'
        """
        
        string = ""
        nodo_actual = self.lista_premios.nodo_cab
        string += "Premios: {"
        for _ in range(self.lista_premios.__len__()):   
            if _ ==  self.lista_premios.__len__() - 1 and self.lista_premios.__len__() != 1: 
                val = '{:,.1f}'.format(nodo_actual.dato.valor).replace(",", "@").replace(".", ",").replace("@", ".")             
                string += " [" + nodo_actual.dato.nombre + " : $ " + val + "]}"
            else:
                if nodo_actual != self.lista_premios.nodo_cab:
                    string += " "
                val = '{:,.1f}'.format(nodo_actual.dato.valor).replace(",", "@").replace(".", ",").replace("@", ".")    
                string += "[" + nodo_actual.dato.nombre + " : $ " + val + "]"
                if self.lista_premios.__len__() == 1 :
                    string += "}"
            
            nodo_actual = nodo_actual.sig
        if self.lista_premios.__len__() == 0:
            string += "}"
        string += "\n[$ " + str(self.valor_total_entregado) + "]\n"
        
        nodo_actual2 = self.lista_concursantes.nodo_cab
        string += "Concursantes: {"
        for _ in range(self.lista_concursantes.__len__()):   
            if _ ==  self.lista_concursantes.__len__() - 1 and self.lista_concursantes.__len__() != 1:           
                string += " (" + nodo_actual2.dato.nombre + ")}"
            else: 
                if nodo_actual2 != self.lista_concursantes.nodo_cab:
                    string += " "
                string += "(" + nodo_actual2.dato.nombre + ")"
                if self.lista_concursantes.__len__() == 1 :
                    string += "}"

            nodo_actual2 = nodo_actual2.sig
        if self.lista_concursantes.__len__() == 0:
            string += "}"
        string += "\n[" + str(self.total_de_concursantes_ganadores) + "]"

        return string  


'''#Creo premios
premio1 = Premio("Carro1",200)
premio2 = Premio("Carro2", 400)
premio3 = Premio("Carro3", 400)
premio4 = Premio("Carro4", 400)

#Comparo premios el __eq__ es llamado con ==
print(premio1 == premio2)

#Creo loterias
loteria1 = Loteria(30000)

#adicionar premios a loteria1
print(loteria1.agregar_premio(premio1))
print(loteria1.agregar_premio(premio2))
print(loteria1.agregar_premio(premio3))
print(loteria1.agregar_premio(premio4))

#print(loteria1.lista_premios.es_vacia())

#adicionar concursantes a loteria1
concu1 = Concursante("Jean")
concu2 = Concursante("Carlos")
concu3 = Concursante("Hernandez")
concu4 = Concursante("Benavides")
concu5 = Concursante("Villota")
concu6 = Concursante("Calpa")
concu7 = Concursante("Adriana")
print(loteria1.agregar_concursante(concu1))
print(loteria1.agregar_concursante(concu2))
print(loteria1.agregar_concursante(concu3))
print(loteria1.agregar_concursante(concu4))
#print(loteria1.agregar_concursante(concu5))
#print(loteria1.agregar_concursante(concu6))
#print(loteria1.agregar_concursante(concu7))

#en este concu5 ya existe el concursante y no lo adiciona
#print(loteria1.agregar_concursante(concu5))

print("\n###### PARTE 2 ######\n")

#pozo y sumar dinero
print(loteria1.pozo())

#contar la cantidad de un premio
print(loteria1.cuantos_premios(premio1))

print("\n###### PARTE 3 ######\n")

#sortear
#print(loteria1.sortear(2,3))
print(loteria1.sortear(2,0))
print(loteria1.sortear(2,1))
print(loteria1.sortear(0,0))

print("\n###### PARTE 4 ######\n")
#imprimir info'''
'''loteria1 = Loteria(30000)
concu1 = Concursante("Jean")
#print(loteria1.agregar_concursante(concu1))
print(loteria1.__str__())'''