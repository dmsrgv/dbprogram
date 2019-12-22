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
        Admins.resize(543, 426)
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
        self.pushButton_2.setGeometry(QtCore.QRect(290, 202, 182, 31))
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
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 290, 231, 121))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.plainTextEdit.setReadOnly(False)
        self.plainTextEdit.setPlainText("")
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
        self.label_6 = QtWidgets.QLabel(Admins)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 161, 16))
        self.label_6.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Admins)
        self.label_7.setGeometry(QtCore.QRect(270, 360, 261, 16))
        self.label_7.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Admins)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 160, 221, 31))
        self.plainTextEdit_2.setStyleSheet("QPlainTextEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setPlaceholderText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_5 = QtWidgets.QLabel(Admins)
        self.label_5.setGeometry(QtCore.QRect(280, 170, 251, 16))
        self.label_5.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(Admins)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 202, 182, 31))
        self.pushButton_4.setStyleSheet("QPushButton {background-color: rgb(255, 255, 0);\n"
"     border-style: outset;\n"
"     border-radius: 10px;\n"
"     border-color: beige;\n"
"     font: bold 14px;\n"
"     min-width: 10em;\n"
"     padding: 6px;}\n"
"QPushButton::hover{background-color: rgb(217, 217, 0)}\n"
"QPushButton::pressed{background-color: rgb(181, 181, 0)}")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Admins)
        QtCore.QMetaObject.connectSlotsByName(Admins)

    def retranslateUi(self, Admins):
        _translate = QtCore.QCoreApplication.translate
        Admins.setWindowTitle(_translate("Admins", "Form"))
        self.label_2.setText(_translate("Admins", "Ваша роль:"))
        self.label_3.setText(_translate("Admins", "Выберите пользователя:"))
        self.pushButton_2.setText(_translate("Admins", "Назначить"))
        self.plainTextEdit.setPlaceholderText(_translate("Admins", "Введите любой запрос..."))
        self.label.setText(_translate("Admins", "admins"))
        self.pushButton_3.setText(_translate("Admins", "Выполнить"))
        self.label_4.setText(_translate("Admins", "Выберите роль:"))
        self.label_6.setText(_translate("Admins", "Запрос:"))
        self.pushButton_4.setText(_translate("Admins", "Узнать роль"))
