# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supervisors.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Supervisors(object):
    def setupUi(self, Supervisors):
        Supervisors.setObjectName("Supervisors")
        Supervisors.resize(519, 402)
        Supervisors.setStyleSheet("background: rgb(24, 24, 24)")
        self.label_2 = QtWidgets.QLabel(Supervisors)
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
        self.comboBox = QtWidgets.QComboBox(Supervisors)
        self.comboBox.setGeometry(QtCore.QRect(10, 120, 231, 22))
        self.comboBox.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(Supervisors)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 161, 16))
        self.label_3.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Supervisors)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 170, 182, 23))
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Supervisors)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 290, 231, 51))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Supervisors)
        self.label.setGeometry(QtCore.QRect(160, 20, 161, 31))
        self.label.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             \n"
"    font: 75 20pt \"MS Shell Dlg 2\";}")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Supervisors)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 120, 182, 31))
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

        self.retranslateUi(Supervisors)
        QtCore.QMetaObject.connectSlotsByName(Supervisors)

    def retranslateUi(self, Supervisors):
        _translate = QtCore.QCoreApplication.translate
        Supervisors.setWindowTitle(_translate("Supervisors", "Form"))
        self.label_2.setText(_translate("Supervisors", "Ваша роль:"))
        self.label_3.setText(_translate("Supervisors", "Выберите курьера:"))
        self.pushButton_2.setText(_translate("Supervisors", "Уволить"))
        self.plainTextEdit.setPlainText(_translate("Supervisors", "Информация"))
        self.label.setText(_translate("Supervisors", "supervisors"))
        self.pushButton_3.setText(_translate("Supervisors", "Добавить курьера"))
