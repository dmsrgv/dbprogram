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
        Supervisors.resize(602, 473)
        Supervisors.setStyleSheet("background: rgb(24, 24, 24)")
        self.label_2 = QtWidgets.QLabel(Supervisors)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 151, 31))
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
        self.comboBox.setGeometry(QtCore.QRect(30, 120, 231, 22))
        self.comboBox.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(Supervisors)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 161, 16))
        self.label_3.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Supervisors)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 170, 182, 23))
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
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 220, 231, 201))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Supervisors)
        self.label.setGeometry(QtCore.QRect(180, 20, 161, 31))
        self.label.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             \n"
"    font: 75 20pt \"MS Shell Dlg 2\";}")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Supervisors)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 380, 182, 31))
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
        self.comboBox_2 = QtWidgets.QComboBox(Supervisors)
        self.comboBox_2.setGeometry(QtCore.QRect(340, 110, 231, 22))
        self.comboBox_2.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.comboBox_2.setObjectName("comboBox_2")
        self.graphicsView = QtWidgets.QGraphicsView(Supervisors)
        self.graphicsView.setGeometry(QtCore.QRect(320, 61, 261, 401))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Supervisors)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 60, 261, 401))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_4 = QtWidgets.QLabel(Supervisors)
        self.label_4.setGeometry(QtCore.QRect(340, 80, 161, 16))
        self.label_4.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Supervisors)
        self.label_5.setGeometry(QtCore.QRect(340, 140, 161, 16))
        self.label_5.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(Supervisors)
        self.comboBox_3.setGeometry(QtCore.QRect(340, 170, 231, 22))
        self.comboBox_3.setStyleSheet("QComboBox {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.comboBox_3.setObjectName("comboBox_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Supervisors)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 200, 113, 20))
        self.lineEdit_2.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Supervisors)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 230, 113, 20))
        self.lineEdit_3.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Supervisors)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 260, 113, 20))
        self.lineEdit_4.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Supervisors)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 290, 113, 20))
        self.lineEdit_5.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Supervisors)
        self.lineEdit_6.setGeometry(QtCore.QRect(440, 320, 113, 20))
        self.lineEdit_6.setStyleSheet("QLineEdit {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(Supervisors)
        self.label_6.setGeometry(QtCore.QRect(330, 200, 91, 16))
        self.label_6.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Supervisors)
        self.label_7.setGeometry(QtCore.QRect(330, 230, 91, 16))
        self.label_7.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Supervisors)
        self.label_8.setGeometry(QtCore.QRect(330, 260, 91, 16))
        self.label_8.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Supervisors)
        self.label_9.setGeometry(QtCore.QRect(330, 290, 91, 16))
        self.label_9.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Supervisors)
        self.label_10.setGeometry(QtCore.QRect(330, 320, 101, 16))
        self.label_10.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Supervisors)
        self.label_11.setGeometry(QtCore.QRect(360, 420, 211, 21))
        self.label_11.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Supervisors)
        self.label_12.setGeometry(QtCore.QRect(390, 440, 181, 21))
        self.label_12.setStyleSheet("QLabel {color: rgb(85, 255, 0);\n"
"             font: bold;            }")
        self.label_12.setObjectName("label_12")
        self.graphicsView_2.raise_()
        self.graphicsView.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.plainTextEdit.raise_()
        self.label.raise_()
        self.pushButton_3.raise_()
        self.comboBox_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.comboBox_3.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()

        self.retranslateUi(Supervisors)
        QtCore.QMetaObject.connectSlotsByName(Supervisors)

    def retranslateUi(self, Supervisors):
        _translate = QtCore.QCoreApplication.translate
        Supervisors.setWindowTitle(_translate("Supervisors", "Form"))
        self.label_2.setText(_translate("Supervisors", "Ваша роль:"))
        self.label_3.setText(_translate("Supervisors", "Выберите курьера:"))
        self.pushButton_2.setText(_translate("Supervisors", "Выбрать"))
        self.label.setText(_translate("Supervisors", "supervisors"))
        self.pushButton_3.setText(_translate("Supervisors", "Добавить курьера"))
        self.label_4.setText(_translate("Supervisors", "Курьерская служба:"))
        self.label_5.setText(_translate("Supervisors", "Тип курьера:"))
        self.label_6.setText(_translate("Supervisors", "Имя:"))
        self.label_7.setText(_translate("Supervisors", "Фамилия:"))
        self.label_8.setText(_translate("Supervisors", "Отчество:"))
        self.label_9.setText(_translate("Supervisors", "Телефон:"))
        self.label_10.setText(_translate("Supervisors", "День рождения:"))
        self.label_11.setText(_translate("Supervisors", "После добавление курьера,"))
        self.label_12.setText(_translate("Supervisors", "нужно перезайти в систему"))
