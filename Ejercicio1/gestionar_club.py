#!/usr/bin/env python3

from tad.listas.lse import ListaSimplementeEnlazada as Lista
from datetime import date

"""
    PROJECT: Taller Estructuras de Información

    MODULE: gestionar_club.py

    DESCRIPTION:
    Construir un programa, que utilizando una ListaSimplementeEnlazada, permita
    almacenar y manipular información relacionada a socios de un club
    deportivo.

    DATE: 24.04.2019 09:00:02 COT

    AUTHORS: Maria Jose Guerrero, Jose Alejandro Castrillon
"""


class SocioClub:

    """
    Cada socio se caracteriza porque tiene un número de socio, su nombre,
    domicilio y año de ingreso. Tanto el nombre, el domicilio y el año de
    ingreso pueden tener valores por defecto en su inicialización.
    """

    # Escriba AQUI el constructor de la clase, los parámetros que recibe y la
    # inicialización de los atributos correspondientes.
    def __init__(self, numero_socio, nombre='', direccion='', año_ingreso=0):
        self.numero_socio = numero_socio
        self.nombre = nombre
        self.direccion = direccion
        self.año_ingreso = año_ingreso

    # Método SC # 1
    def __eq__(self, other) -> bool:
        """
        Método de comparación de un socio, teniendo en cuenta su número de
        socio.

        :other: El otro socio con el cual se van a ser las comparaciones
        :returns: True si los socios son iguales. False en caso contrario.
        :rtype: bool
        """
        return (
            isinstance(other, SocioClub)
            and self.numero_socio == other.numero_socio
        )

    # Método SC # 2
    def __str__(self) -> str:
        """
        Método de presentación del socio del club.

        :returns: Una cadena con el formato:
            "<numero socio--nombre socio--domicilio--año de ingreso>"
        :rtype: str
        """
        return (
            '<'
            + str(self.numero_socio)
            + '--'
            + str(self.nombre)
            + '--'
            + str(self.direccion)
            + '--'
            + str(self.año_ingreso)
            + '>'
        )


class ClubDeportivo:

    """
    El club deportivo se caracteriza por tener un nombre, un teléfono y el
    registro de los diferentes socios pertenecientes al club.
    """

    # Escriba AQUI el constructor de la clase, los parámetros que recibe y la
    # inicialización de los atributos correspondientes.
    def __init__(self, nombre_club, telefono):
        self.nombre_club = nombre_club
        self.telefono = telefono
        self.registro_socios = Lista()

    # Método CD # 1
    def registrar_nuevo_socio(self, nuevo_socio):
        """
        Hay que considerar que no puede haber 2 socios con el mismo número de
        socio.

        :nuevo_socio: El nuevo socio a ser ingresado al club.
        :returns: True si el nuevo socio es admitido. False en caso contrario.
        :rtype: bool
        """
        socio = self.registro_socios.localizar(nuevo_socio)
        if socio is not None:
            return False
        else:
            return self.registro_socios.añadir(nuevo_socio)

    # Método CD # 2
    def registrar_nuevo_socio_despues_de(self, nuevo_socio, num_socio) -> bool:
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

        socio = self.registro_socios.localizar(nuevo_socio)
        if socio is None:
            socio = self.registro_socios.localizar(SocioClub(num_socio))

            cnt = 1
            for i in self.registro_socios:
                if i == socio:
                    return self.registro_socios.añadir(nuevo_socio, False, cnt)
                else:
                    cnt += 1
        return False

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

        nuevo_socio = SocioClub(num_socio)
        socio = self.registro_socios.localizar(nuevo_socio)
        if socio is not None:
            socio.direccion = nuevo_domicilio
            return socio
        else:
            return None

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
        lista = Lista()
        for i in self.registro_socios:
            if date.today().year - i.año_ingreso >= años_antg:
                lista.añadir(i)

        return lista

    # Método CD # 5
    def eliminar_socio(self, num_socio) -> bool:
        """
        Método que permite dar de baja a un socio dado un número de
        identificación de socio.

        :num_socio: Corresponde al número de identificación del socio a ser
        eliminado.
        :returns: True si el socio es expulsado del club de socios. False en
        caso contrario.
        :rtype: bool
        """
        nuevo_socio = SocioClub(num_socio)
        socio = self.registro_socios.localizar(nuevo_socio)
        if socio is not None:
            return self.registro_socios.suprimir(socio)
        else:
            return False

    # Método CD # 6
    def __len__(self):
        """
        Método que ...

        :returns: ... retorna el número de socios actualmente registrados en el
        club.
        :rtype: int
        """
        return len(self.registro_socios)

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
        return (
            '[Club Deportivo:'
            + self.nombre_club
            + '\nTeléfono:'
            + self.telefono
            + '\nTotal Socios:'
            + str(len(self))
            + '\n'
            + str(self.registro_socios)
            + ']'
        )
