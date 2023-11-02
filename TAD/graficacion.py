
#!/usr/bin/env python
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

qtCreatorFile = "Calculadora.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def _init_(self):
        QtWidgets.QMainWindow._init_(self)
        Ui_MainWindow._init_(self)
        self.setupUi(self)
        #self.boton.clicked.connect(self.pri)
        #self.qlineedi=QLineEdit(self)
        #self.qlineedi.move(330,460)
        #self.qlineedi.setText("none")
        
    def pri(self): 
        if type(self.num1.text())==type(3) and type(self.num2.text())==type(3):
            a=int(self.num1.text())
            b=int(self.num2.text())
            self.qlineedi.setText(str(a+b))
        else:
            self.num1.setText("")
            self.num2.setText("") 
        

if __name__ == "_main_":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    #sys.exit(app.exec_())