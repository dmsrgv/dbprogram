# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zakaz.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Zakaz(object):
    def setupUi(self, Zakaz):
        Zakaz.setObjectName("Zakaz")
        Zakaz.resize(370, 362)
        Zakaz.setStyleSheet("background: rgb(24, 24, 24)")
        self.label = QtWidgets.QLabel(Zakaz)
        self.label.setGeometry(QtCore.QRect(120, 20, 141, 16))
        self.label.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Zakaz)
        self.comboBox.setGeometry(QtCore.QRect(60, 50, 231, 22))
        self.comboBox.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(Zakaz)
        self.pushButton.setGeometry(QtCore.QRect(80, 240, 182, 23))
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
        self.label_2 = QtWidgets.QLabel(Zakaz)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 121, 16))
        self.label_2.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Zakaz)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 270, 191, 71))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tableWidget = QtWidgets.QTableWidget(Zakaz)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 321, 111))
        self.tableWidget.setStyleSheet("QTableWidget {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Zakaz)
        QtCore.QMetaObject.connectSlotsByName(Zakaz)

    def retranslateUi(self, Zakaz):
        _translate = QtCore.QCoreApplication.translate
        Zakaz.setWindowTitle(_translate("Zakaz", "Form"))
        self.label.setText(_translate("Zakaz", "Выберите ресторан:"))
        self.pushButton.setText(_translate("Zakaz", "Заказать"))
        self.label_2.setText(_translate("Zakaz", "Выберите блюдо:"))
        self.plainTextEdit.setPlainText(_translate("Zakaz", "Информация"))
