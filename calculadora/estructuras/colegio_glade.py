import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from adt.lists.sll import SinglyLinkedList
from colegio import Estudiante
class signalHandLers():
    def __init__(self,builder):
        self.ent_cod=builder.get_object("ent_cod")
        self.ent_nom=builder.get_object("ent_nom")
        self.ent_nota=builder.get_object("ent_nota")
        self.cbx_cod=builder.get_object("cbx_cod")
        self.dlg_append=builder.get_object("dlg_append")
        self.dlg_serch=builder.get_object("dlg_serch")
        self.dlg_serch=builder.get_object("dlg_")


     def on_btn_ing_clicked(self, button):
         nuevo_estudiante=Estudiante(self.ent_cod.get_text(),self.ent_nom.get_text(),float(self.ent_nota.get_text()))
         if not self.estudiantes.serch(nuevo_estudaiante):
             if self.estudiantes.append(nuevo_estudiante):
                 self.dlg_append.set_property("text",
                                               "Estudiante adicionado OK")
               self.cbx_cod.append_text(nuevo_estudiante.cpdigo)

           else:
               self.dlg_append.set_property("text",
                                             "Estudiante ya adicionado ")
               self.dlg_append.run()
               self.dlg_append.hide()



    def on_btn_bus_clicked(self,button):
        cod_bus=self.cbx_cod,get_activate_text()
        if cod_bus is not None:
            el_estudiante=self.estudiantes.(serch(cod_bus))
            texto_info="El estudiante de cidigo{el_estudiante.codigo} llamado"
    def on_btn_reporte_clicked(self,button):
        pass
class AppColegio(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventana = None

    def do_activate(self):
        if not self.ventana:
            builder=Gtk.Builder()
            builder.add_from_file("ventana_estudiante.glade")
            self.ventana = builder.get_object("mainwindow")
            self.add_window(self.ventana)
            builder.connect_signals(signalHandLers())
        self.ventana.show_all()


if __name__ == "__main__":
    app = AppColegio(application_id="adt.lists.sll.colegio_glade")
    sys.exit(app.run(sys.argv))
