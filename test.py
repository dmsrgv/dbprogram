# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Clients(object):
    def setupUi(self, Clients):
        Clients.setObjectName("Clients")
        Clients.resize(535, 703)
        Clients.setStyleSheet("background: rgb(24, 24, 24)")
        self.label_2 = QtWidgets.QLabel(Clients)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 151, 31))
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
        self.comboBox = QtWidgets.QComboBox(Clients)
        self.comboBox.setGeometry(QtCore.QRect(20, 230, 231, 22))
        self.comboBox.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"                     font: bold;\n"
"}\n"
"QComboBox:editable {\n"
"    color:  rgb(85, 255, 0)\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(Clients)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 141, 16))
        self.label_3.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Clients)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 121, 16))
        self.label_4.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Clients)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 420, 182, 23))
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Clients)
        self.plainTextEdit.setGeometry(QtCore.QRect(280, 520, 231, 111))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Clients)
        self.label.setGeometry(QtCore.QRect(170, 70, 111, 31))
        self.label.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             \n"
"    font: 75 20pt \"MS Shell Dlg 2\";}")
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(Clients)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 230, 231, 22))
        self.comboBox_2.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(Clients)
        self.label_5.setGeometry(QtCore.QRect(290, 180, 141, 16))
        self.label_5.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_5.setObjectName("label_5")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Clients)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(280, 300, 231, 111))
        self.plainTextEdit_2.setStyleSheet("QPlainTextEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.plainTextEdit_2.setReadOnly(False)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_6 = QtWidgets.QLabel(Clients)
        self.label_6.setGeometry(QtCore.QRect(320, 70, 31, 16))
        self.label_6.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Clients)
        self.lineEdit.setGeometry(QtCore.QRect(320, 90, 113, 20))
        self.lineEdit.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(Clients)
        self.label_7.setGeometry(QtCore.QRect(190, 120, 111, 16))
        self.label_7.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(Clients)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 150, 113, 20))
        self.lineEdit_2.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Clients)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 150, 141, 20))
        self.lineEdit_3.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(Clients)
        self.label_8.setGeometry(QtCore.QRect(320, 120, 141, 16))
        self.label_8.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Clients)
        self.label_9.setGeometry(QtCore.QRect(30, 120, 141, 16))
        self.label_9.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(Clients)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 150, 113, 20))
        self.lineEdit_4.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tableWidget = QtWidgets.QTableWidget(Clients)
        self.tableWidget.setGeometry(QtCore.QRect(20, 300, 231, 111))
        self.tableWidget.setStyleSheet("QTableWidget {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Clients)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(20, 520, 231, 111))
        self.plainTextEdit_3.setStyleSheet("QPlainTextEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_10 = QtWidgets.QLabel(Clients)
        self.label_10.setGeometry(QtCore.QRect(280, 270, 121, 16))
        self.label_10.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_10.setObjectName("label_10")
        self.pushButton_3 = QtWidgets.QPushButton(Clients)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 650, 182, 23))
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
        self.label_11 = QtWidgets.QLabel(Clients)
        self.label_11.setGeometry(QtCore.QRect(20, 490, 121, 16))
        self.label_11.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Clients)
        self.label_12.setGeometry(QtCore.QRect(290, 490, 121, 16))
        self.label_12.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_12.setObjectName("label_12")
        self.label_16 = QtWidgets.QLabel(Clients)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 491, 31))
        self.label_16.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;    \n"
"font-size: 20pt        }")
        self.label_16.setObjectName("label_16")
        self.graphicsView = QtWidgets.QGraphicsView(Clients)
        self.graphicsView.setGeometry(QtCore.QRect(10, 11, 511, 451))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Clients)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 480, 511, 211))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(Clients)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 10, 511, 51))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView.raise_()
        self.graphicsView_2.raise_()
        self.graphicsView_3.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_2.raise_()
        self.plainTextEdit.raise_()
        self.label.raise_()
        self.comboBox_2.raise_()
        self.label_5.raise_()
        self.plainTextEdit_2.raise_()
        self.label_6.raise_()
        self.lineEdit.raise_()
        self.label_7.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.lineEdit_4.raise_()
        self.tableWidget.raise_()
        self.plainTextEdit_3.raise_()
        self.label_10.raise_()
        self.pushButton_3.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_16.raise_()

        self.retranslateUi(Clients)
        QtCore.QMetaObject.connectSlotsByName(Clients)

    def retranslateUi(self, Clients):
        _translate = QtCore.QCoreApplication.translate
        Clients.setWindowTitle(_translate("Clients", "Form"))
        self.label_2.setText(_translate("Clients", "Ваша роль:"))
        self.label_3.setText(_translate("Clients", "Выберите ресторан:"))
        self.label_4.setText(_translate("Clients", "Выберите блюдо:"))
        self.pushButton_2.setText(_translate("Clients", "Заказать"))
        self.plainTextEdit.setPlainText(_translate("Clients", "Информация"))
        self.label.setText(_translate("Clients", "clients"))
        self.label_5.setText(_translate("Clients", "Выберите тип оплаты:"))
        self.plainTextEdit_2.setPlainText(_translate("Clients", "Ваш комментарий..."))
        self.label_6.setText(_translate("Clients", "Имя:"))
        self.label_7.setText(_translate("Clients", "Адрес:"))
        self.label_8.setText(_translate("Clients", "Промокод скидки:"))
        self.label_9.setText(_translate("Clients", "Телефон:"))
        self.plainTextEdit_3.setPlainText(_translate("Clients", "Вы выбрали"))
        self.label_10.setText(_translate("Clients", "Ваш комментарий:"))
        self.pushButton_3.setText(_translate("Clients", "Очистить"))
        self.label_11.setText(_translate("Clients", "Ваш заказ:"))
        self.label_12.setText(_translate("Clients", "Информация:"))
        self.label_16.setText(_translate("Clients", "ЛОЛ"))
