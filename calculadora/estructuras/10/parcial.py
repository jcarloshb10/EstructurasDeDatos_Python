import os, sys
import gi
from cancion import Cancion
###########from adt.lists.sll  import SinglyLinkedList
from adt.lists.dll  import DoublyLinkedList

gi.require_version('Gtk', '3.0')
from gi.repository  import Gtk


class PlayList(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box_main)

        #Metodos De interfaz
        self.__construir_nueva_cancion(box_main)
        self.__eliminar_cancion(box_main)
        self.__recorrer_canciones(box_main)
        self.__mostrar_canciones(box_main)

        lol=Cancion("adsfs","fsdaf","23")
        lol2=Cancion("aaaaa","frrrrr","43")
        lol3=Cancion("werre","wfd","43")
        lol4=Cancion("bbbb","w111111111w","43")
        lol5=Cancion("prrrrr","54354343","43")
        self.canciones = DoublyLinkedList()
        self.canciones.append(lol)
        self.canciones.append(lol2)
        self.canciones.append(lol3)
        self.canciones.append(lol4)
        self.canciones.append(lol5)





        #Metodos De interfaz
    def __construir_nueva_cancion(self, box_main):
        frm_ing = Gtk.Frame(label="Nuevas Canciones",
                            margin_left=5, margin_right=5)

        box_main.add(frm_ing)
        grid_ing = Gtk.Grid(column_homogeneous=True, column_spacing=10)

        lbl_art = Gtk.Label(label="Artista:")
        lbl_tit = Gtk.Label(label="Titulo:")
        lbl_dur = Gtk.Label(label="Duracion")
        lbl_pos = Gtk.Label(label="Pocicion:")

        self.ent_art = Gtk.Entry()
        self.ent_tit = Gtk.Entry()
        self.ent_dur = Gtk.Entry()
        self.ent_pos = Gtk.Entry()


        btn_adc = Gtk.Button(label="Adicionar Cancion")

        grid_ing.attach(child=lbl_art, left=0, top=0, width=1, height=1)
        grid_ing.attach(child=lbl_tit, left=1, top=0, width=1, height=1)
        grid_ing.attach(child=lbl_dur, left=0, top=2, width=1, height=1)
        grid_ing.attach(child=lbl_pos, left=1, top=3, width=1, height=1)

        grid_ing.attach(child=self.ent_art, left=0, top=1, width=1, height=1)
        grid_ing.attach(child=self.ent_tit, left=1, top=1, width=1, height=1)
        grid_ing.attach(child=self.ent_dur, left=0, top=3, width=1, height=1)
        grid_ing.attach(child=self.ent_pos, left=1, top=4, width=1, height=1)



        btn_adc.connect("clicked", self.event_adcionar_canciones)
        grid_ing.attach(child=btn_adc, left=0, top=4, width=1, height=1)
        frm_ing.add(grid_ing)
    def __recorrer_canciones(self, box_main):
            frm_ing = Gtk.Frame(label="recorr Canciones",
                                margin_left=5, margin_right=5)

            box_main.add(frm_ing)
            grid_ing = Gtk.Grid(column_homogeneous=True, column_spacing=10)

            lbl_artrc = Gtk.Label(label="Artista:")
            lbl_titrc = Gtk.Label(label="Titulo:")
            lbl_durrc = Gtk.Label(label="Duracion")


            self.ent_artrc = Gtk.Entry()
            self.ent_titrc = Gtk.Entry()
            self.ent_durrc = Gtk.Entry()



            btn_ant = Gtk.Button(label="Anterior")
            btn_sig = Gtk.Button(label="Siguiente")

            grid_ing.attach(child=lbl_artrc, left=0, top=0, width=1, height=1)
            grid_ing.attach(child=lbl_titrc, left=1, top=0, width=1, height=1)
            grid_ing.attach(child=lbl_durrc, left=2, top=0, width=1, height=1)


            grid_ing.attach(child=self.ent_artrc, left=0, top=1, width=1, height=1)
            grid_ing.attach(child=self.ent_titrc, left=1, top=1, width=1, height=1)
            grid_ing.attach(child=self.ent_durrc, left=2, top=1, width=1, height=1)



            #btn_adc.connect("clicked", self.event_adcionar_canciones)
            grid_ing.attach(child=btn_ant, left=0, top=2, width=1, height=1)
            grid_ing.attach(child=btn_sig, left=2, top=2, width=1, height=1)
            frm_ing.add(grid_ing)

            btn_ant.connect("clicked", self.event_anterior)
            btn_sig.connect("clicked", self.event_siguiente)
    def __mostrar_canciones(self,box_main):

        grid_1 = Gtk.Grid(column_homogeneous=True, column_spacing=10)
        box_ver = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)

        btn_right_playlist = Gtk.Button(label=">>>playlist")
        btn_left_playlist = Gtk.Button(label="<<<playlist")




        self.txbf_reporte = Gtk.TextBuffer()
        txv_reporte = Gtk.TextView(buffer=self.txbf_reporte)


        grid_1.attach(child=btn_left_playlist, left=0, top=0, width=1, height=1)
        grid_1.attach(child=btn_right_playlist, left=3, top=0, width=1, height=1)
        #grid_1.attach(child=txv_reporte, left=0, top=1, width=3, height=4)

        btn_right_playlist.connect("clicked", self.event_rplay)
        btn_left_playlist.connect("clicked", self.event_lplay)

        box_ver.add(grid_1)
        box_ver.add(txv_reporte)
        box_main.add(box_ver)
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




        #Metodos De Funcionalidad
    def event_adcionar_canciones(self, btn_ing):
        pass




    def event_anterior(self, btn_ing):
        pass
    def event_siguiente(self, btn_ing):
        pass
    def on_btn_elim_clicked(self, btn_ing):
        pass



    def event_lplay(self, btn_ing):
        cad = "[NUMERO DE CANCIONES:"+str(self.canciones.__len__())+"]\n"
        cad +="""
ARTISTA                                               TITULO                                                      Duracion
--------------------------------------------------------------------------------------------------------------------------------------
0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
--------------------------------------------------------------------------------------------------------------------------------------
"""

        for value in self.canciones:
            tit=str(value.titulo).center(50," ")
            art=str(value.artista).center(50," ")
            dur=str(value.duracion).center(50," ")

            cad+=tit+art+dur+"\n"
            #cad+=str(value)+"\n"
        self.txbf_reporte.set_text(cad)



    def event_rplay(self, btn_ing):
                cad = "[NUMERO DE CANCIONES:"+str(self.canciones.__len__())+"]\n"
                cad +="""
ARTISTA                                               TITULO                                                      Duracion
--------------------------------------------------------------------------------------------------------------------------------------
0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
--------------------------------------------------------------------------------------------------------------------------------------
"""
                
                for value in self.canciones.__len__():
                    tit=str(value.titulo).center(50," ")
                    art=str(value.artista).center(50," ")
                    dur=str(value.duracion).center(50," ")

                    cad+=tit+art+dur+"\n"
                    #cad+=str(value)+"\n"

                self.txbf_reporte.set_text(cad)











class AppPlayList(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventana = None

    def do_activate(self):
        if not self.ventana:
            self.ventana = PlayList(title="***Play List***", application = self)
        self.ventana.show_all()

if __name__== "__main__":
    app = AppPlayList()
    sys.exit(app.run(sys.argv))
