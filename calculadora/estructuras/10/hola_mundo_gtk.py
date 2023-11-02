import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class VentanaHM(Gtk.ApplicationWindow):
    def __init__(self,*args,**kwargs):
        super(VentanaHM, self).__init__(*args, **kwargs)
        boton=Gtk.Button(label="Hola")
        boton.connect("clicked",self.on_boton_clicked)
        self.set_default_size(200,200)
        self.add(boton)


    def on_boton_clicked(self,boton):
        #print(boton.get_label(), "Hola mundo")
        dialogo=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text=boton.get_label()+" Mundo",secondary_text="Bienvenidos",title="Mensaje Hola mundo")

        dialogo.run()
        dialogo.destroy()



class AppHM(Gtk.Application):
    def __init__(self,*args,**kwargs):
        super(AppHM, self).__init__(*args, **kwargs)
        self.win=None

    def do_activate(self):
        if not self.win:
            self.win=VentanaHM(title="Titulo ventana",application=self)
        self.win.show_all()


if __name__ == '__main__':
    app=AppHM()
    sys.exit(app.run(sys.argv))
