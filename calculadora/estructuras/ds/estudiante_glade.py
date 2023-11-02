import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from adt.lists.sll import SinglyLinkedList
from estudiante import Estudiante

class SignalHandlers():#maneja eventos de las señales
    def __init__(self,builder):
        #cargo los objetos de entrada de datos del Estudiantes
        self.ent_cod = builder.get_object("ent_cod")
        self.ent_nom = builder.get_object("ent_nom")
        self.ent_nota = builder.get_object("ent_nota")
        #cargo el combo de bùsqueda de estudiantes por codigo
        self.cbx_cod = builder.get_object ("cbx_cod")
        #cargo el objeto buffer de presentacion
        self.buff_reporte = builder.get_object("buff_reporte")
        #
        self.dlg_append = builder.get_object("dlg_append")
        self.dlg_search = builder.get_object("dlg_search")
        #inicializo la lista de estudiantes
        self.estudiantes = SinglyLinkedList()

    def on_btn_ing_clicked(self,button):
        nuevo_estudiante = Estudiante(self.ent_cod.get_text(),
                                      self.ent_nom.get_text(),
                                      float(self.ent_nota.get_text()))

        if not self.estudiantes.search(nuevo_estudiante):
            if self.estudiantes.append(nuevo_estudiante):
                self.dlg_append.set_property("text","Estudiante agregado OK!")
                self.dlg_append.format_secondary_text(
                "Codigo: "+nuevo_estudiante.codigo+
                "\nNombre: "+nuevo_estudiante.nombre+
                "\nNota: "+self.ent_nota.get_text() )
            #Adicionamos el codigo al GtkComboBoxText
            self.cbx_cod.append_text(nuevo_estudiante.codigo)
        else:
            self.dlg_append.set_property("text","Estudiante YA EXISTE NO fue adicionado")
            self.dlg_append.format_secondary_text("")
        self.dlg_append.run()
        self.dlg_append.hide()


    def on_btn_bus_clicked(self,button):
        #obtenemos el codigo del estudiante a buscar del GtkComboBoxText
        cod_est = self.cbx_cod.get_active_text()
        if cod_est is not None:
            el_est = self.estudiantes.search(Estudiante(cod_est))
            if el_est is not None:#dificil que ocurra
                info_est = (f"El estudiante de còdigo{el_est.codigo}"+
                             f"llamado{el_est.nombre}tiene una nota de")

    def on_btn_rep_clicked(self,button):
        pass

class AppPrincipal(Gtk.Application):  # heredando
    def __init__(self, *args, **kwargs):  # (**diccionario, *Tupla)
        super().__init__(*args, **kwargs)
        self.ventana = None

    def do_activate(self):
        if not self.ventana:
            builder = Gtk.Builder()
            builder.add_from_file("ventana_estudiantes.glade")
            self.ventana = builder.get_object("main_window")#vincular ventana
            self.add_window(self.ventana)
            builder.connect_signals(SignalHandlers(builder))
        self.ventana.show_all()

if __name__  ==  "__main__":
    app = AppPrincipal(application_id = "adt.lists.sll.colegio_glade")
    sys.exit(app.run(sys.argv))
