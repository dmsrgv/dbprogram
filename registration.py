# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(202, 262)
        Registration.setStyleSheet("background: rgb(0, 0, 0)")
        self.pushButton = QtWidgets.QPushButton(Registration)
        self.pushButton.setGeometry(QtCore.QRect(9, 224, 182, 29))
        self.pushButton.setStyleSheet("QPushButton {background-color: rgb(255, 255, 0);\n"
"     border-style: outset;\n"
"     border-radius: 10px;\n"
"     border-color: beige;\n"
"     font: bold 14px;\n"
"     min-width: 10em;\n"
"     padding: 6px;}\n"
"QPushButton::hover{background-color: rgb(217, 217, 0)}\n"
"QPushButton::pressed{background-color: rgb(181, 181, 0)}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Registration)
        self.lineEdit.setGeometry(QtCore.QRect(9, 55, 181, 20))
        self.lineEdit.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Registration)
        self.lineEdit_2.setGeometry(QtCore.QRect(9, 126, 181, 20))
        self.lineEdit_2.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Registration)
        self.lineEdit_3.setGeometry(QtCore.QRect(9, 198, 181, 20))
        self.lineEdit_3.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(Registration)
        self.label.setGeometry(QtCore.QRect(9, 9, 26, 16))
        self.label.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Registration)
        self.label_2.setGeometry(QtCore.QRect(9, 81, 37, 16))
        self.label_2.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Registration)
        self.label_3.setGeometry(QtCore.QRect(9, 152, 46, 16))
        self.label_3.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Registration"))
        self.pushButton.setText(_translate("Registration", "Зарегистрироваться"))
        self.label.setText(_translate("Registration", "Имя:"))
        self.label_2.setText(_translate("Registration", "Логин:"))
        self.label_3.setText(_translate("Registration", "Пароль:"))
