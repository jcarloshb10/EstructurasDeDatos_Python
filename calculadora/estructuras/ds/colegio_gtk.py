import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from adt.lists.sll import SinglyLinkedList
from estudiante import Estudiante


class VentanaPrincipal(Gtk.ApplicationWindow):  # heredando
    def __init__(self, *args, **kwargs):  # (**diccionario, *Tupla)
        super().__init__(*args, **kwargs)
        # crea lo basico de una ventana a travez de super
        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box_main)  # self -> ventana
        # Frame para insertar estudiantes
        frm_ing = Gtk.Frame(
            label="Ingreso de Estudiantes", margin_left=5, margin_right=5
        )
        box_main.add(frm_ing)
        grid_ing = Gtk.Grid(column_homogeneous=True, column_spacing=10)
        lbl_cod = Gtk.Label(label="Còdigo:")
        lbl_nom = Gtk.Label(label="Nombre:")
        lbl_nota = Gtk.Label(label="Nota:")
        grid_ing.attach(child=lbl_cod, left=0, top=0, width=1, height=1)
        grid_ing.attach(child=lbl_nom, left=1, top=0, width=1, height=1)
        grid_ing.attach(child=lbl_nota, left=2, top=0, width=1, height=1)
        self.ent_cod = Gtk.Entry()
        self.ent_nom = Gtk.Entry()
        self.ent_nota = Gtk.Entry()
        grid_ing.attach(child=self.ent_cod, left=0, top=1, width=1, height=1)
        grid_ing.attach(child=self.ent_nom, left=1, top=1, width=1, height=1)
        grid_ing.attach(child=self.ent_nota, left=2, top=1, width=1, height=1)
        btn_ing = Gtk.Button(label="Ingresar")
        btn_ing.connect("clicked", self.on_btn_ing_clicked)
        grid_ing.attach(child=btn_ing, left=0, top=2, width=1, height=1)
        frm_ing.add(grid_ing)
        # creacion de la lista de estudiantes del __Colegio__
        self.estudiantes = SinglyLinkedList()

    def on_btn_ing_clicked(self, btn_ing):
        un_estudiante = Estudiante(
            self.ent_cod.get_text(),
            self.ent_nom.get_text(),
            float(self.ent_nota.get_text()),
        )
        if not self.estudiante.search(un_estudiante):
            if self.estudiante.append(un_estudiante):
                dialogo = Gtk.MessageDialog(
                    parent=self,
                    buttons=Gtk.ButtonsType.OK,
                    text=boton.get_label()
                    + "Estudiante Adicionado Exitosamente!",
                )

                # print("Estudiante Adicionado Exitosamente!")
            else:
                dialogo = Gtk.MessageDialog(
                    parent=self,
                    buttons=Gtk.ButtonsType.OK,
                    text=boton.get_label() + "Estudiante NO pudo adicionarse!",
                )
                # print("Estudiante NO pudo adicionarse!")
        else:
            dialogo = Gtk.MessageDialog(
                parent=self,
                buttons=Gtk.ButtonsType.OK,
                text=boton.get_label()
                + "El estudinate ya se encuentra matriculado imposible matricularlo nuevamente",
            )
            # print("El estudinate ya se encuentra matriculado imposible matricularlo nuevamente")


class AppColegio(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventana = None

    def do_activate(self):
        if not self.ventana:
            self.ventana = VentanaPrincipal(
                title="__Colegio__", application=self
            )
        self.ventana.show_all()


if __name__ == "__main__":
    app = AppColegio(application_id="adt.lists.sll.colegio")
    sys.exit(app.run(sys.argv))
