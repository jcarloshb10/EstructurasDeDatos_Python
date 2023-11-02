import sys
from PyQt5 import uic
from PyQt5 import*
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QListWidget, QLabel, QLineEdit, QFrame, QMessageBox
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from loteria import*
class Ventana(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1080,600)
        self.setWindowTitle("********LOTERIA*******")
        self.setStyleSheet("background-color: rgb(85, 0, 255)")
        self.loteria=Loteria(1000)
        self.poso=self.loteria.pozo()
        #self.setWindowIcon(QIcon('web.jpg'))
        self.initUI()
        
    def initUI(self):
        """metodo que inicializara todos los atributos de la interfaz como son los botones y los contenedores que se abriran
        al monemto de precionar dicho boton

        """     
        #________________________________ Botones principales _______________________________ 

        loteriaButton = QPushButton("Loteria",self)
        a=50
        loteriaButton.setGeometry(60,170+a,121,41)
        loteriaButton.setStyleSheet("background-color: rgb(255, 255, 127);"
        +"font: italic 11pt 'Arial'")
        loteriaButton.clicked.connect(self.muestraVenLot)
        
        premiosButton = QPushButton("Premios",self)
        premiosButton.setGeometry(60,220+a,121,41)
        premiosButton.setStyleSheet("background-color: rgb(255, 255, 127);"
        +"font: italic 11pt 'Arial'")
        premiosButton.clicked.connect(self.muestraVenPre)

        participantesButton = QPushButton("Participantes",self)
        participantesButton.setGeometry(60,270+a,121,41)
        participantesButton.setStyleSheet("background-color: rgb(255, 255, 127);"
        +"font: italic 11pt 'Arial'")
        participantesButton.clicked.connect(self.muestraVenPartici)
        # creacion de la lista que contendra a los premios
        self.listaPremios=QListWidget()
        self.listaPremios.setStyleSheet("background-color: rgb(170, 255, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        self.listaPart=QListWidget()
        self.listaPart.setStyleSheet("background-color: rgb(170, 255, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        b=50

        label1=QLabel("        Poso acumumulado",self)
        label1.setGeometry(850,10+b,191,31)
        
        esti="font: 12pt 'MS Sans Serif';background-color: rgb(255, 255, 255)"
        label1.setStyleSheet(esti)
        self.line1=QLineEdit(self)
        esti1="background-color: rgb(255, 255, 16);font: 12pt 'MS Shell Dlg 2'"
        self.line1.setGeometry(850,40+b,191,51)
        self.line1.setStyleSheet(esti1)
        self.line1.setText("$ "+str(self.loteria.pozo()))
        self.line1.setReadOnly(True)

        label2=QLabel("        recaudo de boletas",self)
        label2.setStyleSheet(esti)
        label2.setGeometry(850,130+b,191,31)
        self.line2=QLineEdit(self)
        self.line2.setGeometry(850,155+b,191,51)
        self.line2.setStyleSheet(esti1)
        self.line2.setText("$ "+str(self.loteria.precio_boleta*self.loteria.lista_concursantes.__len__()))
        self.line2.setReadOnly(True)
        label3=QLabel("Cantidad de concursantes",self)
        label3.setStyleSheet(esti)
        label3.setGeometry(850,230+b,191,31)
        self.line3=QLineEdit(self)
        self.line3.setGeometry(850,260+b,191,51)
        self.line3.setStyleSheet(esti1)
        self.line3.setText(str(self.loteria.lista_concursantes.__len__()))
        self.line3.setReadOnly(True)
        label4=QLabel("    Cantidad de premios",self)
        label4.setStyleSheet(esti)
        label4.setGeometry(850,340+b,191,31)
        self.line4=QLineEdit(self)
        self.line4.setGeometry(850,370+b,191,51)
        self.line4.setStyleSheet(esti1)
        self.line4.setText(str(self.loteria.lista_premios.__len__()))
        self.line4.setReadOnly(True)
        #__________________________________Contenedores__________________________________________________
        #ventana premios
        self.ventPremios=QFrame(self)
        self.ventPremios.setGeometry(210,20+a,570,401)
        self.ventPremios.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.agregarVentPremios()
        self.ventPremios.setVisible(False)
        #ventana participantes
        self.ventParticipantes=QFrame(self)
        self.ventParticipantes.setGeometry(210,20+a,570,401)
        self.ventParticipantes.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.agregarventParticipantes()
        self.ventParticipantes.setVisible(False)
        #ventana loteria
        self.ventLoteria=QFrame(self)
        self.ventLoteria.setGeometry(220,30,571,531)
        self.ventLoteria.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.agregar_ventana_lote()
        self.ventLoteria.setVisible(True)
        
    def muestraVenPre(self):
        self.listaPremios.setParent(self.ventPremios)
        self.listaPremios.setGeometry(290,10,271,380)
        self.ventPremios.setVisible(True)
        self.ventParticipantes.setVisible(False) 
        self.ventLoteria.setVisible(False)
        
    def muestraVenPartici(self):
        self.listaPart.setParent(self.ventParticipantes)
        self.listaPart.setGeometry(290,10,271,380)
        self.ventPremios.setVisible(False)
        self.ventParticipantes.setVisible(True)
        self.ventLoteria.setVisible(False)

    def muestraVenLot(self):
        self.listaPart.setParent(self.ventLoteria)
        self.listaPart.setGeometry(10,10,261,351)
        self.listaPremios.setParent(self.ventLoteria)
        self.listaPremios.setGeometry(290,10,271,351)
        self.ventLoteria.setVisible(True)
        self.ventPremios.setVisible(False)
        self.ventParticipantes.setVisible(False)





    #________________________________Funciones para la ventana Premios __________________________    
            
    def agregarVentPremios(self):
        # creacion de labels para premios
        self.listaPremios.setParent(self.ventPremios)
        self.listaPremios.setGeometry(290,10,271,380)

        labelNombre=QLabel("Nombre:",self.ventPremios)
        labelNombre.setGeometry(30,60,61,21)
        labelNombre.setStyleSheet("font: 12pt 'MS Sans Serif'")

        labelPrecio=QLabel("Precio:",self.ventPremios)
        labelPrecio.setGeometry(30,110,61,21)
        labelPrecio.setStyleSheet("font: 12pt 'MS Sans Serif'")

        self.lineNom=QLineEdit(self.ventPremios)
        self.lineNom.setGeometry(150,50,111,31)
        self.lineNom.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")

        self.linePreci=QLineEdit(self.ventPremios)
        self.linePreci.setGeometry(150,100,111,31)
        self.linePreci.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")

        btnGuardar=QPushButton("Agregar",self.ventPremios)
        btnGuardar.setGeometry(150,170,111,41)
        btnGuardar.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        btnGuardar.clicked.connect(self.agregarPremio)

        btnBorrar=QPushButton("Eliminar",self.ventPremios)
        btnBorrar.setGeometry(150,240,111,41)
        btnBorrar.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        btnBorrar.clicked.connect(self.borrarpremio)
        

    def agregarPremio(self):

        try:
            nom=self.lineNom.text()
            pre=float(self.linePreci.text())
            premio=Premio(nom,pre)
            msg=QMessageBox()
            msg.setWindowTitle("Agregacion de premios")
            if self.loteria.agregar_premio(premio):
                msg.setIcon(QMessageBox.Information)
                msg.setText("El premio: " +premio.__str__() +" se agrego"+ 
                "correctamente a lista de premios")
                self.poso=self.loteria.pozo()
                self.line1.setText("$ "+str(self.poso))
                self.line4.setText(str(self.loteria.lista_premios.__len__()))
            else:
                msg.setIcon(QMessageBox.Critical)
                msg.setText(" ERROR El premio: " +premio.__str__() +" no se agrego"+ 
                "correctamente a lista de premios")
            x=msg.exec_()    
        #self.listaPremios.addItem(premio.__str__())
            self.lineNom.setText("")
            self.linePreci.setText("")     
            self.pintar()
        except  :
            self.lineNom.setText("")
            self.linePreci.setText("")                 
                            
    def borrarpremio(self):
        try:
            nom=self.lineNom.text()
            pre=float(self.linePreci.text())
            premio1=Premio(nom,pre)
            msg=QMessageBox()
            msg.setWindowTitle("Borrar premios")
            msg.setIcon(QMessageBox.Question)
            msg.setText("Atencion se borrara todos los premios del tipo :"+
                        premio1.__str__())    
            x=msg.exec_()  
            msg1=QMessageBox()
            msg1.setWindowTitle("Borrar premios")                 
            if self.loteria.quitar_premios(premio1):
                msg1.setIcon(QMessageBox.Information)
                msg1.setText("se borro con Exito todo los premios"+
                            "del tipo : "+premio1.__str__())

                items = self.listaPremios.findItems(premio1.__str__(),Qt.MatchExactly) 
                if len(items) > 0: 
                    for item in items: 
                        q=self.listaPremios.row(item)
                        self.listaPremios.takeItem(q) 
                self.poso=self.loteria.pozo()
                self.line1.setText("$ "+str(self.poso))   
                self.line4.setText(str(self.loteria.lista_premios.__len__()))        
            else :
                msg1.setIcon(QMessageBox.Critical)
                msg1.setText("Atencion No se pudo borrar todos los premios"+
                        "del tipo : "+premio1.__str__())  
            x=msg1.exec_()
            self.lineNom.setText("")
            self.linePreci.setText("")
        except :
            self.lineNom.setText("")
            self.linePreci.setText("")   
#______________________________Fin funciones ventana Premios________________________________     




#_________________________ funciones para ventana Concursantes_________________________
    def agregarventParticipantes(self):
        self.listaPart.setParent(self.ventParticipantes)
        self.listaPart.setGeometry(290,10,271,380)
        labelNombre=QLabel("Nombre :",self.ventParticipantes)
        labelNombre.setGeometry(30,60,61,21)
        labelNombre.setStyleSheet("font: 12pt 'MS Sans Serif'")
        labelNombre1=QLabel("Precio Boleta :",self.ventParticipantes)
        labelNombre1.setGeometry(10,100,97,21)
        labelNombre1.setStyleSheet("font: 12pt 'MS Sans Serif'")
        lineNomPar1=QLineEdit(self.ventParticipantes)
        lineNomPar1.setGeometry(150,100,111,31)
        lineNomPar1.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")
        lineNomPar1.setText("$ "+str(self.loteria.precio_boleta))
        lineNomPar1.setReadOnly(True)
        self.lineNomPar=QLineEdit(self.ventParticipantes)
        self.lineNomPar.setGeometry(150,50,111,31)
        self.lineNomPar.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")
        btnGuardar=QPushButton("Agregar",self.ventParticipantes)
        btnGuardar.setGeometry(150,170,111,41)
        btnGuardar.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        btnGuardar.clicked.connect(self.guardarNombrePart)

    def guardarNombrePart(self):
        if not self.lineNomPar.text():
            self.lineNomPar.setText("") 
            
        else:
            nom=self.lineNomPar.text()
            parti=Concursante(nom)
            msg=QMessageBox()
            msg.setWindowTitle("Agregar Concursantes")  
            if self.loteria.agregar_concursante(parti):
                msg.setIcon(QMessageBox.Information)
                msg.setText("El concursante "+ parti.__repr__()+" se creo correctamente")
                self.line2.setText("$ "+str(self.loteria.precio_boleta*self.loteria.lista_concursantes.__len__()))
                self.line3.setText(str(self.loteria.lista_concursantes.__len__()))
                self.pintar()
            else:
                msg.setIcon(QMessageBox.Critical)
                msg.setText("El concursante "+ parti.__repr__()+" Ya existe")
            x=msg.exec_()
            self.lineNomPar.setText("") 
#______________________fin de funciones para ventana Concursantes_________________________     

#______________________funciones para ventana loteria______________________________________

    def agregar_ventana_lote(self):
        self.listaPart.setParent(self.ventLoteria)
        self.listaPart.setGeometry(10,10,261,351)
        self.listaPremios.setParent(self.ventLoteria)
        self.listaPremios.setGeometry(290,10,271,351)
        self.num_concursante=QLineEdit(self.ventLoteria)
        self.num_concursante.setGeometry(90,380,111,31)
        self.num_concursante.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")
        self.num_premio=QLineEdit(self.ventLoteria)
        self.num_premio.setGeometry(380,380,111,31)
        self.num_premio.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")
        label_numPar=QLabel("indice para el Concursante",self.ventLoteria)
        label_numPar.setGeometry(50,420,191,21)
        label_numPar.setStyleSheet("font: 12pt 'MS Sans Serif'")
        label_numPre=QLabel("indice para el premio",self.ventLoteria)
        label_numPre.setGeometry(360,420,191,21)
        label_numPre.setStyleSheet("font: 12pt 'MS Sans Serif'")
        btn_sortear=QPushButton("Sortear",self.ventLoteria)
        btn_sortear.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        btn_sortear.setGeometry(230,450,111,41)
        btn_sortear.clicked.connect(self.sorteo)

    def sorteo(self):
        try:
            numCon=int(self.num_concursante.text())
            numPre=int(self.num_premio.text())
            msg=QMessageBox()
            msg.setWindowTitle("****** Ganador Sorteo ********")  
            resultado=self.loteria.sortear(numCon,numPre)
            res=str(resultado)
            if resultado[0] is not None :
                msg.setIcon(QMessageBox.Information)
                msg.setText("FELICITACIONES :" +str(resultado[0])+
                " Acabas de ganar un espectacular : "+str(resultado[1]))
                self.poso=self.loteria.pozo()
                self.line1.setText("$ "+str(self.poso))
                self.line2.setText("$ "+str(self.loteria.precio_boleta*self.loteria.lista_concursantes.__len__()))
                self.line3.setText(str(self.loteria.lista_concursantes.__len__()))
                self.line4.setText(str(self.loteria.lista_premios.__len__()))
                self.pintar()

            else:
                msg.setIcon(QMessageBox.Critical)
                msg.setText("No se cumplen las condiciones necesarias para sortear ")
            x=msg.exec_()
            self.num_concursante.setText("")
            self.num_premio.setText("")
        except:
            self.num_concursante.setText("")
            self.num_premio.setText("")            
#______________________fin funciones para ventana loteria_____________________________
    def pintar(self):
        self.listaPart.clear()
        self.listaPremios.clear()
        lista=[]
        listaconcu=[]
        for i in self.loteria.lista_premios:
            lista.append(i.dato.__str__())
        for i in self.loteria.lista_concursantes:
            listaconcu.append(i.dato.__str__())
        self.listaPart.addItems(listaconcu)   
        self.listaPremios.addItems(lista) 

if __name__ == "__main__":
    app=QApplication([])
    window=Ventana()
    window.show()
    app.exec_()    
    