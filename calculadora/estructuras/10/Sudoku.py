#!/usr/lib/python3 import sys print("Version ",sys.version)

import gi
gi.require_version ('Gtk', '3.0')
from gi.repository import Gtk
print("Ventana")
ventana=Gtk.ApplicationWindow(title="Mi Ventana")
ventana.connect("delete-event", Gtk.main_quit)
malla=Gtk.Grid(row_homogeneous=True, column_homogeneous=True)


boton1=Gtk.Button(label="oooo")
#boton1.connect('clicked', met_boton1)
boton2=Gtk.Button(label="lloooo")
malla.attach(child=boton1, left=0, top=0, width=1, height=1)
malla.attach(child=boton2, left=0, top=1, width=2, height=1)



ventana.add(malla)
ventana.show_all();


Gtk.main()
