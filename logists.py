# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logists.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Logists(object):
    def setupUi(self, Logists):
        Logists.setObjectName("Logists")
        Logists.resize(519, 379)
        Logists.setStyleSheet("background: rgb(24, 24, 24)")
        self.label_2 = QtWidgets.QLabel(Logists)
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
        self.comboBox = QtWidgets.QComboBox(Logists)
        self.comboBox.setGeometry(QtCore.QRect(10, 120, 231, 22))
        self.comboBox.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(Logists)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 141, 16))
        self.label_3.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Logists)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 180, 182, 23))
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Logists)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 240, 461, 111))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Logists)
        self.label.setGeometry(QtCore.QRect(160, 20, 111, 31))
        self.label.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             \n"
"    font: 75 20pt \"MS Shell Dlg 2\";}")
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(Logists)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 120, 231, 22))
        self.comboBox_2.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(Logists)
        self.label_5.setGeometry(QtCore.QRect(280, 80, 141, 16))
        self.label_5.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Logists)
        QtCore.QMetaObject.connectSlotsByName(Logists)

    def retranslateUi(self, Logists):
        _translate = QtCore.QCoreApplication.translate
        Logists.setWindowTitle(_translate("Logists", "Form"))
        self.label_2.setText(_translate("Logists", "Ваша роль:"))
        self.label_3.setText(_translate("Logists", "Выберите курьера:"))
        self.pushButton_2.setText(_translate("Logists", "Назначить"))
        self.plainTextEdit.setPlainText(_translate("Logists", "Информация"))
        self.label.setText(_translate("Logists", "logists"))
        self.label_5.setText(_translate("Logists", "Выберите заказ:"))
