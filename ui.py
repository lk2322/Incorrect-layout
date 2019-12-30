# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created: Mon Dec 30 07:02:01 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
import PySide2
from PySide2 import QtWidgets, QtCore, QtGui


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 101)
        Form.setFixedSize(395, 101)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(202, 40, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(74, 40, 121, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(73, 10, 251, 21))
        self.lineEdit.setCursor(QtCore.Qt.IBeamCursor)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setFrame(True)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        # self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(73, 69, 251, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle("Переводчик")
        Form.setWindowIcon(QtGui.QIcon('2.ico'))
        self.pushButton_2.setText("Сохранить в Txt")
        self.pushButton_3.setText("Перевести")
