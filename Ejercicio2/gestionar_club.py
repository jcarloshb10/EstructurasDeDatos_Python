#!/usr/bin/env python3
"""
    PROJECT: Taller Estructuras de Información

    MODULE: gestionar_club.py

    DESCRIPTION:
    Construir un programa, que utilizando una ListaSimplementeEnlazada, permita
    almacenar y manipular información relacionada a socios de un club
    deportivo.

    DATE: 24.04.2019 09:00:01 COT

    AUTHORS: Student 1 and Student 2
"""

from tad.listas.lse import ListaSimplementeEnlazada
from datetime import date


class SocioClub:

    """
    Cada socio se caracteriza porque tiene un número de socio, su nombre,
    domicilio y año de ingreso. Tanto el nombre, el domicilio y el año de
    ingreso pueden tener valores por defecto en su inicialización.
    """

    def __init__(self, numSocio, nombre=None, domicilio=None, añoIngreso=None):
        self.numSocio = numSocio
        self.nombre = nombre
        self.domicilio = domicilio
        self.añoIngreso = añoIngreso
    # Escriba AQUI el constructor de la clase, los parámetros que recibe y la
    # inicialización de los atributos correspondientes.
    # Método SC # 1

    def __eq__(self, other):
        """
        Método de comparación de un socio, teniendo en cuenta su número de
        socio.

        :other: El otro socio con el cual se van a ser las comparaciones
        :returns: True si los socios son iguales. False en caso contrario.
        :rtype: bool
        """

        return type(self) == type(other) and self.numSocio == other.numSocio

    # Método SC # 2
    def __str__(self):
        """
        Método de presentación del socio del club.

        :returns: Una cadena con el formato:
            "<numero socio--nombre socio--domicilio--año de ingreso>"
        :rtype: str
        """
        return "<"+str(self.numSocio)+"--"+str(self.nombre)+"--"+str(self.domicilio)+"--"+str(self.añoIngreso)+">"


class ClubDeportivo:

    """
    El club deportivo se caracteriza por tener un nombre, un teléfono y el
    registro de los diferentes socios pertenecientes al club.
    """

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.registro = ListaSimplementeEnlazada()

    def registrar_nuevo_socio(self, nuevo_socio):
        """
        Hay que considerar que no puede haber 2 socios con el mismo número de
        socio.

        :nuevo_socio: El nuevo socio a ser ingresado al club.
        :returns: True si el nuevo socio es admitido. False en caso contrario.
        :rtype: bool
        """
        encontrado = self.registro.localizar(nuevo_socio)

        if encontrado is None:
            return self.registro.añadir(nuevo_socio)
        else:
            return False

    # Método CD # 2

    def registrar_nuevo_socio_despues_de(self, nuevo_socio, num_socio):
        """
        Este método intenta ingresar un nuevo socio al club, en la posición
        que está después de un determinado socio, identificado con un número
        cualquiera. Tambien hay que considerar que no puede haber 2 socios con
        el mismo número de socio.

        :nuevo socio: El nuevo socio a ser ingresado al club.
        :num_socio: Es el número de socio que supuestamente ya hace parte del
        club.
        :returns: True si el nuevo socio se pudo agregar al club en una
        posición posterior a un socio existente. False en caso contrario.
        :rtype: bool
        """
        encontrado = self.registro.localizar(nuevo_socio)
        if encontrado is not None:
            return False

        aux = SocioClub(num_socio)
        indice = 0
        for i in self.registro:
            if aux == i:
                break
            indice += 1
        if indice == self.__len__():
            return False
        else:
            return self.registro.añadir(nuevo_socio, False, indice)

    # Método CD # 3
    def modificar_domicilio_socio(self, num_socio, nuevo_domicilio):
        """
        Método que realiza el cambio de domicilio de un socio registrado en el
        club.

        :num_socio: El número de socio al cual se le va a realizar la
        modificación del domicilio.
        :nuevo_domicilio: El nuevo domicilio del socio.
        :returns: El socio del club, con la modificación de domicilio realizada
        OK. None en caso de que el socio no exista según el número de socio
        ingresado.
        :rtype: Un objeto de tipo SocioClub o None
        """

        aux = SocioClub(num_socio)
        indice = 0
        for i in self.registro:
            if aux == i:
                i.domicilio = nuevo_domicilio
                return i

    # Método CD # 4

    def reporte_antigüedad(self, años_antg):
        """
        Genera un listado de todos los socios que tengan una antigüedad mayor o
        igual a un número de años determinado.

        :años_antg: Un valor numérico que representa la cantidad de años de
        antigüedad.
        :returns: Una lista con los socios que cumplen con una angüedad mayor o
        igual a la especificada o en su defecto una lista vacía.
        :rtype: Una lista de tipo ListaSimplementeEnlazada

        Nota: La clase date permite manipular fechas. Para utilizarla es
              necesario importarla de la siguiente manera:
              from datetime import date
              De esta forma podemos acceder a muchos método definidos en esta
              clase de utilidad. Con ayuda de la terminal de linux ejecuten
              python en modo interactivo, importen la clase y ejecuten:
              date.[TAB][TAB]
              para acceder a todos los método de la clase. Para consultar
              cualquier método solo basta llamar a la función help() y pasarle
              como parámetro la clase y el método que deseamos consulta, por
              ejemplo:
              help(date.weekday)
              para salir del modo ayuda presionamos la tecla 'q'.
        """
        antiguos = ListaSimplementeEnlazada()
        for i in self.registro:
            antiguedad = date.today().year-i.añoIngreso
            if antiguedad >= años_antg:
                antiguos.añadir(i)
        return antiguos
    # Método CD # 5

    def eliminar_socio(self, num_socio):
        """
        Método que permite dar de baja a un socio dado un número de
        identificación de socio.

        :num_socio: Corresponde al número de identificación del socio a ser
        eliminado.
        :returns: True si el socio es expulsado del club de socios. False en
        caso contrario.
        :rtype: bool
        """
        aux = SocioClub(num_socio)
        return self.registro.suprimir(SocioClub(num_socio))

    # Método CD # 6

    def __len__(self):
        """
        Método que ...

        :returns: ... retorna el número de socios actualmente registrados en el
        club.
        :rtype: int
        """
        return len(self.registro)

    # Método CD # 7
    def __str__(self):
        """
        Método que ...

        :returns: ... retorna una cadena de presentación del Club Deportivo,
        utilizando el siguiente formato:
            "[Club Deportivo:nombre_club_deportivo
             Teléfono:teléfono_c_d
             Total Socios:numero_socios_c_d
             <Socio_1> <Socio_2> <Socio_3> ... <Socio_n>]"
        :rtype: str
        """
        reporte = "[Club Deportivo:"+str(self.nombre)+"\nTeléfono:"+str(self.telefono) + \
            "\nTotal Socios:"+str(self.__len__())+"\n"+str(self.registro)+"]"
        return reporte
