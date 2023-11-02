import sys
import gi
from adt.lists.dll  import DoublyLinkedList
from cancion import Cancion
gi.require_version('Gtk', '3.0')
from gi.repository  import Gtk

class PlayList(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box_main)
        self.canciones = DoublyLinkedList()
        cancion1=Cancion("can","art",3)
        cancion2=Cancion(2,3,4)
        self.canciones.append(cancion1)
        self.canciones.append(cancion2)
        self.__nuevas_canciones(box_main)
        self.__eliminar_cancion(box_main)
        self.__recorrer_canciones(box_main)

    def __nuevas_canciones(self, box_main):
        frame1 = Gtk.Frame(label="Nuevas Canciones",
                            margin_left=5, margin_right=5)
        box_main.add(frame1)

    def __eliminar_cancion(self, box_main):
        frame2 = Gtk.Frame(label="Eliminar una Canción",
                            margin_left=5, margin_right=5)
        box_main.add(frame2)
        grid2 = Gtk.Grid(column_homogeneous=True, column_spacing=10)
        self.ent_artist_pos = Gtk.Entry()
        self.ent_title = Gtk.Entry()
        grid2.attach(child=self.ent_artist_pos,left=0, top=1, width=1, height=1)
        grid2.attach(child=self.ent_title,left=1, top=1, width=1, height=1)
        btn_elim = Gtk.Button(label="Eliminar")
        btn_elim.connect("clicked",self.on_btn_elim_clicked)
        grid2.attach(child=btn_elim,left=2, top=1, width=1, height=1)
        frame2.add(grid2)


    def __recorrer_canciones(self, box_main):
        frame3 = Gtk.Frame(label="Recorrer Canciones",
                            margin_left=5, margin_right=5)
        box_main.add(frame3)

    def on_btn_elim_clicked(self,btn_elim):
        try:
            if self.canciones.delete(self.canciones.locate(int(self.ent_artist_pos.get_text()))):
                dialog=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text="La Cancion en la posicion "+self.ent_artist_pos.get_text()+" se elimino de forma satisfactoria",title="Eliminar...")
            else:
                dialog=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text="La Cancion en la posicion "+self.ent_artist_pos.get_text()+" NO existe",title="Atencion")
            dialog.run()
            dialog.destroy()
        except ValueError:
            while True:
                if self.ent_title.get_text() == "":
                    dialog=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text="Ingresar titulo",title="Eliminar...")
                    dialog.run()
                    dialog.destroy()
                elif self.ent_artist_pos.get_text() == "":
                    dialog=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text="Ingresar Artista",title="Eliminar...")
                    dialog.run()
                    dialog.destroy()
                else:
                    break

            if len(self.canciones) != 0:
                for can in self.canciones:
                    if can.titulo == self.ent_title.get_text() and can.titulo == self.ent_artist_pos:
                        if self.canciones.delete(can):
                            dialog=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text="La Cancion "+self.ent_title.get_text()+" del artista "+ self.ent_artist_pos+ " se eliminó de forma satisfactoria",title="Eliminar...")
                        else:
                            dialog=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text="La Cancion "+self.ent_title.get_text()+" del artista "+ self.ent_artist_pos+ " NO se encuentra",title="Eliminar...")
                        break

                dialog=Gtk.MessageDialog(parent=self,buttons=Gtk.ButtonsType.OK,text="La Cancion "+self.ent_title.get_text()+" del artista "+ self.ent_artist_pos.get_text()+ " No se encuentra",title="Eliminar...")

                dialog.run()
                dialog.destroy()









class AppPlayList(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventana = None

    def do_activate(self):
        if not self.ventana:
            self.ventana = PlayList(title="***** Play List *****", application = self)
        self.ventana.show_all()

if __name__== "__main__":
    app = AppPlayList()
    sys.exit(app.run(sys.argv))
