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
    def __init__(self, nombre):  # CONTRUCTOR INICIALIZA LOS ELEMENTOS BASICOS
        self.nombre = nombre
        # guardar varios estudiantes
        self.lista = SinglyLinkedList()

    def matricular(self, un_estudiante):
        """if self.lista.search(un_estudiante):
            print("estudiante encontrado")"""
        if self.lista.append(un_estudiante):  # con self se vincula con los metodos
            # como retorna un booleano if
            print("El estudiante llamado " + un_estudiante.nombre + " FUE MATRICULADO!")
        else:
            print("El estudiante llamado " + un_estudiante.nombre + " NO FUE MATRICULADO!")

    def expulsar(self, pos):
        rta = "SI" if self.lista.remove(pos) else "NO"
        print("El estudiante en la posiciòn " + str(pos) + " " + rta + " fue EXPULSADO!")

    """def expulsarcod(self,data):
        rta = "SI" if self.lista.delete(self.codigo)"""

    def registro(self, un_estudiante):
        reg_est = self.lista.search(un_estudiante)
        if reg_est is not None:
            print("Registro Estudiantil:")
            #print("Còdigo Nombre Nota")
            #print(" Codigo".rjust(20)+"Nombre".center(40)+"Nota".ljust(60))
            print("-" * 18)
            print(reg_est)
        else:
            print(f"No tenemos registrado al estudiante de còdigo {un_estudiante.codigo} en nuestras bases de datos!")  # cadena formateada

    def reporte(self):
        print(f"\n\n\nColegio {self.nombre}")
        print("REPORTE DE ESTUDIANTES ACTUALMENTE MATRCULADOS")
        print("=" * 47)
        #print("Codigo Nombre Nota")
        print("-" * 18)
        self.lista.explorer()

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
        if self.lista.is_empty():
            print("No hay estudiantes MATRICULADOS para obtener la mayor nota")
            input()
        else:
            mayor_actual = self.lista.locate(0).nota
            for i in range(len(self.lista)):
                if mayor_actual < self.lista.locate(i).nota:
                    mayor_actual=self.lista.locate(i).nota
            mayores_notas = SinglyLinkedList()
            for i in range(len(self.lista)):
                if mayor_actual == self.lista.locate(i).nota:
                    mayores_notas.append(self.lista.locate(i))
            return "Reporte de estudiantes con mayor nota: \n" + str(mayores_notas)




"""estudiantes = SinglyLinkedList()
estudiantes.append(Estudiante ("123","JUAN",3.5))
estudiantes.append(Estudiante("456","MARIA",2.9))
estudiantes.append(Estudiante("789","Pedro",5.0))


estudiantes.explorer()

print ("Buscando.....",estudiantes.search(Estudiante("789")))"""

"""if __name__ == "__main__":
    estudiantes = []
    for i in range(11):
        estudiantes += [Estudiante(str(i + 1), str(i + 1), float(i + 1))]

    print("codigo\t\tnombre\t\tnota")

    for i in estudiantes:
        print(f"{i.codigo}\t\t{i.nombre}\t\t{i.nota}")

    import math

    print(math.pi)
    print(round(math.pi, 5))"""
