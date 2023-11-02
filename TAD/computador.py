from ed.jerarquicas.arbolBinarioBusqueda import ArbolBinarioBusqueda
from ed.jerarquicas.arbolBinario import ArbolBinario
from ed.jerarquicas.recorridos import *

class Computador:
    """Creamos la clase Computador para crear un objeto de este tipo y poder usar los diferentes
    atributos de este en diferentes operaciones o metodos.

    Autores: JEAN CARLOS HERNANDEZ BENAVIDES | MILER ANDRES ESPAÑA
    """ 

    #Valores por defecto y constructor de Computador
    def __init__(self, marca, velocidad_procesador, precio_compra):
        """__init__ es el constructor de la clase Computador.

        Args:
            marca (string): guarda el nombre de la marca del computador.
            velocidad_procesador (float): parametro que guarda la velocidad del procesador del computador.
            precio_compra ([type]): parametro del precio en el aque se adquiere una computadora.
        """
        
        self.marca = marca
        self.velocidad_procesador = velocidad_procesador
        self.precio_compra = precio_compra

    #Metodo para comparar dos computadores
    def __eq__(self, otro_computador):
        """Este metodo nos permite hacer la comparacion entre dos objetos de tipo Computador
                para determinar si son iguales.

        Args:
            otro_computador (Computador): es un computador con el cuál vamos a realizar la comparacion.

        Returns:
            bool: retorna True si son iguales y False si son diferentes los computadores.
        """ 

        if otro_computador.marca == self.marca:
            if otro_computador.velocidad_procesador == self.velocidad_procesador:
                return True
        return False
    
    #metodos magicos > .. etc
    def __gt__(self, otro_computador):
        if self.marca >= otro_computador.marca:
            if self.velocidad_procesador > otro_computador.velocidad_procesador: return True
        return False
    
    def __lt__(self, otro_computador):
        if self.marca <= otro_computador.marca:
            if self.velocidad_procesador < otro_computador.velocidad_procesador: return True
        return False
    
    def __ge__(self, otro_computador):
        if self.marca >= otro_computador.marca:
            if self.velocidad_procesador >= otro_computador.velocidad_procesador: return True
        return False

    def __le__(self, otro_computador):
        if self.marca <= otro_computador.marca:
            if self.velocidad_procesador <= otro_computador.velocidad_procesador: return True
        return False


    #Presentacion del Computador en vez de str
    def __repr__(self):
        """Método que retorna una cadena de presentación del computador
        Returns
        -------
        str
        Una cadena como:
        Ejm: '[SAMSUNG : 1.5 Ghz $ 1.250.000,0]'
        """

        string = ""
        val = '{:,.1f}'.format(self.precio_compra).replace(",", "@").replace(".", ",").replace("@", ".")   
        string += "[" + str(self.marca) + ": " + str(self.velocidad_procesador) +" Ghz" +": $ " + val + "]"
        
        return string

class Almacen:

    #Constructor inicializador del  Almacén
    def __init__(self):
        #self.nombre = nombre
        self.ganancias_netas = 0
        self.stock = ArbolBinarioBusqueda()

    #Comprar un nuevo computador
    def comprar_computador(self, un_computador):
        b = self.stock.buscar(un_computador)
        if not b:
            self.stock.adicionar(un_computador)
            return True
        else: return False


    def vender_computador(self, un_computador):
        f = self.stock.borrar(un_computador)
        
        if f:
            self.ganancias_netas += un_computador.precio_compra * 0.15         
            
            #print("Se borró del stock el computador")
            return True
        else:
            #print("No se borró del stock el computador")
            return False

    def mayor_computador(self):
        return self.stock.buscar_maximo()

    def menor_computador(self):
        return self.stock.buscar_minimo()

    def inorden(self):
        return cad_inorden(self.stock)

    def reporte(self):
        string = ""
        string += str("Computador mayor: ")
        string += str(self.stock.buscar_maximo())
        string += "\n"
        string += str("Computador menor: ")
        string += str(self.stock.buscar_minimo()) 
        string += "\n"
        string += str("Cantidad de PC´s: ")
        string += str(self.stock.__len__()) 
        string += "\n"
        string += str("Ganancias Netas: ")
        string += str(self.ganancias_netas)

        

"""#Test
if __name__ == "__main__":
    pc = Computador("HP", 3.65, 3600000)
    print(pc)
    Alma = Almacen()
    Alma.comprar_computador(pc)
    pc = Computador("HP", 4.8, 3800000)
    Alma.comprar_computador(pc)
    pc = Computador("HP", 4.8, 3800000)
    Alma.comprar_computador(pc)
    pc = Computador("DELL", 4.8, 3800000)
    Alma.comprar_computador(pc)
    pc = Computador("JANUS", 4.8, 2000000)
    Alma.comprar_computador(pc)
    pc = Computador("COMPAQ", 2.8, 3800000)
    Alma.comprar_computador(pc)
    pc = Computador("HP", 3.8, 4800000)
    Alma.comprar_computador(pc)
    pc = Computador("MAC", 4.8, 6800000)
    Alma.comprar_computador(pc)
    pc = Computador("MAC", 4.8, 6800000)
    #Alma.vender_computador(pc)
    #Alma.reporte()
    pc = Computador("COMPAQ", 2.8, 3800000)
    Alma.vender_computador(pc)
    
    print(Alma.ganancias_netas)
    print(Alma.mayor_computador())
    Alma.menor_computador()"""



    












        
