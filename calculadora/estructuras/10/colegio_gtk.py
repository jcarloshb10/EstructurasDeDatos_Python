import sys
import gi
from adt.lists.sll  import SinglyLinkedList
from colegio    import Estudiante
gi.require_version('Gtk', '3.0')
from gi.repository  import Gtk


class VentanaPrincipal(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box_main)
        # ***frame para insertar estudiantes***
        self.__construir_ingreso(box_main)

        # Creacion de la lista de estudiantes del Colegio
        self.estudiantes = SinglyLinkedList()
        self.__construir_presentación(box_main)


    def __construir_ingreso(self, box_main):
        frm_ing = Gtk.Frame(label="Ingreso de Estudiantes",
                            margin_left=5, margin_right=5)
        box_main.add(frm_ing)
        grid_ing = Gtk.Grid(column_homogeneous=True, column_spacing=10)
        lbl_cod = Gtk.Label(label="Codigo:")
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
        grid_ing.attach(child=btn_ing, left=1, top=2, width=1, height=1)
        frm_ing.add(grid_ing)
    def __construir_presentación(self,box_main):
        frm_pres = Gtk.Frame(label="Listado de Estudiantes",
                            margin_left=5, margin_right=5)
        box_main.add(frm_pres)
        box_ver = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        btn_reporte = Gtk.Button(label="Reporte de estudiantes")
        btn_reporte.connect("clicked", self.on_btn_reporte_clicked)
        box_ver.add(btn_reporte)
        self.txbf_reporte = Gtk.TextBuffer()
        txv_reporte = Gtk.TextView(buffer=self.txbf_reporte)
        box_ver.add(txv_reporte)


        frm_pres.add(box_ver)
    def on_btn_ing_clicked(self, btn_ing):

        un_estudiante = Estudiante(self.ent_cod.get_text(),
                                   self.ent_nom.get_text(),
                                   float(self.ent_nota.get_text()))
        if not self.estudiantes.search(un_estudiante):
            if self.estudiantes.append(un_estudiante):
                dialog=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text="Estudiante Adicionado Exitosamente!",title="Atencion")
            else:
                dialog=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text="Estudiante NO pudo adicionarse!",title="Error")
        else:
            dialog=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text="Estudiante ya esta matriculado",title="Error")
        dialog.run()
        dialog.destroy()
    def on_btn_reporte_clicked(self, btn_reporte):
        cad = "CODIGO         NOMBRE        NOTA\n"
        cad += str(self.estudiantes)
        self.txbf_reporte.set_text(cad)


class AppColegio(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventana = None

    def do_activate(self):
        if not self.ventana:
            self.ventana = VentanaPrincipal(title="__ Colegio __", application = self)
        self.ventana.show_all()

if __name__== "__main__":
    app = AppColegio()
    sys.exit(app.run(sys.argv))
