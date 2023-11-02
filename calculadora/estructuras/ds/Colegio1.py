from adt.lists.sll import SinglyLinkedList
class Estudiante:
    def __init__(self, codigo, nombre="", nota=0.0):  # VALORES POR DEFECTO TODOS LOS PARAMETROS A LA DERECHA DEBEN TENER UN VALOR POR DEFECTO
        self.codigo = codigo  # ATRIBUTO
        self.nombre = nombre
        self.nota = nota

    def __eq__(self, otro_estudiante):  # comparar dos estudiantes por codigo
        if type(otro_estudiante) == type(self):
            # if isinstance(otro_estudiante,Estudiante):
            return self.codigo == otro_estudiante.codigo
        else:
            return False

    def __str__(self):
        cad_new = f"{'Codigo':>20} {'Nombre':^20} {'Nota':<20}" + '\n'
        cad_new += f"{self.codigo:>20} {self.nombre:^20} {str(self.nota):<20}"
        return cad_new

class Colegio:
    def __init__(self, nombre, nom_materia1, nom_materia2, nom_materia3, nom_materia4):
        # CONTRUCTOR INICIALIZA LOS ELEMENTOS BASICOS
        self.nombre = nombre
        self.lista = SinglyLinkedList()

        self.nom_materia1 = nom_materia1
        self.lista_materia1 = SinglyLinkedList()

        self.nom_materia2 = nom_materia2
        self.lista_materia2 = SinglyLinkedList()

        self.nom_materia3 = nom_materia3
        self.lista_materia3 = SinglyLinkedList()

        self.nom_materia4 = nom_materia4
        self.lista_materia4 = SinglyLinkedList()
        # guardar varios estudiantes

    def matricular(self, un_estudiante, indice_materia):
        if indice_materia == 1:
            if self.lista_materia1.append(un_estudiante):
                print("EL ESTUDIANTE " + un_estudiante.nombre + " FUE MATRICULADO EN LA MATERIA  " + self.nom_materia1)
            else:
                print("EL ESTUDIANTE " + un_estudiante.nombre + " NO FUE MATRICULADO EN LA MATERIA " + self.nom_materia1)
        if indice_materia == 2:
            if self.lista_materia2.append(un_estudiante):
                print("EL ESTUDIANTE " + un_estudiante.nombre + " FUE MATRICULADO EN LA MATERIA " + self.nom_materia2)
            else:
                print("EL ESTUDIANTE " + un_estudiante.nombre + " NO FUE MATRICULADO EN LA MATERIA " + self.nom_materia2)
        if indice_materia == 3:
            if self.lista_materia3.append(un_estudiante):
                print("EL ESTUDIANTE " + un_estudiante.nombre + " FUE MATRICULADO EN LA MATERIA " + self.nom_materia3)
            else:
                print("EL ESTUDIANTE " + un_estudiante.nombre + " NO FUE MATRICULADO EN LA MATERIA " + self.nom_materia3)
        if indice_materia == 4:
            if self.lista_materia4.append(un_estudiante):
                print("EL ESTUDIANTE " + un_estudiante.nombre + " FUE MATRICULADO EN LA MATERIA " + self.nom_materia4)
            else:
                print("EL ESTUDIANTE " + un_estudiante.nombre + " NO FUE MATRICULADO EN LA MATERIA " + self.nom_materia4)

        if not self.lista.search(un_estudiante):
             self.lista.append(un_estudiante)

    def expulsar(self, pos):
        rta = " SI" if self.lista.remove(pos) else " NO"
        print("El estudiante en la posicion " + str(pos) + rta + " fue EXPULSADO!")

    def expulsarcod(self,data):
        rta = " SI" if self.lista.delete(Estudiante(data)) else " NO"
        rta = " SI" if self.lista_materia1.delete(Estudiante(data)) else " NO"
        print("El estudiante con codigo " + str(data) + rta + " fue EXPULSADO!"+self.nom_materia1)
        rta = " SI" if self.lista_materia2.delete(Estudiante(data)) else " NO"
        print("El estudiante con codigo " + str(data) + rta + " fue EXPULSADO!"+self.nom_materia2)
        rta = " SI" if self.lista_materia3.delete(Estudiante(data)) else " NO"
        print("El estudiante con codigo " + str(data) + rta + " fue EXPULSADO!"+self.nom_materia3)
        rta = " SI" if self.lista_materia4.delete(Estudiante(data)) else " NO"
        print("El estudiante con codigo " + str(data) + rta + " fue EXPULSADO!"+self.nom_materia4)

    def registro(self, un_estudiante):
        reg_est = self.lista.search(un_estudiante)
        if reg_est:
            print("Registro Estudiantil:")
            #print("Còdigo Nombre Nota")
            #print(" Codigo".rjust(20)+"Nombre".center(40)+"Nota".ljust(60))
            print("-" * 18)
            print(reg_est)
        else:
            print(f"No tenemos registrado al estudiante de còdigo {un_estudiante.codigo} en nuestras bases de datos!")  # cadena formateada

    def reporte(self):
        print(f"\nColegio {self.nombre}")
        print("REPORTE DE ESTUDIANTES ACTUALMENTE MATRCULADOS")
        print("=" * 47)
        #print("Codigo Nombre Nota")
        print("-" * 18)
        self.lista.explorer()

    def reporte_por_materia(self, indice_materia):
        print(f"\n\n\nColegio {self.nombre}")
        if indice_materia == 1:
            print("REPORTE DE ESTUDIANTES ACTUALMENTE MATRCULADOS EN " + self.nom_materia1)
            print("=" * 47)
            print("-" * 18)
            self.lista_materia1.explorer()
        elif indice_materia == 2:
            print("REPORTE DE ESTUDIANTES ACTUALMENTE MATRCULADOS EN " + self.nom_materia2)
            print("=" * 47)
            print("-" * 18)
            self.lista_materia2.explorer()
        elif indice_materia == 3:
            print("REPORTE DE ESTUDIANTES ACTUALMENTE MATRCULADOS EN " + self.nom_materia3)
            print("=" * 47)
            print("-" * 18)
            self.lista_materia3.explorer()
        elif indice_materia == 4:
            print("REPORTE DE ESTUDIANTES ACTUALMENTE MATRCULADOS EN " + self.nom_materia4)
            print("=" * 47)
            print("-" * 18)
            self.lista_materia4.explorer()


    def promedio(self):
        acum = 0
        if self.lista.is_empty():
            return "No hay estudiantes MATRICULADOS para obtener el promedio"
            #input()
        else:
            for i in range (len(self.lista)):
                acum += self.lista.locate(i).nota

            prom = acum/len(self.lista)
            return "El promedio de notas de todos los estudiantes es: " +str(prom)

    def mayorNota(self):
        # if self.lista.is_empty():
        #     print("No hay estudiantes MATRICULADOS para obtener la mayor nota")
        #     input()
        # else:
        #     mayor_actual = self.lista.locate(0).nota
        #     for i in range(len(self.lista)):
        #         if mayor_actual < self.lista.locate(i).nota:
        #             mayor_actual=self.lista.locate(i).nota
        #     mayores_notas = SinglyLinkedList()
        #     for i in range(len(self.lista)):
        #         if mayor_actual == self.lista.locate(i).nota:
        #             mayores_notas.append(self.lista.locate(i))
        #     return "Reporte de estudiantes con mayor nota: \n" + str(mayores_notas)
        return mayorNota_Materia(self.lista)

    def mayorNota_Materia(self,lista):
        if lista.is_empty():
            print("No hay estudiantes MATRICULADOS para obtener la mayor nota")
            input()
        else:
            mayor_actual = lista.locate(0).nota
            for i in range(len(lista)):
                if mayor_actual < lista.locate(i).nota:
                    mayor_actual=lista.locate(i).nota
            mayores_notas = SinglyLinkedList()
            for i in range(len(lista)):
                if mayor_actual == lista.locate(i).nota:
                    mayores_notas.append(lista.locate(i))
            return "Reporte de estudiantes con mayor nota: \n" + str(mayores_notas)
