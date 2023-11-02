#!/usr/bin/env python3
from test_builder import TestBuilder
from gestionar_club import SocioClub, ClubDeportivo
import unittest
import traceback


def gen_lst_datos_socios():
    """Función especial que permite la creación tuplas con datos de socios
    utilizados en las diferentes pruebas, devolviendo una lista con los datos
    para la vinculación de diferentes socios en el Club Deportivo.
    """
    sc_1 = ("123", "Javier Díaz", "Clle 123", 1989)
    sc_2 = ("234", "María Rosero", "Clle 234", 2018)
    sc_3 = ("345", "Daniel Salas", "Clle 345", 1999)
    sc_4 = ("456", "Carolina Patiño", "Clle 456", 2016)
    sc_5 = ("567", "Alexander Romero", "Clle 567", 2009)
    sc_6 = ("678", "Mario Rodríguez", "Clle 678", 1975)
    sc_7 = ("789", "Carlos Gómez", "Clle 789", 2002)
    sc_8 = ("890", "Andrea Calderón", "Clle 890", 1995)
    sc_9 = ("901", "Jesús Ruales", "Clle 901", 1987)
    sc_10 = ("110", "Lucia Benavides", "Clle 110", 2006)

    lst_soc = [sc_1, sc_2, sc_3, sc_4, sc_5, sc_6, sc_7, sc_8, sc_9, sc_10]
    return lst_soc


class SocioColado:
    """ Clase escpecial que simulará un socio con atributos casi similares a
        los del socio verdadero.
    """

    def __init__(self, num_soc):
        self.num_soc = num_soc
        self.nombre = "Juanito Colado"
        self.domicilio = "Domicilio"
        self.año_ingr = 0

    def __str__(self):
        return ("Socio Colado #" + self.num_soc)


class TestClubDeportivo(TestBuilder):
    """ Es posible desactivar cualquiera de las pruebas colocando el valor de
        cero a cualquiera de ellas en el siguiente diccionario:
    """
    dict_pruebas = {"registro": 1, "registro_despues": 1, "modificar": 1,
                    "antigüedad": 1, "eliminar": 1, "todo": 1}

    def setUp(self):
        # Creación del Club Deportivo
        self.club_depor = ClubDeportivo("Python Sports Club", "8-852670")

    def test_0(self):
        self.presentación("Test Club Deportivo")

    def test_1_registrar_nuevo_socio(self):
        iTest = 1
        sTitle = "Nuevos socios y número de socios registrados en el club"
        fMax_nota = 0.7
        Nt1_1 = fMax_nota * 0.30 / 6  # Registrar
        Nt1_2 = fMax_nota * 0.20 / 4  # Tamaño del Club
        Nt1_3 = fMax_nota * 0.20 / 2  # Informe
        if self.dict_pruebas.get("registro"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(0, len, [self.club_depor], Nt1_2, le)

            # Comprobación del registro de nuevos socios en la Club Deportivo
            lst_prod = gen_lst_datos_socios()
            Nt1_4 = fMax_nota * 0.30 / len(lst_prod)  # Registrar 2
            cr_i = 0
            for datos_socio in lst_prod:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(True,
                                        self.club_depor.
                                        registrar_nuevo_socio,
                                        [unSocio],
                                        Nt1_4, le, cr_i)
                cr_i += 1

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, len, [self.club_depor], Nt1_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:10\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<345--Daniel Salas--Clle 345--1999> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987> "
                       "<110--Lucia Benavides--Clle 110--2006>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt1_3, le)

            # Comprobación de la validación de socios ya existentes en el
            # Club Deportivo, teniendo en cuenta únicamente el número de socio
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.registrar_nuevo_socio,
                                    [SocioClub("456", "Carlos Hernández",
                                               "Clle 456", 1979)], Nt1_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, len, [self.club_depor], Nt1_2, le)

            # Agregamos un nuevo socio al club
            sc_11 = SocioClub("611", "Edwin Martinez", "Clle 611", 1999)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.registrar_nuevo_socio,
                                    [sc_11], Nt1_1, le)

            # Comprobación de la validación de socios ya existentes en el
            # Club Deportivo, teniendo en cuenta únicamente el número de socio
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.registrar_nuevo_socio,
                                    [SocioClub("789", "Sandra Rojas",
                                               "Clle 789", 1968)], Nt1_1, le)

            # Agregamos un nuevo socio al club
            sc_12 = SocioClub("712", "Vanessa Toro", "Clle 712", 1981)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.registrar_nuevo_socio,
                                    [sc_12], Nt1_1, le)

            # Comprobación de la validación de socios ya existentes en el
            # Club Deportivo, teniendo en cuenta únicamente el número de socio
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.registrar_nuevo_socio,
                                    [SocioClub("110", "Zoila Vargas",
                                               "Clle 110", 2005)], Nt1_1, le)

            # Intento de ingreso de un socio colado al club
            scol = SocioColado("666")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.registrar_nuevo_socio,
                                    [scol], Nt1_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(12, len, [self.club_depor], Nt1_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:12\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<345--Daniel Salas--Clle 345--1999> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987> "
                       "<110--Lucia Benavides--Clle 110--2006> "
                       "<611--Edwin Martinez--Clle 611--1999> "
                       "<712--Vanessa Toro--Clle 712--1981>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt1_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_2_registrar_nuevo_socio_despues_de(self):
        iTest = 2
        sTitle = "Nuevos socios a registrar después de un socio existente"
        fMax_nota = 1.4
        Nt2_1 = fMax_nota * 0.50 / 6  # Registrar después
        Nt2_2 = fMax_nota * 0.20 / 3  # Tamaño del Club
        Nt2_3 = fMax_nota * 0.30 / 3  # Informe
        if self.dict_pruebas.get("registro_despues"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ########################
            """
            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(0, len, [self.club_depor], Nt2_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:0\n"
                       "]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt2_3, le)

            # Registro de socios en el Club Deportivo
            lst_prod = gen_lst_datos_socios()
            for datos_socio in lst_prod:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                self.club_depor.registrar_nuevo_socio(unSocio)

            # Agregamos un nuevo socio al club después del socio identificado
            # con el número 234
            sc_11 = SocioClub("768", "Edwin Martinez", "Clle 768", 1999)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.
                                    registrar_nuevo_socio_despues_de,
                                    [sc_11, "234"], Nt2_1, le)

            # Intento por agrega un socio que ya existe, al menos con el mismo
            # número de socio, despues del socio identificado con el número 123
            sc_3e = SocioClub("345", "Daniel Salas R.", "Clle 345 R.", 1900)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.
                                    registrar_nuevo_socio_despues_de,
                                    [sc_3e, "123"], Nt2_1, le)

            # Agregamos un nuevo socio al club después de la posición del socio
            # identificado con el número 123
            sc_7 = SocioClub("798", "Vanessa Toro", "Clle 798", 1981)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.
                                    registrar_nuevo_socio_despues_de,
                                    [sc_7, "123"], Nt2_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(12, len, [self.club_depor], Nt2_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:12\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<798--Vanessa Toro--Clle 798--1981> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<768--Edwin Martinez--Clle 768--1999> "
                       "<345--Daniel Salas--Clle 345--1999> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987> "
                       "<110--Lucia Benavides--Clle 110--2006>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt2_3, le)

            # Intentamos agregar un nuevo socio al club, pero el socio con el
            # número 777 NO EXISTE
            sc_8 = SocioClub("890", "Camilo Osejo", "Clle 890", 2011)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.
                                    registrar_nuevo_socio_despues_de,
                                    [sc_8, "777"],
                                    Nt2_1, le)

            # Agregamos un nuevo socio al club después de la posición del socio
            # identificado con el número 110, que es úlitmo registrado
            sc_9 = SocioClub("120", "Paola Rivera", "Clle 120", 1951)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.
                                    registrar_nuevo_socio_despues_de,
                                    [sc_9, "110"],
                                    Nt2_1, le)

            # Intento de ingreso de un socio colado al club ddespués de la
            # posición del socio identificado con el número 345
            scol = SocioColado("999")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.
                                    registrar_nuevo_socio_despues_de,
                                    [scol, "345"],
                                    Nt2_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(13, len, [self.club_depor], Nt2_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:13\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<798--Vanessa Toro--Clle 798--1981> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<768--Edwin Martinez--Clle 768--1999> "
                       "<345--Daniel Salas--Clle 345--1999> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987> "
                       "<110--Lucia Benavides--Clle 110--2006> "
                       "<120--Paola Rivera--Clle 120--1951>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt2_3, le)
            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_3_modificar_domicilio_socio(self):
        iTest = 3
        sTitle = "Cambio de domicilio a Socio"
        fMax_nota = 0.4
        Nt3_1 = fMax_nota * 0.60 / 4  # Modificar
        Nt3_2 = fMax_nota * 0.15 / 1  # Tamaño del Club
        Nt3_3 = fMax_nota * 0.25 / 1  # Informe
        if self.dict_pruebas.get("modificar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Registro de socios en el Club Deportivo
            lst_prod = gen_lst_datos_socios()
            for datos_socio in lst_prod:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                self.club_depor.registrar_nuevo_socio(unSocio)

            # Modificación del domicilio del socio de número 345 y comprobamos
            # el cambio, comparando la cadena de presentación del socio
            # modificado
            soc_mod_3 = self.club_depor.modificar_domicilio_socio(
                "345", "New Clle 345")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(("<345--Daniel Salas--"
                                     "New Clle 345--1999>"),
                                    str, [soc_mod_3], Nt3_1, le)

            # Modificación del domicilio del socio de número 110 y comprobamos
            # el cambio, comparando la cadena de presentación del socio
            # modificado
            soc_mod_10 = self.club_depor.modificar_domicilio_socio(
                "110", "New Clle 110")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(("<110--Lucia Benavides"
                                     "--New Clle 110--2006>"),
                                    str, [soc_mod_10], Nt3_1, le)

            # Modificación del domicilio del socio de número 951 que NO EXISTE
            # y comparamos el resultado devuelto por el método
            # 'modificar_domicilio_socio' con None
            soc_mod = self.club_depor.modificar_domicilio_socio(
                "951", "New Clle 951")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción(None, soc_mod, Nt3_1, le)

            # Modificación del domicilio del socio de número 123 y comprobamos
            # el cambio, comparando la cadena de presentación del socio
            # modificado
            soc_mod_1 = self.club_depor.modificar_domicilio_socio(
                "123", "New Clle 123")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(("<123--Javier Díaz"
                                     "--New Clle 123--1989>"),
                                    str, [soc_mod_1], Nt3_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, len, [self.club_depor], Nt3_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:10\n"
                       "<123--Javier Díaz--New Clle 123--1989> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<345--Daniel Salas--New Clle 345--1999> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987> "
                       "<110--Lucia Benavides--New Clle 110--2006>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt3_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_4_reporte_antigüedad(self):
        iTest = 4
        sTitle = "Listado de socios con una determinada antigüedad"
        fMax_nota = 0.9
        Nt4_1 = fMax_nota * 0.60 / 5  # Antigüedad (Informe)
        Nt4_2 = fMax_nota * 0.15 / 5  # Tamaño de la lista de Angtigüedad
        Nt4_3 = fMax_nota * 0.25 / 19  # Comparación de socios antigüos
        if self.dict_pruebas.get("antigüedad"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Registro de socios en el Club Deportivo
            lst_prod = gen_lst_datos_socios()
            for datos_socio in lst_prod:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                self.club_depor.registrar_nuevo_socio(unSocio)

            # Generamos un listado con todos los socios que tienen una
            # antigüedad mayor o igual a 5 años
            lst_ra_5 = self.club_depor.reporte_antigüedad(5)
            sAntig = ("<123--Javier Díaz--Clle 123--1989> "
                      "<345--Daniel Salas--Clle 345--1999> "
                      "<567--Alexander Romero--Clle 567--2009> "
                      "<678--Mario Rodríguez--Clle 678--1975> "
                      "<789--Carlos Gómez--Clle 789--2002> "
                      "<890--Andrea Calderón--Clle 890--1995> "
                      "<901--Jesús Ruales--Clle 901--1987> "
                      "<110--Lucia Benavides--Clle 110--2006>")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sAntig, str, [lst_ra_5], Nt4_1, le)

            # Número de socios con la antigüedad mayor o igual a 5 años
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(8, len, [lst_ra_5], Nt4_2, le)

            # Comparación del listado de socios con antigüedad mayor o igual a
            # 5 años
            lst_ra_5_OK = [lst_prod[0], lst_prod[2], lst_prod[4], lst_prod[5],
                           lst_prod[6], lst_prod[7], lst_prod[8], lst_prod[9]]
            cr_i = 0
            for datos_socio in lst_ra_5_OK:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(True, unSocio in lst_ra_5, Nt4_3,
                                       le, cr_i)
                cr_i += 1

            # Generamos un listado con todos los socios que tienen una
            # antigüedad mayor o igual a 15 años
            lst_ra_15 = self.club_depor.reporte_antigüedad(15)
            sAntig = ("<123--Javier Díaz--Clle 123--1989> "
                      "<345--Daniel Salas--Clle 345--1999> "
                      "<678--Mario Rodríguez--Clle 678--1975> "
                      "<789--Carlos Gómez--Clle 789--2002> "
                      "<890--Andrea Calderón--Clle 890--1995> "
                      "<901--Jesús Ruales--Clle 901--1987>")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sAntig, str, [lst_ra_15], Nt4_1, le)

            # Número de socios con la antigüedad mayor o igual a 15 años
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(6, len, [lst_ra_15], Nt4_2, le)

            # Comparación del listado de socios con antigüedad mayor o igual a
            # 15 años

            lst_ra_15_OK = [lst_prod[0], lst_prod[2], lst_prod[5], lst_prod[6],
                            lst_prod[7], lst_prod[8]]
            cr_i = 0
            for datos_socio in lst_ra_15_OK:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(True, unSocio in lst_ra_15, Nt4_3,
                                       le, cr_i)
                cr_i += 1

            # Generamos un listado con todos los socios que tienen una
            # antigüedad mayor o igual a 30 años
            lst_ra_30 = self.club_depor.reporte_antigüedad(30)
            sAntig = ("<123--Javier Díaz--Clle 123--1989> "
                      "<678--Mario Rodríguez--Clle 678--1975> "
                      "<901--Jesús Ruales--Clle 901--1987>")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sAntig, str, [lst_ra_30], Nt4_1, le)

            # Número de socios con la antigüedad mayor o igual a 30 años
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(3, len, [lst_ra_30], Nt4_2, le)

            # Comparación del listado de socios con antigüedad mayor o igual a
            # 30 años
            lst_ra_30_OK = [lst_prod[0], lst_prod[5], lst_prod[8]]
            cr_i = 0
            for datos_socio in lst_ra_30_OK:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(True, unSocio in lst_ra_30, Nt4_3,
                                       le, cr_i)
                cr_i += 1

            # Generamos un listado con todos los socios que tienen una
            # antigüedad mayor o igual a 44 años
            lst_ra_44 = self.club_depor.reporte_antigüedad(44)
            sAntig = ("<678--Mario Rodríguez--Clle 678--1975>")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sAntig, str, [lst_ra_44], Nt4_1, le)

            # Número de socios con la antigüedad mayor o igual a 44 años
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(1, len, [lst_ra_44], Nt4_2, le)

            # Comparación del listado de socios con antigüedad mayor o igual a
            # 44 años
            lst_ra_44_OK = [lst_prod[5]]
            cr_i = 0
            for datos_socio in lst_ra_44_OK:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(True, unSocio in lst_ra_44, Nt4_3,
                                       le, cr_i)
                cr_i += 1

            # Generamos un listado con todos los socios que tienen una
            # antigüedad mayor o igual a 45 años
            lst_ra_45 = self.club_depor.reporte_antigüedad(45)
            sAntig = ("")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sAntig, str, [lst_ra_45], Nt4_1, le)

            # Número de socios con la antigüedad mayor o igual a 45 años
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(0, len, [lst_ra_45], Nt4_2, le)

            # Comparación del listado de socios con antigüedad mayor o igual a
            # 45 años
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True, lst_ra_45.es_vacia, [], Nt4_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_5_eliminar_socio(self):
        iTest = 5
        sTitle = "Eliminar un socio del Club"
        fMax_nota = 1.1
        Nt5_1 = fMax_nota * 0.60 / 6  # Eliminar socio
        Nt5_2 = fMax_nota * 0.15 / 6  # Tamaño del Club
        Nt5_3 = fMax_nota * 0.25 / 6  # Informe
        if self.dict_pruebas.get("eliminar"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Registro de socios en el Club Deportivo
            lst_prod = gen_lst_datos_socios()
            for datos_socio in lst_prod:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                self.club_depor.registrar_nuevo_socio(unSocio)

            # Eliminación del socio con el número 345
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.eliminar_socio,
                                    ["345"], Nt5_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(9, len, [self.club_depor], Nt5_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:9\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987> "
                       "<110--Lucia Benavides--Clle 110--2006>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt5_3, le)

            # Eliminación del socio con el número 761 que NO EXISTE
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.eliminar_socio,
                                    ["761"], Nt5_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(9, len, [self.club_depor], Nt5_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:9\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987> "
                       "<110--Lucia Benavides--Clle 110--2006>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt5_3, le)

            # Eliminación del socio con el número 110
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.eliminar_socio,
                                    ["110"], Nt5_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(8, len, [self.club_depor], Nt5_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:8\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt5_3, le)

            # Eliminación del socio con el número 234
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.eliminar_socio,
                                    ["234"], Nt5_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(7, len, [self.club_depor], Nt5_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:7\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt5_3, le)

            # Eliminación del socio con el número 345 que YA NO EXISTE
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.eliminar_socio,
                                    ["345"], Nt5_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(7, len, [self.club_depor], Nt5_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:7\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt5_3, le)

            # Eliminación del socio con el número 123
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.eliminar_socio,
                                    ["123"], Nt5_1, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(6, len, [self.club_depor], Nt5_2, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:6\n"
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt5_3, le)

            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_6_todo(self):
        iTest = 6
        sTitle = ("Registrar, Modificar, Eliminar e Informes de Antigüedad " +
                  "del Club Deportivo")
        fMax_nota = 0.5
        Nt6_1 = fMax_nota * 0.10 / 6  # Tamaño del Club
        Nt6_2 = fMax_nota * 0.15 / 6  # Informe
        Nt6_4 = fMax_nota * 0.05 / 2  # Registrar nuevo socio
        Nt6_5 = fMax_nota * 0.20 / 1  # Registrar nuevo socio después
        Nt6_6 = fMax_nota * 0.10 / 1  # Modificar socio
        Nt6_7 = fMax_nota * 0.15 / 3  # Eliminar socio
        Nt6_8 = fMax_nota * 0.10 / 7  # Antigüedad
        if self.dict_pruebas.get("todo"):
            _nota = self.nota
            self.titulo(iTest, sTitle)
            """
            ##################### INICIO DE PRUEBAS ###########################
            """
            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(0, len, [self.club_depor], Nt6_1, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:0\n"
                       "]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt6_2, le)

            # Comprobación del registro de nuevos socios en la Club Deportivo
            lst_prod = gen_lst_datos_socios()
            Nt6_3 = fMax_nota * 0.15 / len(lst_prod)  # Registro nuevo socio
            cr_i = 0
            for datos_socio in lst_prod:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción2(True,
                                        self.club_depor.
                                        registrar_nuevo_socio,
                                        [unSocio],
                                        Nt6_3, le, cr_i)
                cr_i += 1

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, len, [self.club_depor], Nt6_1, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:10\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<345--Daniel Salas--Clle 345--1999> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987> "
                       "<110--Lucia Benavides--Clle 110--2006>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt6_2, le)

            # Comprobación de la validación de socios ya existentes en el
            # Club Deportivo, teniendo en cuenta únicamente el número de socio
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.registrar_nuevo_socio,
                                    [SocioClub("456", "Martha Benavides",
                                               "Clle 456", 1968)], Nt6_4, le)

            # Intento de ingreso de un socio colado al club
            scol = SocioColado("000")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.registrar_nuevo_socio,
                                    [scol], Nt6_4, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(10, len, [self.club_depor], Nt6_1, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:10\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<345--Daniel Salas--Clle 345--1999> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987> "
                       "<110--Lucia Benavides--Clle 110--2006>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt6_2, le)

            # Agregamos un nuevo socio al club después del socio identificado
            # con el número 678
            sc_11 = SocioClub("768", "Julio Muñoz", "Clle 768", 1986)
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.
                                    registrar_nuevo_socio_despues_de,
                                    [sc_11, "678"], Nt6_5, le)

            # Modificación del domicilio del socio de número 110 y comprobamos
            # el cambio, comparando la cadena de presentación del socio
            # modificado
            soc_mod_10 = self.club_depor.modificar_domicilio_socio(
                "110", "New Clle 110")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(("<110--Lucia Benavides--"
                                     "New Clle 110--2006>"),
                                    str, [soc_mod_10], Nt6_6, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(11, len, [self.club_depor], Nt6_1, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:11\n"
                       "<123--Javier Díaz--Clle 123--1989> "
                       "<234--María Rosero--Clle 234--2018> "
                       "<345--Daniel Salas--Clle 345--1999> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<768--Julio Muñoz--Clle 768--1986> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<901--Jesús Ruales--Clle 901--1987> "
                       "<110--Lucia Benavides--New Clle 110--2006>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt6_2, le)

            # Eliminación del socio con el número 901
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.eliminar_socio,
                                    ["901"], Nt6_7, le)

            # Eliminación del socio con el número 123
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(True,
                                    self.club_depor.eliminar_socio,
                                    ["123"], Nt6_7, le)

            # Generamos un listado con todos los socios que tienen una
            # antigüedad mayor o igual a 7 años
            lst_ra_7 = self.club_depor.reporte_antigüedad(7)
            sAntig = ("<345--Daniel Salas--Clle 345--1999> "
                      "<567--Alexander Romero--Clle 567--2009> "
                      "<678--Mario Rodríguez--Clle 678--1975> "
                      "<768--Julio Muñoz--Clle 768--1986> "
                      "<789--Carlos Gómez--Clle 789--2002> "
                      "<890--Andrea Calderón--Clle 890--1995> "
                      "<110--Lucia Benavides--New Clle 110--2006>")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sAntig, str, [lst_ra_7], Nt6_2, le)

            # Número de socios con la antigüedad mayor o igual a 7 años
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(7, len, [lst_ra_7], Nt6_1, le)

            # Comparación del listado de socios con antigüedad mayor o igual a
            # 7 años
            lst_ra_7_OK = [lst_prod[2], lst_prod[4], lst_prod[5],
                           ('768', 'Julio Muñoz', 'Clle 768', 1986),
                           lst_prod[6], lst_prod[7], lst_prod[9]]

            cr_i = 0
            for datos_socio in lst_ra_7_OK:
                sNumSoc, sNombre, sDomic, iAñoIng = datos_socio
                unSocio = SocioClub(sNumSoc, sNombre, sDomic, iAñoIng)
                le = (traceback.extract_stack()[-1])[1] + 1
                self.comprobarAserción(True, unSocio in lst_ra_7, Nt6_8,
                                       le, cr_i)
                cr_i += 1

            # Eliminación del socio con el número 111 que NO EXISTE
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(False,
                                    self.club_depor.eliminar_socio,
                                    ["111"], Nt6_7, le)

            # Calculo del número de socios en el club
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(9, len, [self.club_depor], Nt6_1, le)

            # Presentación del Club Deportivo
            sInfoCD = ("[Club Deportivo:Python Sports Club\n"
                       "Teléfono:8-852670\n"
                       "Total Socios:9\n"
                       "<234--María Rosero--Clle 234--2018> "
                       "<345--Daniel Salas--Clle 345--1999> "
                       "<456--Carolina Patiño--Clle 456--2016> "
                       "<567--Alexander Romero--Clle 567--2009> "
                       "<678--Mario Rodríguez--Clle 678--1975> "
                       "<768--Julio Muñoz--Clle 768--1986> "
                       "<789--Carlos Gómez--Clle 789--2002> "
                       "<890--Andrea Calderón--Clle 890--1995> "
                       "<110--Lucia Benavides--New Clle 110--2006>]")
            le = (traceback.extract_stack()[-1])[1] + 1
            self.comprobarAserción2(sInfoCD, str, [self.club_depor], Nt6_2, le)
            """
            ################ PRESENTACIÓN DE LA NOTA DEL TEST #################
            """
            self.nota_test(iTest, fMax_nota, _nota)

    def test_nota(self):
        """
        INFORME DE LA NOTA FINAL
        """
        self.nota_final()


if __name__ == "__main__":
    unittest.main(verbosity=0)
