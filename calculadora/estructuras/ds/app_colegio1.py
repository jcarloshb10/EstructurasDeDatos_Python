from Colegio1 import Colegio, Estudiante

def menu():
    print("\n\n***MENU DE ADMINISTRACION DE COLEGIOS***")
    print("1-Crear un colegio")
    print("2-Matricular un estudiante")
    print("3-Expulsar un estudiante")
    print("4-Obtener el registro de un estudiante")
    print("5-Listado General de estudiantes matriculados")
    print("6-Promedio de estudiantes matriculados")
    print("7-Mayor Nota de estudiantes matriculados")
    print("8-Listado por Materia")
    print("9-Nota maxima por materia")
    print("10-Salir")


def menu_matricular_materias(nm1, nm2, nm3, nm4):
    print("\n***MENU MATRICULAR MATERIAS***")
    print("1-Matricular en " + nm1)
    print("2-Matricular en " + nm2)
    print("3-Matricular en " + nm3)
    print("4-Matricular en " + nm4)
    print("5-Finalizar ")

def menu_mostrar_materias(nm1, nm2, nm3, nm4):
    print("\n***MENU MOSTRAR MATERIAS***")
    print("1-Mostrar Estudiantes en " + nm1)
    print("2-Mostrar Estudiantes en " + nm2)
    print("3-Mostrar Estudiantes en " + nm3)
    print("4-Mostrar Estudiantes en " + nm4)
    print("5-Finalizar ")


if __name__ == "__main__":
    cole = None  # parte de que no existe el colegio

    while True:
        menu()
        opc = int(input("Opcion: "))
        if opc == 1:
            nom_cole = input("Nombre del colegio: ")
            nom_materia1 = input("Nombre de la materia 1: ")
            nom_materia2 = input("Nombre de la materia 2: ")
            nom_materia3 = input("Nombre de la materia 3: ")
            nom_materia4 = input("Nombre de la materia 4: ")
            cole = Colegio(nom_cole,nom_materia1,nom_materia2,nom_materia3,nom_materia4)

        elif cole is not None:  # seguros de que el colegio existe
            if opc == 2:
                cod = input("Codigo del estudiante: ")  # escribir  el codigo

                if cole.lista.search(Estudiante(cod)):
                    pass
                else:
                    nom = input("Nombre del estudiante: ")  # el impu es para String

                while True:
                    menu_matricular_materias(cole.nom_materia1, cole.nom_materia2, cole.nom_materia3, cole.nom_materia4)

                    opc = int(input("Opcion: "))
                    if opc == 1:
                        print("Matriculado en "+cole.nom_materia1)
                    elif opc == 2:
                        print("Matriculado en "+cole.nom_materia2)
                    elif opc == 3:
                         print("Matriculado en "+cole.nom_materia3)
                    elif opc == 4:
                        print("Matriculado en "+cole.nom_materia4)
                    elif opc == 5:
                        print("Terminado el registro de materias")
                        break

                    if opc in [1, 2, 3, 4]:
                        nota = float(input("Nota del estudiante: "))  # conversion a float
                        if nota >= 0.0 and nota <= 5.0:
                            cole.matricular(Estudiante(cod, nom, round(nota,3)), opc)  # metodo que contiene los elementos
                        else:
                            print("EL ESTUDIANTE " + nom.upper() + " NO FUE MATRICULADO")

            elif opc == 3:
                print("Como desea expulsar el estudiante:")
                print("1.Posicion")
                print("2.Codigo")

                opc = int(input("Opcion:"))
                if opc == 1:
                    pos_exp = int(input("Posicion para expulsar estudiante:"))
                    cole.expulsar(pos_exp)
                elif opc == 2:
                    cod_exp = input("codigo para expulsar estudiante:")
                    cole.expulsarcod(cod_exp)

            elif opc == 4:
                cod = input("Codigo del estudiante:")  # escribir el codigo
                cole.registro(Estudiante(cod))  # paso el estudiante con su Codigo

            elif opc == 5:
                print("==============================================================================")
                cole.reporte()  # el reporte invoca a su vez al explorer

            elif opc == 6:
                print(cole.promedio())

            elif opc == 7:
                print(cole.mayorNota())
            elif opc == 8:
                while True:
                    menu_mostrar_materias(cole.nom_materia1, cole.nom_materia2, cole.nom_materia3, cole.nom_materia4)

                    opc = int(input("Opcion: "))
                    if opc == 1:
                        cole.reporte_por_materia(opc)
                    elif opc == 2:

                        cole.reporte_por_materia(opc)
                    elif opc == 3:

                         cole.reporte_por_materia(opc)
                    elif opc == 4:

                        cole.reporte_por_materia(opc)
                    elif opc == 5:
                        print("Terminado el Listado de  materias")
                        break

            elif opc == 9:
                print("PARA MATERIA " + cole.nom_materia1)
                print(cole.mayorNota_Materia(cole.lista_materia1))
                print("PARA MATERIA " + cole.nom_materia2)
                print(cole.mayorNota_Materia(cole.lista_materia2))
                print("PARA MATERIA " + cole.nom_materia3)
                print(cole.mayorNota_Materia(cole.lista_materia3))
                print("PARA MATERIA " + cole.nom_materia4)
                print(cole.mayorNota_Materia(cole.lista_materia4))

            elif opc == 10:
                print("Bye Bye")
                break
            else:
                print("OPCION NO VALIDA")

        elif opc == 10:
            print("Bye Bye")
            break
        else:
            print("ADVERTENCIA: Es necesario crear un colegio antes de continuar")

        input("<ENTER> para continuar....")
