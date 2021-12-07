# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GAMEMENU.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import numpy as np
import pygame
import sys
import math
import os
import random
import subprocess
import DINOCODE

pygame.init()
from PyQt5 import QtCore, QtGui, QtWidgets

#def run(self, path):
    #subprocess.call(['pythonw',path])

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 420)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.CONNECTButton = QtWidgets.QPushButton(Form)
        self.CONNECTButton.setGeometry(QtCore.QRect(400, 190, 271, 151))
        self.CONNECTButton.setStyleSheet("font: 28pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.CONNECTButton.setObjectName("CONNECTButton")
        self.DINOButton = QtWidgets.QPushButton(Form)
        self.DINOButton.setGeometry(QtCore.QRect(60, 190, 271, 151))
        self.DINOButton.setStyleSheet("font: 28pt \"OCR A Extended\";\n"
"background-color: rgb(255, 255, 255);")
        self.DINOButton.setObjectName("DINOButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 80, 531, 91))
        self.label.setStyleSheet("font: 36pt \"Sylfaen\";\n"
"color: rgb(0, 25, 255);")
        self.label.setObjectName("label")
        self.DINOButton.clicked.connect(DINOCODE.startdino())
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CONNECTButton.setText(_translate("Form", "CONNECT 4"))
        self.DINOButton.setText(_translate("Form", "DINO GAME"))
        self.label.setText(_translate("Form", "Please Choose Your Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
