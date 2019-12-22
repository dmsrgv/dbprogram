# Библиотеки
from datetime import datetime, timedelta
import sys
import psycopg2
# Импортируем наш интерфейс
from design import *
from registration import *
from test import *
from zakaz import *
from admins import *
from logists import *
from supervisors import *
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QAction
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator


# Главное окно

class Window1(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Вход')
        self.ui.lineEdit_2.setEchoMode(self.ui.lineEdit_2.Password)
        slov_logpass = QtCore.QRegExp("[0-9a-zA-Z]{20}")
        validator_logpass = QtGui.QRegExpValidator(slov_logpass)
        self.ui.lineEdit.setValidator(validator_logpass)
        self.ui.lineEdit_2.setValidator(validator_logpass)
        self.ui.label.setVisible(True)
        self.ui.label_2.setVisible(True)

        # Здесь прописываем событие нажатия на кнопку
        # self.ui.pushButton.clicked.connect(self.show_registration)
        self.ui.pushButton_2.clicked.connect(self.show_registration)
        self.ui.pushButton.clicked.connect(self.login_enter)
        # self.ui.pushButton_3.clicked.connect(self.connect_bd)
        # self.ui.pushButton_2.clicked.connect(self.push_query)
        # self.ui.pushButton_4.clicked.connect(self.select_all)

        # Вход

    def login_enter(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        try:
            con = psycopg2.connect(
                database="DeliveryFood",
                user=username,
                password=password,
                host="127.0.0.1",
                port="5432"
            )
            cur = con.cursor()
            cur.execute(
                "select * from information_schema.applicable_roles WHERE grantee =" + "'" + username + "'")
            role = cur.fetchone()[1]
            if role == "clients":
                self.window_clients()
            elif role == "supervisors":
                self.window_supervisors()
            elif role == "admins":
                self.window_admins()
            elif role == "logists":
                self.window_logists()
            self.ui.label.setText("УСПЕХ")
            return con

        except psycopg2.DatabaseError:
            self.ui.label.setText("НЕ УСПЕХ")

            # Покажем окно регистрации

    def show_registration(self):
        self.w = Registration()
        self.w.show()

        # Вызов окна для клиентов

    def window_clients(self):
        self.w = Window_clients()
        self.w.show()

        # Вызов окна для админов

    def window_admins(self):
        self.w = Window_admins()
        self.w.show()

        # Вызов окна для логистов

    def window_logists(self):
        self.w = Window_logists()
        self.w.show()

        # Вызов окна для супервайзеров

    def window_supervisors(self):
        self.w = Window_supervisors()
        self.w.show()

        # Метод подключени я к бд

    def connect_bd(self):
        try:
            con = psycopg2.connect(
                database="DeliveryFood",
                user="postgres",
                password="1",
                host="127.0.0.1",
                port="5432"
            )
            self.ui.label.setText("Подключение успешно")
            return con
        except psycopg2.DatabaseError:
            self.ui.label.setText("Подключение не удалось")

            # Метод отправки запросов ( не используется пока-что)

    def push_query(self):
        con = self.connect_bd()
        cur = con.cursor()
        try:
            cur.execute(self.ui.plainTextEdit.toPlainText())
            self.ui.label_2.setText("Запрос выполнен!")
            con.commit()
            con.close()
        except psycopg2.DatabaseError:
            self.ui.label_2.setText("Ошибка")
        finally:
            if con:
                con.close()


# Окно регистрации

class Registration(QMainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.ui = Ui_Registration()
        self.ui.setupUi(self)
        self.setWindowTitle("Регистрация")
        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.lineEdit_3.setEchoMode(self.ui.lineEdit_3.Password)

        slov_name = QtCore.QRegExp("[а-яА-Я0-9a-zA-Z]{20}")
        slov_logpass = QtCore.QRegExp("[0-9a-zA-Z]{20}")
        validator_name = QtGui.QRegExpValidator(slov_name)
        validator_logpass = QtGui.QRegExpValidator(slov_logpass)

        self.ui.lineEdit.setValidator(validator_name)
        self.ui.lineEdit_2.setValidator(validator_logpass)
        self.ui.lineEdit_3.setValidator(validator_logpass)

        # Создание пользователя

    def reg(self):
        con = Window1().connect_bd()
        cur = con.cursor()
        # cur.execute('CREATE USER %s WITH PASSWORD %s', (self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text()))
        cur.execute(
            "CREATE USER " + self.ui.lineEdit_2.text() + " WITH PASSWORD " + "'" + self.ui.lineEdit_3.text() + "'")

        con.commit()
        cur.execute("GRANT clients TO " + self.ui.lineEdit_2.text())

        con.commit()
        con.close()

    # Окно для клиентов


class Window_clients(QMainWindow):
    def __init__(self):
        super(Window_clients, self).__init__()
        self.ui = Ui_Clients()
        self.ui.setupUi(self)
        self.setWindowTitle('Client Form')
        self.sum_prize = 0
        self.ui.comboBox.activated.connect(self.onActivation)
        self.ui.comboBox_2.activated.connect(self.check_id_payments)
        self.ui.pushButton_2.clicked.connect(self.zakazat)
        self.ui.plainTextEdit_2.setPlainText("")
        self.ui.plainTextEdit_3.setPlainText("")
        self.ui.plainTextEdit_2.setPlaceholderText("Введите ваш комментарий...")
        self.ui.tableWidget.clicked.connect(self.click_table)
        self.ui.pushButton_3.clicked.connect(self.clear_dishes)
        rest = self.ui.comboBox
        type_payments = self.ui.comboBox_2
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("SELECT COUNT(id_restaurant) from restaurant")
        result = cur.fetchone()
        col = int(result[0]) + 1
        con.commit()
        try:

            for i in range(1, col):
                cur = con.cursor()
                cur.execute("select name_restaurant from restaurant where id_restaurant =" + str(i) + "")
                result = cur.fetchone()
                rest.addItems(result)
            con.commit()
            for i in range(1, 3):
                cur = con.cursor()
                cur.execute("select name_type_payments from type_payments where id_type_payments =" + str(i))
                result = cur.fetchone()
                type_payments.addItems(result)

        except psycopg2.DatabaseError:
            print("Ошибка")


    def click_table(self):
        row = self.ui.tableWidget.currentRow()
        col = 0
        value = self.ui.tableWidget.item(row, col).text()
        id_restik = int((self.ui.comboBox.currentIndex() + 1))
        self.ui.plainTextEdit_3.appendPlainText(str(value))
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("select prize_dish from dishes where id_restaurant = %s and name_dish = %s",
                    (id_restik, value))
        prize = cur.fetchone()[0]
        #sum_prize = sum_prize + prize
        prize = prize.replace(" ?", "")
        prize = prize.replace(",",".")
        self.sum_prize += float(prize)
        return self.sum_prize


    def clear_dishes(self):
        self.ui.plainTextEdit_3.setPlainText("")
        self.sum_prize = 0


            # Обработка кнопки "Заказать". Добавление заказа

    def zakazat(self):
        now = datetime.now()
        ordered_in = now.strftime("%H:%M:%S")
        after = now + timedelta(minutes=45)
        deliver_in = after.strftime("%H:%M:%S")
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("select count(id_order) from orders")
        id_order = cur.fetchone()[0] + 1
        id_type_payments = self.check_id_payments()
        id_restaurant = self.check_id_restaurant()
        id_status = 3
        id_discount = self.check_id_discount()
        id_client = self.client_create()
        self.ui.plainTextEdit.setPlainText("Номер вашего заказа: " + str(id_order))
        self.ui.plainTextEdit.appendPlainText("Время заказа:   " + str(ordered_in))
        self.ui.plainTextEdit.appendPlainText("Время доставки: " + str(deliver_in))
        self.ui.plainTextEdit.appendPlainText("Сумма к оплате: " + str(self.sum_prize) + " рублей")

        # print(id_order, id_type_payments, id_status, id_discount, id_client, id_discount)
        cur.execute(
            "INSERT INTO orders (id_order,id_type_payments,id_status,deliver_in,id_restaurant, id_client, id_discount, ordered_in) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (id_order, id_type_payments, id_status, deliver_in, id_restaurant, id_client, id_discount, ordered_in))
        con.commit()

        # rezz = self.poluchim_x()

    ## print(rezz)
    # print(id_order)
    # cur.execute("INSERT INTO orders (id_order,id_type_payments,id_status,deliver_in,id_restaurant, id_client, id_discount) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')")

    # Создаем клиента



    def client_create(self):
        try:
            con = Window1().connect_bd()
            cur = con.cursor()
            cur.execute("SELECT COUNT(id_client) from clients")
            id_client = cur.fetchone()[0] + 1
            name_client = self.ui.lineEdit.text()
            address_client = self.ui.lineEdit_2.text()
            comment_client = self.ui.plainTextEdit_2.toPlainText()
            phone_client = self.ui.lineEdit_4.text()
            cur.execute(
                "INSERT INTO clients (id_client, name_client, address_client, comment_client, phone_client) VALUES (%s, %s, %s, %s, %s)",
                (id_client, name_client, address_client, comment_client, phone_client))
            con.commit()
            con.close()
            return id_client

        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            sys.exit(1)

    # Проверяем id оплаты по выбору в комбобоксе
    def check_id_payments(self):
        index = self.ui.comboBox_2.currentIndex()
        return index + 1

    # Проверяем id ресторана
    def check_id_restaurant(self):
        index = self.ui.comboBox.currentIndex()
        return index + 1

    # Проверяем id скидки
    def check_id_discount(self):
        if self.ui.lineEdit_3.text() == "":
            id_discount = 1
            return id_discount
        else:
            con = Window1().connect_bd()
            cur = con.cursor()
            promokod = self.ui.lineEdit_3.text()
            cur.execute("SELECT id_discount FROM system_discount WHERE promokod = %s", (promokod,))
            id_discount = cur.fetchone()[0]
            return id_discount

    # Выводим список блюд в зависимости от выбора ресторана

    def onActivation(self, index):
        con = Window1().connect_bd()
        cur = con.cursor()
        col = index + 1
        try:
            cur.execute("SELECT name_dish,prize_dish FROM dishes WHERE id_restaurant =" + str(col) + "")
            result = cur.fetchall()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(2)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Блюда                         ", "Цена            "])
            self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.ui.tableWidget.sizeHintForColumn(2)
            self.ui.tableWidget.resizeColumnsToContents()

            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            con.commit()
            con.close()
        except psycopg2.DatabaseError:
            print("Ошибка")
        finally:
            if con:
                con.close()

                # Не используется пока-что

    def client_query(self):
        con = Window1().connect_bd()
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM " + self.ui.lineEdit.text())
            result = cur.fetchall()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(12)

            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.tableWidget.setColumnCount(column_number + 1)
            con.commit()
            con.close()
            self.ui.label.setText("Выполнено!")
        except psycopg2.DatabaseError:
            self.ui.label.setText("Ошибка!")
        finally:
            if con:
                con.close()


# Не используется

class Zakaz(QMainWindow):
    def __init__(self):
        super(Zakaz, self).__init__()
        self.ui = Ui_Zakaz()
        self.ui.setupUi(self)
        self.setWindowTitle('Zakaz Form')
        self.ui.comboBox.activated.connect(self.onActivation)
        rest = self.ui.comboBox
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("SELECT COUNT(id_restaurant) from restaurant")
        result = cur.fetchone()
        col = int(result[0]) + 1
        con.commit()
        try:
            for i in range(1, col):
                cur = con.cursor()
                cur.execute("select name_restaurant from restaurant where id_restaurant =" + str(i) + "")
                result = cur.fetchone()
                rest.addItems(result)

            con.commit()
            con.close()

        except psycopg2.DatabaseError:
            print("Error")
            self.ui.plainTextEdit.setPlainText("Ошибка")

    def onActivation(self, index):
        con = Window1().connect_bd()
        cur = con.cursor()
        col = index + 1
        try:
            cur.execute("SELECT name_dish FROM dishes WHERE id_restaurant =" + str(col) + "")
            result = cur.fetchall()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(12)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Блюда"])
            self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.ui.tableWidget.sizeHintForColumn(1)
            self.ui.tableWidget.resizeColumnsToContents()

            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.tableWidget.setColumnCount(1)
            con.commit()
            con.close()
            self.ui.label.setText("Выполнено!")
        except psycopg2.DatabaseError:
            self.ui.label.setText("Ошибка!")
        finally:
            if con:
                con.close()


# Окно для админов (в разработке)

class Window_admins(QMainWindow):
    def __init__(self):
        super(Window_admins, self).__init__()
        self.ui = Ui_Admins()
        self.ui.setupUi(self)
        self.setWindowTitle('Admins Form')


# Окно для супервайзеров ( в разработке)

class Window_supervisors(QMainWindow):
    def __init__(self):
        super(Window_supervisors, self).__init__()
        self.ui = Ui_Supervisors()
        self.ui.setupUi(self)
        self.setWindowTitle('Supervisors Form')


# Окно для логистов (в разработке)

class Window_logists(QMainWindow):
    def __init__(self):
        super(Window_logists, self).__init__()
        self.ui = Ui_Logists()
        self.ui.setupUi(self)
        self.setWindowTitle('Logists Form')
        self.ui.pushButton_2.clicked.connect(self.courier_order)
        self.ui.plainTextEdit.setPlainText("")
        couriers = self.ui.comboBox
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("SELECT COUNT(ID_courier) from couriers")
        result = cur.fetchone()
        col = int(result[0]) + 1
        con.commit()
        for i in range(1, col):
            cur = con.cursor()
            cur.execute("select surname from couriers where id_courier =" + str(i) + "")
            result = cur.fetchone()
            couriers.addItems(result)

        cur.execute("select count(id_order) from orders where id_status = 3")
        col = cur.fetchone()[0]
        for i in range(0, col):
            cur.execute("select id_order from orders where id_status = 3")
            rez = cur.fetchall()[i]
            self.ui.comboBox_2.addItem(str(*rez))
        con.commit()
        con.close()


    def courier_order(self):
        now = datetime.now()
        date_delivery = now.strftime("%Y-%m-%d")
        courier = self.ui.comboBox.currentIndex() + 1
        courier_name = self.ui.comboBox.currentText()
        order = self.ui.comboBox_2.currentText()
        remove_order = self.ui.comboBox_2.currentIndex()
        id_delivery = self.id_delivery()
        id_client = self.put_id_client()
        self.ui.plainTextEdit.appendPlainText("Курьер " + courier_name + " назначен на заказ: " + order)
        print(courier, order, id_delivery, id_client, date_delivery)
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("INSERT INTO deliveries (id_delivery, id_courier, id_client, date_delivery, id_order) VALUES (%s, %s, %s, %s, %s)", (id_delivery, courier, id_client, date_delivery, order))
        con.commit()
        cur.execute("UPDATE orders set id_status=4 where id_order= %s", (order,))
        con.commit()
        con.close()
        self.ui.comboBox_2.removeItem(remove_order)

    def put_id_client(self):
        id_order = self.ui.comboBox_2.currentText()
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("select id_client from orders where id_order =" + id_order)
        id_client = cur.fetchone()[0]
        return id_client


    def id_delivery(self):
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("select count(id_delivery) from deliveries")
        id_delivery = cur.fetchone()[0] + 1
        return id_delivery

# Всегда нужна. Не дает окну закрыться при запуске

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Window1()
    myapp.show()
    sys.exit(app.exec_())
