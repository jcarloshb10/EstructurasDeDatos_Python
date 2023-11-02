#!/usr/bin/env python
import sys
from PyQt5 import uic
from PyQt5 import*
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QListWidget, QLabel, QLineEdit, QFrame, QMessageBox
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from ed.secuenciales.notacionpostfija import Postfija

class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()
        #tamaño de la Ventana
        self.setGeometry(0,0,700,700)
        #titulo de la Ventana
        self.setWindowTitle("CALCULADORA")
        #color y diseño de la Ventana
        self.setStyleSheet("background-color: rgb(192, 57, 43)")   
        self.digit = [str(x) for x in range(10)]
        self.oper = ["+","-","/","*","^","(",")"]

        #metodo que inicializa los atributos de la interfaz
        self.initUI()

    def keyPressEvent(self, event):
        print(event.key())
        cast = None
        if event.key() == Qt.Key_Enter:
            self.calcular()
            return
        try:
            cast = chr(event.key())
        except: 
            pass
        if cast in self.digit:
            self.line1.setText(self.line1.text()+cast)
        elif cast in self.oper:
            self.line1.setText(self.line1.text()+" "+cast+" ")
        elif cast == ' ':
            self.line1.setText(self.line1.text()+cast)

    def add(self, char):
        self.line1.setText(self.line1.text()+char)

    def clear(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")
        
    def initUI(self):

        #Titulo 
        
        label=QLabel("Calculadora",self)
        esti="font: 18pt 'MS Sans Serif';background-color: rgb(255, 255, 255)"
        label.setStyleSheet(esti)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(260,30,190,50)

        #Frame de abajo FrameSTR()

        self.frameAbajo=QFrame(self)
        self.frameAbajo.setGeometry(50,320,600,330)
        self.frameAbajo.setStyleSheet("background-color: rgb(255, 255, 255)") 
        
        # Todos los botones abajo en el FrameAbajo

        btn_uno=QPushButton("1",self.frameAbajo)
        btn_uno.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_uno.setGeometry(10,10,100,70)
        btn_uno.clicked.connect(lambda :self.add("1"))

        btn_dos=QPushButton("2",self.frameAbajo)
        btn_dos.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_dos.setGeometry(120,10,100,70)
        btn_dos.clicked.connect(lambda :self.add("2"))

        btn_tres=QPushButton("3",self.frameAbajo)
        btn_tres.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_tres.setGeometry(230,10,100,70)
        btn_tres.clicked.connect(lambda :self.add("3"))

        btn_cuatro=QPushButton("4",self.frameAbajo)
        btn_cuatro.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_cuatro.setGeometry(10,90,100,70)
        btn_cuatro.clicked.connect(lambda :self.add("4"))

        btn_cinco=QPushButton("5",self.frameAbajo)
        btn_cinco.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_cinco.setGeometry(120,90,100,70)
        btn_cinco.clicked.connect(lambda :self.add("5"))

        btn_seis=QPushButton("6",self.frameAbajo)
        btn_seis.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_seis.setGeometry(230,90,100,70)
        btn_seis.clicked.connect(lambda :self.add("6"))

        btn_siete=QPushButton("7",self.frameAbajo)
        btn_siete.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_siete.setGeometry(10,170,100,70)
        btn_siete.clicked.connect(lambda :self.add("7"))

        btn_ocho=QPushButton("8",self.frameAbajo)
        btn_ocho.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_ocho.setGeometry(120,170,100,70)
        btn_ocho.clicked.connect(lambda :self.add("8"))

        btn_nueve=QPushButton("9",self.frameAbajo)
        btn_nueve.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_nueve.setGeometry(230,170,100,70)
        btn_nueve.clicked.connect(lambda :self.add("9"))

        btn_cero=QPushButton("0",self.frameAbajo)
        btn_cero.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_cero.setGeometry(10,250,100,70)
        btn_cero.clicked.connect(lambda :self.add("0"))

        btn_limpiar=QPushButton("C",self.frameAbajo)
        btn_limpiar.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_limpiar.setGeometry(120,250,100,70)
        btn_limpiar.clicked.connect(self.clear)


        btn_abreparen=QPushButton("(",self.frameAbajo)
        btn_abreparen.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_abreparen.setGeometry(340,10,120,70)
        btn_abreparen.clicked.connect(lambda :self.add(" ( "))

        btn_cierraparen=QPushButton(")",self.frameAbajo)
        btn_cierraparen.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_cierraparen.setGeometry(470,10,120,70)
        btn_cierraparen.clicked.connect(lambda :self.add(" ) "))

        btn_suma=QPushButton("+",self.frameAbajo)
        btn_suma.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_suma.setGeometry(340,90,120,70)
        btn_suma.clicked.connect(lambda :self.add(" + "))

        btn_resta=QPushButton("-",self.frameAbajo)
        btn_resta.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_resta.setGeometry(470,90,120,70)
        btn_resta.clicked.connect(lambda :self.add(" - "))

        btn_multiplicacion=QPushButton("*",self.frameAbajo)
        btn_multiplicacion.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_multiplicacion.setGeometry(340,170,120,70)
        btn_multiplicacion.clicked.connect(lambda :self.add(" * "))

        btn_division=QPushButton("/",self.frameAbajo)
        btn_division.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_division.setGeometry(470,170,120,70)
        btn_division.clicked.connect(lambda :self.add(" / "))

        btn_potencia=QPushButton("^",self.frameAbajo)
        btn_potencia.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_potencia.setGeometry(230,250,100,70)
        btn_potencia.clicked.connect(lambda :self.add(" ^ "))

        btn_calcular=QPushButton("Calcular",self.frameAbajo)
        btn_calcular.setStyleSheet("background-color: rgb(85, 170, 255);"+
        "font: 18pt 'MS Shell Dlg 2'")
        btn_calcular.setGeometry(340,250,250,70)
        btn_calcular.clicked.connect(self.calcular)

        #Pantalla de arriba
        esti1="background-color: rgb(255, 255, 16);font: 12pt 'MS Shell Dlg 2'"

        self.frameArriba=QFrame(self)
        self.frameArriba.setGeometry(50,110,600,190)
        self.frameArriba.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frameArriba.setVisible(True)

        label1=QLabel("Exp. Infija: ",self.frameArriba)
        label1.setStyleSheet(esti)
        label1.setAlignment(Qt.AlignCenter) 
        label1.setGeometry(20,10,120,50)
        
        self.line1=QLineEdit(self.frameArriba)
        self.line1.setGeometry(170,10,410,50)
        self.line1.setStyleSheet(esti1)
        #self.line1.setText("") #lo comento porque o sino se cambia la expresion infija
        self.line1.setAlignment(Qt.AlignCenter)
        self.line1.setReadOnly(True)

        label2=QLabel("Exp. Postfija: ",self.frameArriba)
        label2.setStyleSheet(esti)
        label2.setAlignment(Qt.AlignCenter) 
        label2.setGeometry(15,70,160,50)
        
        self.line2=QLineEdit(self.frameArriba)
        self.line2.setGeometry(170,70,410,50)
        self.line2.setStyleSheet(esti1)
        #self.line2.setText("") #
        self.line2.setAlignment(Qt.AlignCenter)
        self.line2.setReadOnly(True)

        label3=QLabel("Resultado: ",self.frameArriba)
        label3.setStyleSheet(esti)
        label3.setAlignment(Qt.AlignCenter) 
        label3.setGeometry(15,130,140,50)
        
        self.line3=QLineEdit(self.frameArriba)
        self.line3.setGeometry(170,130,410,50)
        self.line3.setStyleSheet(esti1)
        #self.line3.setText("") #
        self.line3.setAlignment(Qt.AlignCenter)
        self.line3.setReadOnly(True)


    def calcular(self):
            exp = Postfija(self.line1.text())
            self.line2.setText(exp.postfija())
            res = str(exp.eval_expr_aritm())
            self.line3.setText(res)
            

if __name__ == "__main__":
    app=QApplication([])
    window=Ventana()
    window.show()
    app.exec_()
