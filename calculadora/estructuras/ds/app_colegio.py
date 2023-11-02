from colegio import Colegio, Estudiante

def menu():
    print("\n\n\n ***MENU DE ADMINISTRACION DE COLEGIOS***")
    print("1-Crear un colegio")
    print("2-Matricular un estudiante")
    print("3-Expulsar un estudiante")
    print("4-Obtener el registro de un estudiante")
    print("5-Listar estudiantes matriculados")
    print("6-Promedio de estudiantes matriculados")
    print("7-Mayor Nota  de estudiantes matriculados")
    print("8-Salir")


if __name__ == "__main__":
    cole = None  # parte de que no existe el colegio
    while True:
        menu()
        opc = int(input("Opcion:"))
        if opc == 1:
            nom_cole = input("Nombre del colegio:")
            cole = Colegio(nom_cole)


        elif cole is not None:  # seguros de que el colegio existe
            if opc == 2:
                cod= input("Codigo del estudiante:")  # escribir el codigo
                nom = input("Nombre del estudiante:")  # el impu es para String
                nota = float(input("Nota del estudiante:"))  # conversion a float
                if nota>=0.0 and nota<=5.0:#
                    cole.matricular(Estudiante(cod, nom, round(nota,3)))  # metodo que contiene los elementos
                else: print("EL ESTUDIANTE "+nom.upper()+ " NO FUE MATRICULADO")

            elif opc == 3:
                pos_exp = int(input("Posicion para expulsar estudiante:"))
                cole.expulsar(pos_exp)

            elif opc == 4:
                cod = input("Codigo del estudiante:")  # escribir el codigo
                cole.registro(Estudiante(cod))  # paso el estudiante con su Codigo

            elif opc == 5:
                cole.reporte()  # el reporte invoca a su vez al explorer

            elif opc == 6:
                print(cole.promedio())

            elif opc ==7:
                print(cole.mayorNota())

            elif opc == 8:
                print("Bye Bye")
                break

            else:
                print("OPCION NO VALIDA")

        elif opc == 8:
            print("Bye Bye")
            break

        else:
            print("ADVERTENCIA: Es necesario crear un colegio antes de continuar")
        input("<ENTER> para continuar....")
