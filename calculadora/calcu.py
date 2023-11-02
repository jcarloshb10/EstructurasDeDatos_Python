from adt.stack_queue.queue import Queue
from adt.stack_queue.notation  import Prefix
from adt.lists.sll import SinglyLinkedList

import os
import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SignalHandlers():

    def __init__(self,builder):
        #cargamos los diferentes widgets a utilizar
        self.ent_num = builder.get_object("ent_num")
        self.c=False
        self.cola = Queue()



    def __str__(self):
        cad_new += (self.cola.__str__())
        return cad_new


    def cliken_c(self,button):

        self.cola.__init__()
        self.ent_num.set_text(self.cola.__str__())

    def cliken_1(self,button):
        self.cola.enqueue(1)
        self.ent_num.set_text(self.cola.__str__())
    def cliken_2(self,button):

        self.cola.enqueue(2)
        self.ent_num.set_text(self.cola.__str__())
    def cliken_3(self,button):

        self.cola.enqueue(3)
        self.ent_num.set_text(self.cola.__str__())
    def cliken_4(self,button):

        self.cola.enqueue(4)
        self.ent_num.set_text(self.cola.__str__())
    def cliken_5(self,button):

        self.cola.enqueue(5)
        self.ent_num.set_text(self.cola.__str__())
    def cliken_6(self,button):

        self.cola.enqueue(6)
        self.ent_num.set_text(self.cola.__str__())
    def cliken_7(self,button):

        self.cola.enqueue(7)
        self.ent_num.set_text(self.cola.__str__())
    def cliken_8(self,button):

        self.cola.enqueue(8)
        self.ent_num.set_text(self.cola.__str__())
    def cliken_9(self,button):

        self.cola.enqueue(9)
        self.ent_num.set_text(self.cola.__str__())
    def cliken_0(self,button):

        self.cola.enqueue(0)
        self.ent_num.set_text(self.cola.__str__())
    def cliken_d(self,button):

        self.cola.enqueue("/")
        self.ent_num.set_text(self.cola.__str__())
    def cliken_p(self,button):

        self.cola.enqueue("*")
        self.ent_num.set_text(self.cola.__str__())
    def cliken_s(self,button):

        self.cola.enqueue("+")
        self.ent_num.set_text(self.cola.__str__())

    def cliken_i(self,button):
        self.ent_num.set_text("=")
        self.calcular = Prefix(self.cola.__str__())
        self.calcular.prefix()
        str(self.arithmetic_expression_evaluation())

    def cliken_a(self,button):

        self.cola.enqueue("^")
        self.ent_num.set_text(self.cola.__str__())
    def cliken_e(self,button):

        self.cola.enqueue(" ")
        self.ent_num.set_text(self.cola.__str__())
    def cliken_par(self,button):

        self.cola.enqueue("( ")
        self.ent_num.set_text(self.cola.__str__())
    def cliken_pard(self,button):

        self.cola.enqueue(")")
        self.ent_num.set_text(self.cola.__str__())
    def cliken_r(self,button):

        self.cola.enqueue("-")
        self.ent_num.set_text(self.cola.__str__())









class Appcalculadora(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventana = None

    def do_activate(self):
        if not self.ventana:
            builder=Gtk.Builder()
            builder.add_from_file("calculadora.glade")
            self.ventana = builder.get_object("window")
            self.add_window(self.ventana)
            builder.connect_signals(SignalHandlers(builder))
        self.ventana.show_all()


if __name__ == "__main__":
    app = Appcalculadora(application_id="calcu")
    sys.exit(app.run(sys.argv))
