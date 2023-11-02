#!/usr/bin/env python
import sys
from PyQt5 import uic
from PyQt5 import*
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QListWidget, QLabel, QLineEdit, QFrame, QMessageBox, QRadioButton
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from computador import *

class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()
        #tamaño de la Ventana
        self.setGeometry(0,0,700,800)
        #titulo de la Ventana
        self.setWindowTitle("ALMACÉN")
        #color y diseño de la Ventana
        self.setStyleSheet("background-color: rgb(192, 57, 43)")   
        self.almacen = Almacen()
        #metodo que inicializa los atributos de la interfaz
        #2cadena para representacion
        self.inord = True

        self.initUI()


    def initUI(self):

        label_titulo=QLabel("ALMACÉN",self)
        label_titulo.setGeometry(250,20,190,50)     
        esti="font: 12pt 'MS Sans Serif';background-color: rgb(255, 255, 255)"
        label_titulo.setStyleSheet(esti)
        label_titulo.setAlignment(Qt.AlignCenter)

        #creacion de ls lista dentro del cuadrito azul de disponibilidad
        self.disponibilidad_PCs=QListWidget()
        self.disponibilidad_PCs.setStyleSheet("background-color: rgb(170, 255, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        
        label1=QLabel("\tGanancias",self)
        label1.setGeometry(450,450,190,30)     
        esti="font: 12pt 'MS Sans Serif';background-color: rgb(255, 255, 255)"
        label1.setStyleSheet(esti)
        label1.setAlignment(Qt.AlignCenter)
        
        self.line1=QLineEdit(self)
        esti1="background-color: rgb(255, 255, 16);font: 12pt 'MS Shell Dlg 2'" 
        self.line1.setGeometry(450,480,190,50)
        self.line1.setStyleSheet(esti1)
        self.line1.setText(str(self.almacen.ganancias_netas))
        self.line1.setAlignment(Qt.AlignCenter)
        self.line1.setReadOnly(True)

        label2=QLabel("Computador mayor",self)
        label2.setStyleSheet(esti)
        label2.setAlignment(Qt.AlignCenter)
        label2.setGeometry(450,130,190,30)
        
        self.line2=QLineEdit(self)
        self.line2.setGeometry(450,155,190,50)
        self.line2.setStyleSheet(esti1)
        self.line2.setText(str(self.almacen.mayor_computador()))
        #self.line2.setText("Mayor")
        self.line2.setAlignment(Qt.AlignCenter)
        self.line2.setReadOnly(True)
        
        label3=QLabel("Computador menor",self)
        label3.setStyleSheet(esti)
        label3.setAlignment(Qt.AlignCenter) 
        label3.setGeometry(450,230,190,30)
        
        self.line3=QLineEdit(self)
        self.line3.setGeometry(450,260,190,50)
        self.line3.setStyleSheet(esti1)
        self.line3.setText(str(self.almacen.menor_computador()))
        #self.line3.setText("Menor")
        self.line3.setAlignment(Qt.AlignCenter)
        self.line3.setReadOnly(True)
        
        label4=QLabel("Número de PC´s",self)
        label4.setStyleSheet(esti)
        label4.setAlignment(Qt.AlignCenter)   
        label4.setGeometry(450,340,190,30)
        
        self.line4=QLineEdit(self)
        self.line4.setGeometry(450,370,190,50)
        self.line4.setStyleSheet(esti1)
        self.line4.setText(str(self.almacen.stock.__len__()))
        #self.line4.setText("Numero PC´s")
        self.line4.setAlignment(Qt.AlignCenter)
        self.line4.setReadOnly(True)

        self.frameSTR=QFrame(self)
        self.frameSTR.setGeometry(50,600,570,150)
        self.frameSTR.setStyleSheet("background-color: rgb(255, 255, 255)") 

        self.lineSTR=QLabel(self.frameSTR)
        diseño="background-color: rgb(255, 255, 16);font: 12pt 'MS Shell Dlg 2'"  
        self.lineSTR.setGeometry(90,10,460,130)
        self.lineSTR.setStyleSheet(diseño)
        self.lineSTR.setText(str(self.almacen.reporte()))
        self.lineSTR.setAlignment(Qt.AlignCenter)

        #Aqui van los QRadioButton
        self.inorden = QRadioButton("Inorden", self.frameSTR)
        self.inorden.setGeometry(10,50,60,30)
        #self.inorden.clicked.connect(self.lineSTR.setText(self.almacen.inorden())) #progrmacion del evento de inorden

        self.preorden = QRadioButton("Preorden", self.frameSTR)
        self.preorden.setGeometry(10,85,60,30)
        #self.preorden.clicked.connect(self.lineSTR.setText(self.almacen.preorden())) #progrmacion del evento de preorden

        self.postorden = QRadioButton("Postorden", self.frameSTR)
        self.postorden.setGeometry(10,120,70,30)
        #self.postorden.clicked.connect(self.lineSTR.setText(self.almacen.postorden())) #progrmacion del evento de postorden
        
        self.btn_reporte=QPushButton("Reporte",self.frameSTR)
        self.btn_reporte.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        self.btn_reporte.setGeometry(10,10,70,40)
        self.btn_reporte.clicked.connect(self.reportar)

        
        
        self.ventanaPCs=QFrame(self)
        self.ventanaPCs.setGeometry(50,110,340,450)
        self.ventanaPCs.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.agregarVentanaPCs()

        self.disponibilidad_PCs.setParent(self.ventanaPCs)
        self.disponibilidad_PCs.setGeometry(20,250,300,150)
        self.ventanaPCs.setVisible(True)

      
    def agregarVentanaPCs(self):
        
        self.disponibilidad_PCs.setParent(self.ventanaPCs)
        self.disponibilidad_PCs.setGeometry(20,250,300,150)

        labelNombre=QLabel("Marca:",self.ventanaPCs)
        labelNombre.setGeometry(40,30,70,20)
        labelNombre.setStyleSheet("font: 12pt 'MS Sans Serif'")

        labelVelocidad=QLabel("Velocidad:",self.ventanaPCs)
        labelVelocidad.setGeometry(40,75,75,20)
        labelVelocidad.setStyleSheet("font: 12pt 'MS Sans Serif'")

        labelPrecio=QLabel("Precio:",self.ventanaPCs)
        labelPrecio.setGeometry(40,120,70,20)
        labelPrecio.setStyleSheet("font: 12pt 'MS Sans Serif'")

        self.lineNom=QLineEdit(self.ventanaPCs)
        self.lineNom.setGeometry(150,25,145,30)
        self.lineNom.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")

        self.lineVelo=QLineEdit(self.ventanaPCs)
        self.lineVelo.setGeometry(150,70,145,30)
        self.lineVelo.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")

        self.linePreci=QLineEdit(self.ventanaPCs)
        self.linePreci.setGeometry(150,115,145,30)
        self.linePreci.setStyleSheet("font: 75 11pt 'MS Shell Dlg 2'")

        btnComprar=QPushButton("Comprar",self.ventanaPCs)
        btnComprar.setGeometry(40,170,116,40)
        btnComprar.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        btnComprar.clicked.connect(self.agregar_computador)

        btnVender=QPushButton("Vender",self.ventanaPCs)
        btnVender.setGeometry(183,170,116,40)
        btnVender.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 11pt 'MS Shell Dlg 2'")
        btnVender.clicked.connect(self.borrar_computador)
        
        
    def agregar_computador(self):      
        try:
            marca = self.lineNom.text()
            velo = float(self.lineVelo.text())
            pre=float(self.linePreci.text())
            compu = Computador(marca,velo,pre)

            msg=QMessageBox()
            msg.setWindowTitle("VERIFICACIÓN")
            f = self.almacen.comprar_computador(compu)
            if f:
                msg.setIcon(QMessageBox.Information)
                msg.setText("El Computador: " + compu.__str__() +" se agrego" + 
                " correctamente a lista de PC´s")
                #print(self.almacen.inorden())
                self.line2.setText(str(self.almacen.mayor_computador()))
                self.line3.setText(str(self.almacen.menor_computador()))   
                self.line4.setText(str(self.almacen.stock.__len__()))           
            else:
                msg.setIcon(QMessageBox.Critical)
                msg.setText(" ERROR El compu: " + compu.__str__() +" no se agrego"+ 
                " correctamente a lista de PC´s")
            msg.exec_()    
            self.lineNom.setText("")
            self.lineVelo.setText("")
            self.linePreci.setText("")     
            self.pintar_lista_PCs()
        except  :
            self.lineNom.setText("")
            self.lineVelo.setText("")
            self.linePreci.setText("") 
        if self.inord:
            self.lineSTR.setText(self.almacen.inorden())


    def borrar_computador(self):
        try:
            nom=self.lineNom.text()
            pre = float(self.linePreci.text())
            veloc = float(self.lineVelo.text())
            compu1=Computador(nom,veloc,pre)

            msg1=QMessageBox()
            msg1.setWindowTitle("CONFIRMACIÓN")                 
            if self.almacen.vender_computador(compu1):
                self.line1.setReadOnly(False)
                self.line1.setText("$ "+ str(self.almacen.ganancias_netas))  
                self.line1.setReadOnly(True)
                msg1.setIcon(QMessageBox.Information)
                msg1.setText("VENTA EXITOSA DE " +
                            compu1.__str__())
                x1=msg1.exec_()
                
                self.line2.setText(str(self.almacen.mayor_computador())) 
                self.line3.setText(str(self.almacen.menor_computador())) 
                self.line4.setText(str(self.almacen.stock.__len__()))      
            else:
                msg2=QMessageBox()
                msg2.setIcon(QMessageBox.Critical)
                msg2.setText("No existe el producto " +
                        compu1.__str__())  
                x2=msg2.exec_()
            self.lineNom.setText("")        
            self.linePreci.setText("")

        except:
            self.lineNom.setText("")           
            self.linePreci.setText("")

        self.lineSTR.setText(self.almacen.inorden())
        self.pintar_lista_PCs()


    def reportar(self):
        try:
            self.almacen.reporte()
        except:
            msgError=QMessageBox()
            msgError.setWindowTitle("Aviso")  
            msgError.setIcon(QMessageBox.Critical)
            msgError.setText("VALORES NO VÁLIDOS O NO SE CUMPLE LA CONDICIÓN PARA HACER REPORTE")
            x=msgError.exec_()
        

    
    def pintar_lista_PCs(self):
        """self.disponibilidad_PCs.clear()
        lalistadepcs=[]
        for l in self.almacen.stock.__len__():
            lalistadepcs.append(l.__repr__())            
        self.disponibilidad_PCs.addItems(lalistadepcs)"""
        pass
        

if __name__ == "__main__":
    app=QApplication([])
    window=Ventana()
    window.show()
    app.exec_()    
    