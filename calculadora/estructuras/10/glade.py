import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class signalHandLers():
    def __init__(self,builder):
        self.lbl_color= builder.get_object("lbl_color")

    def on_btn_color_clicked(self, button):
        color= button.get_label()

        self.lbl_color.set_text(f"El color favorito es el {color} ")

"""
        self.lbl_color.set_text(f"El color favorito es el {color}")


        self.lbl_color.set_text(f"El color favorito es el {color}")"""





class AppColegio(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventana = None

    def do_activate(self):
        if not self.ventana:
            builder=Gtk.Builder()
            builder.add_from_file("botones.glade")
            self.ventana = builder.get_object("main_window")
            self.add_window(self.ventana)
            builder.connect_signals(signalHandLers(builder))
        self.ventana.show_all()


if __name__ == "__main__":
    app = AppColegio(application_id="adt.lists.sll.colegio_glade")
    sys.exit(app.run(sys.argv))
