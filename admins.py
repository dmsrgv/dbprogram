# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admins.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admins(object):
    def setupUi(self, Admins):
        Admins.setObjectName("Admins")
        Admins.resize(519, 402)
        Admins.setStyleSheet("background: rgb(24, 24, 24)")
        self.label_2 = QtWidgets.QLabel(Admins)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             \n"
"    font: 75 20pt \"MS Shell Dlg 2\";}")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Admins)
        self.comboBox.setGeometry(QtCore.QRect(10, 120, 231, 22))
        self.comboBox.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(Admins)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 161, 16))
        self.label_3.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Admins)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 170, 182, 23))
        self.pushButton_2.setStyleSheet("QPushButton {background-color: rgb(255, 255, 0);\n"
"     border-style: outset;\n"
"     border-radius: 10px;\n"
"     border-color: beige;\n"
"     font: bold 14px;\n"
"     min-width: 10em;\n"
"     padding: 6px;}\n"
"QPushButton::hover{background-color: rgb(217, 217, 0)}\n"
"QPushButton::pressed{background-color: rgb(181, 181, 0)}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Admins)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 260, 231, 121))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Admins)
        self.label.setGeometry(QtCore.QRect(160, 20, 161, 31))
        self.label.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             \n"
"    font: 75 20pt \"MS Shell Dlg 2\";}")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Admins)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 300, 182, 31))
        self.pushButton_3.setStyleSheet("QPushButton {background-color: rgb(255, 255, 0);\n"
"     border-style: outset;\n"
"     border-radius: 10px;\n"
"     border-color: beige;\n"
"     font: bold 14px;\n"
"     min-width: 10em;\n"
"     padding: 6px;}\n"
"QPushButton::hover{background-color: rgb(217, 217, 0)}\n"
"QPushButton::pressed{background-color: rgb(181, 181, 0)}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Admins)
        self.label_4.setGeometry(QtCore.QRect(270, 70, 161, 16))
        self.label_4.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(Admins)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 120, 231, 22))
        self.comboBox_2.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(Admins)
        self.label_5.setGeometry(QtCore.QRect(260, 360, 161, 16))
        self.label_5.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Admins)
        QtCore.QMetaObject.connectSlotsByName(Admins)

    def retranslateUi(self, Admins):
        _translate = QtCore.QCoreApplication.translate
        Admins.setWindowTitle(_translate("Admins", "Form"))
        self.label_2.setText(_translate("Admins", "Ваша роль:"))
        self.label_3.setText(_translate("Admins", "Выберите пользователя:"))
        self.pushButton_2.setText(_translate("Admins", "Назначить"))
        self.plainTextEdit.setPlainText(_translate("Admins", "Введите любой запрос..."))
        self.label.setText(_translate("Admins", "admins"))
        self.pushButton_3.setText(_translate("Admins", "Выполнить"))
        self.label_4.setText(_translate("Admins", "Выберите роль:"))
