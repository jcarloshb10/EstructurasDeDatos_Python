
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os, sys


from adt.lists.sll import SinglyLinkedList


class VentanaTR(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super(VentanaTR,self).__init__(*args, **kwargs)
        self.alternar = 0
        self.casillas = SinglyLinkedList()
        malla = Gtk.Grid(row_homogeneous=True, column_homogeneous=True)

        for i in range(3):
            for j in range(3):
                casilla = Gtk.Button.new_with_label("")
                casilla.connect("clicked", self.on_casilla_clicked)
                malla.attach(child=casilla, left=j, top=i, width=1, height=1)
                self.casillas.append(casilla)
        self.add(malla)

    def on_casilla_clicked(self, casilla):
        if casilla.get_label() == "":
            if self.alternar % 2 == 0:
                casilla.set_label("X")
            else:
                casilla.set_label("O")
        self.alternar += 1
        if self.hayGanador():
            dialogo = Gtk.MessageDialog(parent=self,
                                        buttons=Gtk.ButtonsType.YES_NO,
                                        text="El ganador es " + casilla.get_label(),
                                        secondary_text="Desea jugar Nuevamente",
                                        title="Ganador Tres en Fila"
                                        )

            dialogo.run()
            #dialogo.destroy()
            respuesta = dialogo.run()

            if respuesta == Gtk.ResponseType.YES:
                self.resetearCasillas()
            elif respuesta == Gtk.ResponseType.NO:
                self.destroy()

    def resetearCasillas(self):
        for i in range(9):
            self.casillas.locate(i).set_label("")
        self.alternar = 0

    def hayGanador(self):
        """Juego se compone de las siguientes casillas:
           0|1|2
           3|4|5
           6|7|8
        """
        if self.verificarAdyacencia(0, 1) and self.verificarAdyacencia(1, 2):
            return True
        elif self.verificarAdyacencia(3, 4) and self.verificarAdyacencia(4, 5):
            return True
        return False

    def verificarAdyacencia(self, a, b):
        print("a: ", self.casillas.locate(a).get_label())
        print("b: ", self.casillas.locate(b).get_label())
        if (self.casillas.locate(a).get_label() == self.casillas.locate(b).get_label()) and (not self.casillas.locate(b) == ""):
            return True
        return False


class AppHM(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super(AppHM, self).__init__(*args, **kwargs)
        self.win = None

    def do_activate(self):
        if not self.win:
            self.win = VentanaTR(title="Juego tres en raya",  application=self)
        self.win.show_all()


if __name__ == "__main__":
    app = AppHM()
    app.run()
    #sys.exit(app.run(sys.argv))
