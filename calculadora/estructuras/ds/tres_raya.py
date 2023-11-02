import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from adt.lists.sll import SinglyLinkedList


class VentanaTR(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Tres en Raya")
        self.connect("destroy", Gtk.main_quit)

        self.alternar = 0
        self.casillas = SinglyLinkedList()
        malla = Gtk.Grid(row_homogeneous=True, column_homogeneous=True)

        for i in range(3):
            for j in range(3):
                casilla = Gtk.Button(label="")
                casilla.connect("clicked", self.on_casilla_clicked)
                malla.attach(casilla, top=i * 2, left=j * 2, height=2, width=2)
                self.casillas.append(casilla)

        self.add(malla)

    def on_casilla_clicked(self, casilla):
        if casilla.get_label() == "":
            if self.alternar % 2 == 0:
                casilla.set_label("X")
            else:
                casilla.set_label("O")
            self.alternar += 1

        if self.hay_ganador():
            dialog = Gtk.MessageDialog(
                parent=self,
                title="GANADOR!",
                text=f"Gana el juego con: {casilla.get_label()}.\nJugar Otra vez?",
                buttons=Gtk.ButtonsType.YES_NO,
            )
            respuesta = dialog.run()
            dialog.destroy()

            if respuesta == Gtk.ResponseType.YES:
                self.limpiar_malla()
            elif respuesta == Gtk.ResponseType.NO:
                self.destroy()
        else:
            cont = 0
            for i in range(len(self.casillas)):
                if self.casillas.locate(i).get_label() != "":
                    cont+=1
            if cont == len(self.casillas):
                dialog = Gtk.MessageDialog(
                    parent=self,
                    title="EMPATE!",
                    text="No hay ganador.\nJugar Otra vez?",
                    buttons=Gtk.ButtonsType.YES_NO,
                )
                respuesta = dialog.run()
                dialog.destroy()

                if respuesta == Gtk.ResponseType.YES:
                    self.limpiar_malla()
                elif respuesta == Gtk.ResponseType.NO:
                    self.destroy()


    def limpiar_malla(self):
        for i in range(9):
            self.casillas.locate(i).set_label("")
        self.alternar = 0

    def hay_ganador(self):
        return (
            (self.verificar_adyacencia(0, 1) and self.verificar_adyacencia(1, 2))
            or (self.verificar_adyacencia(3, 4) and self.verificar_adyacencia(4, 5))
            or (self.verificar_adyacencia(6, 7) and self.verificar_adyacencia(7, 8))
            or (self.verificar_adyacencia(0, 3) and self.verificar_adyacencia(3, 6))
            or (self.verificar_adyacencia(1, 4) and self.verificar_adyacencia(4, 7))
            or (self.verificar_adyacencia(2, 5) and self.verificar_adyacencia(5, 8))
            or (self.verificar_adyacencia(0, 4) and self.verificar_adyacencia(4, 8))
            or (self.verificar_adyacencia(2, 4) and self.verificar_adyacencia(4, 6))
        )

    def verificar_adyacencia(self, a, b):
        return (
            self.casillas.locate(a).get_label()
            == self.casillas.locate(b).get_label()
            and self.casillas.locate(a).get_label() != ""
        )


if __name__ == "__main__":
    VentanaTR().show_all()
    Gtk.main()
