#!/usr/bin/env python
import sys
from PyQt5 import uic
from PyQt5 import*
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QListWidget, QLabel, QLineEdit, QFrame, QMessageBox
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from loteria import*
class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()
        #tamaño de la Ventana
        self.setGeometry(0,0,700,800)
        #titulo de la Ventana
        self.setWindowTitle("LOTERIA")
        #color y diseño de la Ventana
        self.setStyleSheet("background-color: rgb(192, 57, 43)")   
        #define la boleta en un precio de 200 pesos
        self.loteria=Loteria(2000)
        #self.pozoLoteria toma el valor en suma total de los premios
        self.pozoLoteria = self.loteria.pozo()
        #self.setWindowIcon(QIcon('web.jpg'))
        #metodo que inicializa los atributos de la interfaz
        self.initUI()

        
    def initUI(self):
            
        loteriaButton = QPushButton("Jugar loteria",self)
        loteriaButton.setGeometry(150,50,100,45)
        loteriaButton.setStyleSheet("background-color: rgb(255, 255, 127);"
        +"font: italic 11pt 'Arial'")
        loteriaButton.clicked.connect(self.muestraVentanaLoteria)
        
        premiosButton = QPushButton("Premios",self)
        premiosButton.setGeometry(300,50,100,45)
        premiosButton.setStyleSheet("background-color: rgb(255, 255, 127);"
        +"font: italic 11pt 'Arial'")
        premiosButton.clicked.connect(self.muestraVentanaPremios)

        concursantesButton = QPushButton("Concursantes",self)
        concursantesButton.setGeometry(450,50,100,45)
        concursantesButton.setStyleSheet("background-color: rgb(255, 255, 127);"
        +"font: italic 11pt 'Arial'")
        concursantesButton.clicked.connect(self.muestraVentanaConcursantes)

        #creacion de las listas
        self.listaDePremios=QListWidget()
        self.listaDePremios.setStyleSheet("background-color: rgb(170, 255, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        self.listaDeConcursantes=QListWidget()
        self.listaDeConcursantes.setStyleSheet("background-color: rgb(170, 255, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        
        label1=QLabel("\tPozo",self)
        label1.setGeometry(450,450,190,30)     
        esti="font: 12pt 'MS Sans Serif';background-color: rgb(255, 255, 255)"
        label1.setStyleSheet(esti)
        label1.setAlignment(Qt.AlignCenter)
        
        self.line1=QLineEdit(self)
        esti1="background-color: rgb(255, 255, 16);font: 12pt 'MS Shell Dlg 2'" 
        self.line1.setGeometry(450,480,190,50)
        self.line1.setStyleSheet(esti1)
        self.line1.setText("$ "+str(self.loteria.pozo()))
        self.line1.setAlignment(Qt.AlignCenter)
        self.line1.setReadOnly(True)

        label2=QLabel("Total en boletas vendidas",self)
        label2.setStyleSheet(esti)
        label2.setAlignment(Qt.AlignCenter)
        label2.setGeometry(450,130,190,30)
        
        self.line2=QLineEdit(self)
        self.line2.setGeometry(450,155,190,50)
        self.line2.setStyleSheet(esti1)
        self.line2.setText("$ "+str(self.loteria.precio_boleta*self.loteria.lista_concursantes.__len__()))
        self.line2.setAlignment(Qt.AlignCenter)
        self.line2.setReadOnly(True)
        
        label3=QLabel("Número de Concursantes",self)
        label3.setStyleSheet(esti)
        label3.setAlignment(Qt.AlignCenter) 
        label3.setGeometry(450,230,190,30)
        
        self.line3=QLineEdit(self)
        self.line3.setGeometry(450,260,190,50)
        self.line3.setStyleSheet(esti1)
        self.line3.setText(str(self.loteria.lista_concursantes.__len__()))
        self.line3.setAlignment(Qt.AlignCenter)
        self.line3.setReadOnly(True)
        
        label4=QLabel("Número de premios",self)
        label4.setStyleSheet(esti)
        label4.setAlignment(Qt.AlignCenter)   
        label4.setGeometry(450,340,190,30)
        
        self.line4=QLineEdit(self)
        self.line4.setGeometry(450,370,190,50)
        self.line4.setStyleSheet(esti1)
        self.line4.setText(str(self.loteria.lista_premios.__len__()))
        self.line4.setAlignment(Qt.AlignCenter)
        self.line4.setReadOnly(True)

        self.frameSTR=QFrame(self)
        self.frameSTR.setGeometry(50,600,570,150)
        self.frameSTR.setStyleSheet("background-color: rgb(255, 255, 255)") 
        
        self.lineSTR=QLabel(self.frameSTR)
        diseño="background-color: rgb(255, 255, 16);font: 12pt 'MS Shell Dlg 2'"  
        self.lineSTR.setGeometry(10,10,550,130)
        self.lineSTR.setStyleSheet(diseño)
        self.lineSTR.setText(str(self.loteria.__str__()))
        self.lineSTR.setAlignment(Qt.AlignCenter)
        
        self.ventanaPremios=QFrame(self)
        self.ventanaPremios.setGeometry(50,120,340,450)
        self.ventanaPremios.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.agregarVentanaDePremios()
        self.ventanaPremios.setVisible(False)

        self.ventanaConcursantes=QFrame(self)
        self.ventanaConcursantes.setGeometry(50,120,340,450)
        self.ventanaConcursantes.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.agregarventanaConcursantes()
        self.ventanaConcursantes.setVisible(False)

        self.ventanaLoteria=QFrame(self)
        self.ventanaLoteria.setGeometry(50,120,340,420)
        self.ventanaLoteria.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.agregar_ventana_loteria()
        self.ventanaLoteria.setVisible(True)


    def muestraVentanaPremios(self):
        self.listaDePremios.setParent(self.ventanaPremios)
        self.listaDePremios.setGeometry(20,250,300,150)
        self.ventanaPremios.setVisible(True)
        self.ventanaConcursantes.setVisible(False) 
        self.ventanaLoteria.setVisible(False)
        
    def muestraVentanaConcursantes(self):
        self.listaDeConcursantes.setParent(self.ventanaConcursantes)
        self.listaDeConcursantes.setGeometry(20,250,300,150)
        self.ventanaPremios.setVisible(False)
        self.ventanaConcursantes.setVisible(True)
        self.ventanaLoteria.setVisible(False)

    def muestraVentanaLoteria(self):
        self.listaDeConcursantes.setParent(self.ventanaLoteria)
        self.listaDeConcursantes.setGeometry(20,170,300,40)
        self.listaDePremios.setParent(self.ventanaLoteria)
        self.listaDePremios.setGeometry(20,260,300,40)
        self.ventanaLoteria.setVisible(True)
        self.ventanaPremios.setVisible(False)
        self.ventanaConcursantes.setVisible(False)
 
       
    def agregarVentanaDePremios(self):
        # creacion de labels para premios
        self.listaDePremios.setParent(self.ventanaPremios)
        self.listaDePremios.setGeometry(20,250,300,150)

        labelNombre=QLabel("Nombre:",self.ventanaPremios)
        labelNombre.setGeometry(40,60,70,20)
        labelNombre.setStyleSheet("font: 12pt 'MS Sans Serif'")

        labelPrecio=QLabel("Precio:",self.ventanaPremios)
        labelPrecio.setGeometry(40,110,70,20)
        labelPrecio.setStyleSheet("font: 12pt 'MS Sans Serif'")

        self.lineNom=QLineEdit(self.ventanaPremios)
        self.lineNom.setGeometry(150,50,145,30)
        self.lineNom.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")

        self.linePreci=QLineEdit(self.ventanaPremios)
        self.linePreci.setGeometry(150,100,145,30)
        self.linePreci.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")

        btnAgregar=QPushButton("Agregar",self.ventanaPremios)
        btnAgregar.setGeometry(40,170,116,40)
        btnAgregar.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        btnAgregar.clicked.connect(self.agregarPremio)

        btnBorrar=QPushButton("Eliminar",self.ventanaPremios)
        btnBorrar.setGeometry(183,170,116,40)
        btnBorrar.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        btnBorrar.clicked.connect(self.borrarpremio)
        

    def agregarPremio(self):      
        try:
            nom=self.lineNom.text()
            pre=float(self.linePreci.text())
            premio=Premio(nom,pre)
            msg=QMessageBox()
            msg.setWindowTitle("VERIFICACIÓN")
            if self.loteria.agregar_premio(premio):
                msg.setIcon(QMessageBox.Information)
                msg.setText("El premio: " +premio.__str__() +" se agrego" + 
                " correctamente a lista de premios")
                self.pozoLoteria=self.loteria.pozo()
                self.line1.setText("$ "+str(self.pozoLoteria))
                self.line4.setText(str(self.loteria.lista_premios.__len__()))
            else:
                msg.setIcon(QMessageBox.Critical)
                msg.setText(" ERROR El premio: " +premio.__str__() +" no se agrego"+ 
                " correctamente a lista de premios")
            x=msg.exec_()    
            self.lineNom.setText("")
            self.linePreci.setText("")     
            self.pintar_premios()
        except  :
            self.lineNom.setText("")
            self.linePreci.setText("") 
        self.lineSTR.setText(str(self.loteria.__str__()))


    def borrarpremio(self):
        try:
            nom=self.lineNom.text()
            pre=float(self.linePreci.text())
            premio1=Premio(nom,pre)
            msg=QMessageBox()
            msg.setWindowTitle("VERIFICACIÓN")
            msg.setIcon(QMessageBox.Question)
            msg.setText("Atención!\nSe borraran todos los premios del tipo: " +
                        premio1.__str__())    
            x=msg.exec_()  
            msg1=QMessageBox()
            msg1.setWindowTitle("CONFIRMACIÓN")                 
            if self.loteria.quitar_premios(premio1):
                msg1.setIcon(QMessageBox.Information)
                msg1.setText("ELIMINACIÓN EXITOSA DE " +
                            premio1.__str__())
                x1=msg1.exec_()
                items = self.listaDePremios.findItems(premio1.__str__(),Qt.MatchExactly) 
                if len(items) > 0: 
                    for item in items: 
                        q=self.listaDePremios.row(item)
                        self.listaDePremios.takeItem(q) 
                self.pozoLoteria=self.loteria.pozo()
                self.line1.setText("$ "+str(self.pozoLoteria))   
                self.line4.setText(str(self.loteria.lista_premios.__len__()))        
            else :
                print("raro")
                msg2=QMessageBox()
                #msg2.setIcon(QMessageBox.Critical)
                #msg2.setText("ERROR! NO SE ELIMINÓ " +
                        #premio1.__str__())  
                x2=msg2.exec_()
            self.lineNom.setText("")
            self.linePreci.setText("")
        except :
            self.lineNom.setText("")
            self.linePreci.setText("")

        self.lineSTR.setText(str(self.loteria.__str__()))
        self.pintar_premios()
        self.pintar_concursantes()

 
    def agregarventanaConcursantes(self):
        self.listaDeConcursantes.setParent(self.ventanaConcursantes)
        self.listaDeConcursantes.setGeometry(20,250,300,150)

        labelNombre=QLabel("Nombre:",self.ventanaConcursantes)
        labelNombre.setGeometry(40,60,70,20)
        labelNombre.setStyleSheet("font: 12pt 'MS Sans Serif'")
        labelNombre1=QLabel("Precio Boleta:",self.ventanaConcursantes)
        labelNombre1.setGeometry(40,110,120,20)
        labelNombre1.setStyleSheet("font: 12pt 'MS Sans Serif'")

        lineNomPar1=QLineEdit(self.ventanaConcursantes)
        lineNomPar1.setGeometry(175,100, 120,30)
        lineNomPar1.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")
        lineNomPar1.setText("$ "+str(self.loteria.precio_boleta))
        lineNomPar1.setAlignment(Qt.AlignCenter)
        lineNomPar1.setReadOnly(True)

        self.lineNomPar=QLineEdit(self.ventanaConcursantes)
        self.lineNomPar.setGeometry(150,50,145,30)
        self.lineNomPar.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")

        btnAgregar=QPushButton("Agregar",self.ventanaConcursantes)
        btnAgregar.setGeometry(110,170,125,40)
        btnAgregar.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        btnAgregar.clicked.connect(self.guardarNombreConcursante)

    
    def guardarNombreConcursante(self):
        if not self.lineNomPar.text():
            self.lineNomPar.setText("")         
        else:
            nom=self.lineNomPar.text()
            concur=Concursante(nom)
            msg=QMessageBox()
            msg.setWindowTitle("Agregar Concursantes")  
            if self.loteria.agregar_concursante(concur):
                msg.setIcon(QMessageBox.Information)
                msg.setText("El concursante "+ concur.__repr__()+" se agregó correctamente")
                self.line2.setText("$ "+str(self.loteria.precio_boleta*self.loteria.lista_concursantes.__len__()))
                self.line3.setText(str(self.loteria.lista_concursantes.__len__()))
                self.pintar_concursantes()
            else:
                msg.setIcon(QMessageBox.Critical)
                msg.setText("El concursante "+ concur.__repr__()+" ya existe")
            x=msg.exec_()
            self.lineNomPar.setText("") 
        self.lineSTR.setText(str(self.loteria.__str__()))
  

    def agregar_ventana_loteria(self):
        self.pintar_concursantes()
        self.pintar_premios()
        self.listaDeConcursantes.setParent(self.ventanaLoteria)
        self.listaDeConcursantes.setGeometry(20,170,300,40)
        self.listaDePremios.setParent(self.ventanaLoteria)
        self.listaDePremios.setGeometry(20,260,300,40)

        self.num_concursante=QLineEdit(self.ventanaLoteria)
        self.num_concursante.setGeometry(35,70,120,30)
        self.num_concursante.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")
        self.num_premio=QLineEdit(self.ventanaLoteria)
        self.num_premio.setGeometry(180,70,120,30)
        self.num_premio.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")

        label_numPar=QLabel("Posición del\nconcursante",self.ventanaLoteria)
        label_numPar.setGeometry(35,20,120,40)
        label_numPar.setStyleSheet("font: 12pt 'MS Sans Serif'")
        label_numPre=QLabel("Posición del\npremio",self.ventanaLoteria)
        label_numPre.setGeometry(180,20,120,40)
        label_numPre.setStyleSheet("font: 12pt 'MS Sans Serif'")

        label_part_ganador=QLabel("GANADOR:",self.ventanaLoteria)
        label_part_ganador.setGeometry(20,140,100,30)
        label_premio_escogido=QLabel("PREMIO:",self.ventanaLoteria)
        label_premio_escogido.setGeometry(20,230,100,30)

        btn_sortear=QPushButton("Sortear",self.ventanaLoteria)
        btn_sortear.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        btn_sortear.setGeometry(120,350,100,50)
        btn_sortear.clicked.connect(self.sorteo)

    
    def sorteo(self):
        try:
            numCon=int(self.num_concursante.text())
            numPre=int(self.num_premio.text())
            msg=QMessageBox()
            msg.setWindowTitle("Ganador Sorteo")  
            resultado=self.loteria.sortear(numCon,numPre)        
            if resultado[0] is not None :
                msg.setIcon(QMessageBox.Information)
                msg.setText("FELICITACIONES :" +str(resultado[0])+
                " Acabas de ganar un@ espectacular : "+str(resultado[1]))
                self.pozoLoteria = self.loteria.pozo()
                self.line1.setText("$ "+str(self.pozoLoteria))
                self.line2.setText("$ "+str(self.loteria.precio_boleta*self.loteria.lista_concursantes.__len__()))
                self.line3.setText(str(self.loteria.lista_concursantes.__len__()))
                self.line4.setText(str(self.loteria.lista_premios.__len__()))
                self.pintar_concursantes()
                self.pintar_premios()               
            else:
                msg.setIcon(QMessageBox.Critical)
                msg.setText("No se cumplen las condiciones necesarias para sortear o no hay un ganador")
            x=msg.exec_()
            self.num_concursante.setText("")
            self.num_premio.setText("")
        except:
            msgError=QMessageBox()
            msgError.setWindowTitle("Aviso")  
            msgError.setIcon(QMessageBox.Critical)
            msgError.setText("VALORES NO VÁLIDOS O NO SE CUMPLE LA CONDICIÓN PARA SORTEAR")
            x=msgError.exec_()
            self.num_concursante.setText("")
            self.num_premio.setText("") 
        self.lineSTR.setText(str(self.loteria.__str__()))

    
    def pintar_premios(self):
        self.listaDePremios.clear()
        lalistadepremios=[]
        for l in self.loteria.lista_premios:
            lalistadepremios.append(l.__repr__())            
        self.listaDePremios.addItems(lalistadepremios) 
        

    def pintar_concursantes(self):
        self.listaDeConcursantes.clear()
        lalistadeconcursantes=[]
        for j in self.loteria.lista_concursantes:
            lalistadeconcursantes.append(j.nombre.__str__())
        self.listaDeConcursantes.addItems(lalistadeconcursantes)    


if __name__ == "__main__":
    app=QApplication([])
    window=Ventana()
    window.show()
    app.exec_()    
    