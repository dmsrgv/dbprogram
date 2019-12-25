# Created by Dmitry Sergeev, Maria Stepanova
# All rights reserved

# Библиотеки
from datetime import datetime, timedelta
import sys
import random
import psycopg2
import hashlib
# Импортируем наш интерфейс
from couriers import *
from design import *
from registration import *
from test import *
from zakaz import *
from admins import *
from logists import *
from supervisors import *
from requisites import *
from passport import *
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QAction
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator

id_lol = 0
name_users = ""


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
        self.ui.pushButton_2.clicked.connect(self.show_registration)
        self.ui.pushButton.clicked.connect(self.login_enter)
        self.ui.pushButton_3.clicked.connect(self.window_couriers)

        # Вход

    def login_enter(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        global name_users
        name_users = username
        pasw = password + username
        h = hashlib.md5(pasw.encode())
        pasw = h.hexdigest() + "deliveryfood"
        h = hashlib.md5(pasw.encode())
        pasw = "md5" + h.hexdigest()
        con = self.connect_bd()
        cur = con.cursor()
        cur.execute("select exists (select passwd from pg_shadow where usename = %s)", (username,))
        true = cur.fetchone()[0]
        if true:
            cur.execute("select passwd from pg_shadow where usename = %s", (username,))
            passw = cur.fetchone()[0]
            if passw == pasw:
                try:
                    con = self.connect_bd()
                    cur = con.cursor()
                    cur.execute("select * from information_schema.applicable_roles WHERE grantee =" + "'" + username + "'")
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
            else:
                self.ui.label.setText("НЕ УСПЕХ")
        else:
            self.ui.label.setText("НЕ УСПЕХ")

        # try:
        #     con = psycopg2.connect(
        #         database="DeliveryFood",
        #         user=username,
        #         password=password,
        #         host="127.0.0.1",
        #         port="5432"
        #     )
        #     cur = con.cursor()
        #     cur.execute(
        #         "select * from information_schema.applicable_roles WHERE grantee =" + "'" + username + "'")
        #     role = cur.fetchone()[1]
        #     if role == "clients":
        #         self.window_clients()
        #     elif role == "supervisors":
        #         self.window_supervisors()
        #     elif role == "admins":
        #         self.window_admins()
        #     elif role == "logists":
        #         self.window_logists()
        #     self.ui.label.setText("УСПЕХ")
        #     return con
        # except psycopg2.DatabaseError:
        #     self.ui.label.setText("НЕ УСПЕХ")

        # Покажем окно регистрации

    def show_registration(self):
        self.w = Registration()
        self.w.show()

        # Вызов окна курьеров

    def window_couriers(self):
        self.w = Window_couriers()
        self.w.show()
        self.close()

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

        # Метод подключения к бд

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
        try:
            username = self.ui.lineEdit_2.text()
            password = self.ui.lineEdit_3.text()
            con = Window1().connect_bd()
            cur = con.cursor()
            cur.execute(
                "CREATE USER " + self.ui.lineEdit_2.text() + " WITH PASSWORD " + "'" + self.ui.lineEdit_3.text() + "'")
            cur.execute("SELECT make_pass(%s, %s, 'deliveryfood')", (password, username))
            make_password = cur.fetchone()[0]
            cur.execute("ALTER ROLE " + username + " WITH PASSWORD " + "'" + make_password + "'")
            con.commit()
            con.commit()
            cur.execute("GRANT clients TO " + self.ui.lineEdit_2.text())

            con.commit()
            con.close()
            self.close()
        except psycopg2.DatabaseError:
            print("Ошибка")

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
        self.ui.label_16.setText("Привет, " + str(name_users) + "!")
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
        # sum_prize = sum_prize + prize
        prize = prize.replace(" ₽", "")
        prize = prize.replace(",", ".")
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
        discount_percent = self.discount_percent()
        sum_prize = self.sum_prize
        sum_prize = sum_prize * (1 - discount_percent / 100)
        self.ui.plainTextEdit.setPlainText("Номер вашего заказа: " + str(id_order))
        self.ui.plainTextEdit.appendPlainText("Время заказа:   " + str(ordered_in))
        self.ui.plainTextEdit.appendPlainText("Время доставки: " + str(deliver_in))
        self.ui.plainTextEdit.appendPlainText("СКИДКА: " + str(discount_percent) + "%")
        self.ui.plainTextEdit.appendPlainText("Сумма к оплате: " + str(sum_prize) + " рублей")
        kek = self.ui.plainTextEdit_3.toPlainText().split('\n')

        cur.execute(
            "INSERT INTO orders (id_order,id_type_payments,id_status,deliver_in,id_restaurant, id_client, id_discount, ordered_in, prize) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (id_order, id_type_payments, id_status, deliver_in, id_restaurant, id_client, id_discount, ordered_in,
             sum_prize))
        con.commit()

        for i in range(len(kek)):
            dish = kek[i]
            cur.execute("SELECT id_dish from dishes where name_dish = %s",(dish,))
            id_blud = cur.fetchone()[0]
            cur.execute("SELECT count(number_dishes) from dishes_in_order")
            count_dishes = cur.fetchone()[0] + 1
            cur.execute("INSERT INTO dishes_in_order (number_dishes, id_order, dish) VALUES (%s, %s, %s)", (count_dishes, id_order, id_blud))
            con.commit()
        # Узнаем скидку

    def discount_percent(self):
        id_discount = self.check_id_discount()
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("select percent_discount from system_discount where id_discount = %s", (id_discount,))
        percent_discount = cur.fetchone()[0]
        return percent_discount

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
            cur.execute(
                "SELECT name_dish,prize_dish from dishes WHERE id_restaurant =" + str(
                    col) + "")
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


# Окно для админов

class Window_admins(QMainWindow):
    def __init__(self):
        super(Window_admins, self).__init__()
        self.ui = Ui_Admins()
        self.ui.setupUi(self)
        self.setWindowTitle('Admins Form')
        self.ui.pushButton_3.clicked.connect(self.sql_query)
        self.ui.pushButton_2.clicked.connect(self.user_role)
        self.ui.pushButton_4.clicked.connect(self.user_info)
        users = self.ui.comboBox
        roles = self.ui.comboBox_2
        roles.addItems(["clients", "admins", "supervisors", "couriers", "logists"])
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("Select count(grantee) from information_schema.applicable_roles")
        result = cur.fetchone()
        col = int(result[0])
        con.commit()
        try:
            for i in range(3, col):
                cur = con.cursor()
                cur.execute("select grantee from information_schema.applicable_roles")
                result = cur.fetchall()[i]
                users.addItems(result)
        except psycopg2.DatabaseError:
            print("Ошибка")

    def user_role(self):
        next_role = self.ui.comboBox_2.currentText()
        self.ui.plainTextEdit_2.setPlainText("")
        try:
            con = Window1().connect_bd()
            cur = con.cursor()
            grantee = self.ui.comboBox.currentText()
            cur.execute(
                "select role_name from information_schema.applicable_roles where grantee =" + "'" + grantee + "'")
            last_role = cur.fetchone()[0]
            cur.execute("REVOKE " + last_role + " FROM " + grantee + ";")
            con.commit()
            cur.execute("GRANT " + next_role + " TO " + grantee + ";")
            con.commit()
            self.ui.label_5.setText("Выполнено: " + str(last_role) + " ->" + str(next_role))
        except psycopg2.DatabaseError:
            print("Ошибка")
        # cur.execute("GRANT %s TO %s", (next_role, grantee))

    # con.commit()

    def user_info(self):
        try:
            con = Window1().connect_bd()
            cur = con.cursor()
            grantee = self.ui.comboBox.currentText()
            cur.execute(
                "select role_name from information_schema.applicable_roles where grantee =" + "'" + grantee + "'")
            last_role = cur.fetchone()[0]
            self.ui.plainTextEdit_2.setPlainText("")
            self.ui.plainTextEdit_2.appendPlainText("Роль " + grantee + " = " + last_role)
        except psycopg2.DatabaseError:
            self.ui.plainTextEdit_2.appendPlainText("У " + grantee + "нет роли")

    def sql_query(self):
        try:
            con = Window1().connect_bd()
            cur = con.cursor()
            cur.execute(self.ui.plainTextEdit.toPlainText())
            con.commit()
            con.close()
            self.ui.label_7.setText("Запрос выполнен.")
        except psycopg2.DatabaseError:
            print("Ошибка")
            self.ui.label_7.setText("Ошибка. Запрос не выполнен.")


# Окно для супервайзеров
class Window_supervisors(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Supervisors()
        self.ui.setupUi(self)
        self.setWindowTitle('Supervisors Form')
        self.ui.pushButton_3.clicked.connect(self.add_courier)
        self.ui.pushButton_2.clicked.connect(self.info_courier)
        self.ui.pushButton.clicked.connect(self.show_passport)
        self.ui.pushButton_4.clicked.connect(self.show_requisites)
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.label_16.setText(str(name_users))
        couriers = self.ui.comboBox
        service = self.ui.comboBox_2
        type = self.ui.comboBox_3
        con = Window1().connect_bd()
        cur = con.cursor()
        # Все курьеры
        cur.execute("SELECT COUNT(ID_courier) from couriers")
        result = cur.fetchone()
        col = int(result[0]) + 1
        con.commit()
        for i in range(1, col):
            cur = con.cursor()
            cur.execute("select surname from couriers where id_courier =" + str(i) + "")
            result = cur.fetchone()
            couriers.addItems(result)
        # Курьерская служба
        cur.execute("SELECT COUNT(id_courier_service) from courier_service")
        result = cur.fetchone()
        col = int(result[0]) + 1
        con.commit()
        for i in range(1, col):
            cur = con.cursor()
            cur.execute("select name_courier_service from courier_service where id_courier_service =" + str(i) + "")
            result = cur.fetchone()
            service.addItems(result)
        # Тип курьера
        for i in range(1, 4):
            cur = con.cursor()
            cur.execute("select name_type from type_courier where id_type =" + str(i) + "")
            result = cur.fetchone()
            type.addItems(result)

    def show_passport(self):
        self.w = Passport()
        self.w.show()

    def show_requisites(self):
        self.w = Requisites()
        self.w.show()

    def info_courier(self):
        name_courier = self.ui.comboBox.currentText()
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("SELECT id_courier from couriers where surname = %s", (name_courier,))
        id = cur.fetchone()[0]
        self.ui.plainTextEdit.appendPlainText("ID курьера: " + str(id))
        cur.execute("SELECT name from couriers where surname = %s", (name_courier,))
        name = cur.fetchone()[0]
        self.ui.plainTextEdit.appendPlainText("Имя:         " + name)
        self.ui.plainTextEdit.appendPlainText("Фамилия:     " + name_courier)
        cur.execute("SELECT phone from couriers where surname = %s", (name_courier,))
        phone = cur.fetchone()[0]
        self.ui.plainTextEdit.appendPlainText("Телефон:      " + phone)
        cur.execute("SELECT birthday from couriers where surname = %s", (name_courier,))
        birthday = cur.fetchone()[0]
        self.ui.plainTextEdit.appendPlainText("День рождения: " + str(birthday))
        cur.execute("SELECT passport from couriers where surname = %s", (name_courier,))
        passport = cur.fetchone()[0]
        self.ui.plainTextEdit.appendPlainText("Паспорт:       " + str(passport))
        cur.execute("SELECT date_activation from couriers where surname = %s", (name_courier,))
        date_activation = cur.fetchone()[0]
        self.ui.plainTextEdit.appendPlainText("Дата активации:       " + str(date_activation))
        cur.execute("SELECT bank_account from couriers where surname = %s", (name_courier,))
        bank_account = cur.fetchone()[0]
        self.ui.plainTextEdit.appendPlainText("Номер счёта: " + str(bank_account))
        self.ui.plainTextEdit.appendPlainText("-------------------------------------")
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_4.setEnabled(True)
        global id_lol
        id_lol = id
        return id

    def add_courier(self):
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("SELECT COUNT(ID_courier) from couriers")
        result = cur.fetchone()
        id_courier = int(result[0]) + 1
        id_status_courier = 1
        id_type = self.ui.comboBox_3.currentIndex() + 1
        id_service = self.ui.comboBox_2.currentIndex() + 1
        name = self.ui.lineEdit_2.text()
        surname = self.ui.lineEdit_3.text()
        second_name = self.ui.lineEdit_4.text()
        phone = self.ui.lineEdit_5.text()
        dr = self.ui.lineEdit_6.text()
        now = datetime.now()
        date_activation = now.strftime("%Y-%m-%d")
        size_password = 8
        passport = self.ui.lineEdit_7.text()
        bank_account = self.ui.lineEdit_8.text()
        chars_password = "abcdefghijklnopqrstuvwxyz1234567890"
        password = ""
        for i in range(size_password):
            password += random.choice(chars_password)
        cur.execute(
            "INSERT INTO couriers (id_courier, id_courier_service, id_type_courier, id_status_courier, surname, name, second_name, phone, birthday, passport, date_activation, bank_account) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                id_courier, id_service, id_type, id_status_courier, surname, name, second_name, phone, dr, passport,
                date_activation, bank_account))
        con.commit()
        cur.execute("INSERT INTO couriers_password (id_courier, password) VALUES (%s, %s)", (id_courier, password))
        con.commit()
        con.close()
        self.ui.label_11.setText("ID: " + str(id_courier))
        self.ui.label_12.setText("PASSWORD: " + str(password))


# Окно для логистов
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
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO deliveries (id_delivery, id_courier, id_client, date_delivery, id_order) VALUES (%s, %s, %s, %s, %s)",
            (id_delivery, courier, id_client, date_delivery, order))
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


class Window_couriers(QMainWindow):
    def __init__(self):
        super(Window_couriers, self).__init__()
        self.ui = Ui_Couriers()
        self.ui.setupUi(self)
        self.setWindowTitle('Couriers Form')
        self.ui.pushButton_4.clicked.connect(self.opr_login)
        self.ui.tableWidget.setVisible(False)
        self.ui.label_4.setText("")
        self.ui.pushButton_5.setVisible(False)
        self.ui.pushButton_5.clicked.connect(self.delivery)
        self.ui.tableWidget.clicked.connect(self.click_table_couriers)
        self.resize(257, 163)

    def click_table_couriers(self):
        row = self.ui.tableWidget.currentRow()
        col = 0
        value = self.ui.tableWidget.item(row, col).text()
        return value

    def delivery(self):
        id = self.ui.lineEdit.text()
        value = self.click_table_couriers()
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("UPDATE orders set id_status=1 where id_order= %s", (value,))
        con.commit()
        self.ui.tableWidget.setRowCount(0)
        cur.execute(
            "SELECT orders.id_order, clients.name_client, clients.address_client, clients.phone_client, clients.comment_client, orders.deliver_in, orders.ordered_in, type_payments.name_type_payments, orders.prize from orders, deliveries, clients, type_payments where orders.id_order = deliveries.id_order and orders.id_client = clients.id_client and orders.id_type_payments = type_payments.id_type_payments and deliveries.id_courier = %s and orders.id_status = 4",
            (id,))
        result = cur.fetchall()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["Номер заказа", "Имя клиента", "Адрес клиента", "Телефон", "Комментарий", "Доставить к", "Заказано в",
             "Тип оплаты", "Цена"])
        self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.ui.tableWidget.sizeHintForColumn(9)
        self.ui.tableWidget.resizeColumnsToContents()

        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.ui.tableWidget.resizeColumnsToContents()

    def opr_login(self):
        id = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        try:
            con = Window1().connect_bd()
            cur = con.cursor()
            cur.execute(
                "SELECT EXISTS(SELECT id_courier FROM couriers_password WHERE id_courier = %s and password = %s)",
                (id, password))
            true = cur.fetchone()[0]
            con.close()

            if true:
                self.resize(710, 638)
                self.ui.tableWidget.setVisible(True)
                self.ui.label_4.setText("Ваши заказы:")
                self.ui.pushButton_5.setVisible(True)
                self.ui.label_5.setText("")
                self.ui.lineEdit.setVisible(False)
                self.ui.lineEdit_2.setVisible(False)
                self.ui.label_3.setText("")
                self.ui.label_2.setText("")
                self.ui.pushButton_4.setVisible(False)
                con = Window1().connect_bd()
                cur = con.cursor()
                cur.execute(
                    "SELECT orders.id_order, clients.name_client, clients.address_client, clients.phone_client, clients.comment_client, orders.deliver_in, orders.ordered_in, type_payments.name_type_payments, orders.prize from orders, deliveries, clients, type_payments where orders.id_order = deliveries.id_order and orders.id_client = clients.id_client and orders.id_type_payments = type_payments.id_type_payments and deliveries.id_courier = %s and orders.id_status = 4",
                    (id,))
                result = cur.fetchall()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(9)
                self.ui.tableWidget.setHorizontalHeaderLabels(
                    ["Номер заказа", "Имя клиента", "Адрес клиента", "Телефон", "Комментарий", "Доставить к",
                     "Заказано в", "Тип оплаты", "Цена"])
                self.ui.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
                self.ui.tableWidget.sizeHintForColumn(9)
                self.ui.tableWidget.resizeColumnsToContents()

                for row_number, row_data in enumerate(result):
                    self.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.tableWidget.resizeColumnsToContents()
                cur.execute("SELECT name from couriers where id_courier = %s", (id,))
                name = cur.fetchone()[0]
                self.ui.label_6.setText("Привет, " + str(name))

            else:
                self.ui.label_5.setText("Неправильный id или пароль")
        except psycopg2.DatabaseError:
            self.ui.label_5.setText("Неправильный id или пароль")

            # Добавить/обновить данные паспорта


class Passport(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Passport()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.ok_passport)
        self.ui.pushButton_5.clicked.connect(self.not_passport)
        id = id_lol
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("SELECT passport from couriers where id_courier = %s", (id,))
        serial_number = cur.fetchone()[0]
        cur.execute("SELECT place_of_birth from passport_date where serial_number = %s", (serial_number,))
        place_of_birth = cur.fetchone()[0]
        self.ui.lineEdit_2.setText(str(place_of_birth))
        cur.execute("SELECT issued_by_whom from passport_date where serial_number = %s", (serial_number,))
        issued_by_whom = cur.fetchone()[0]
        self.ui.lineEdit_3.setText(str(issued_by_whom))
        cur.execute("SELECT when_issued from passport_date where serial_number = %s", (serial_number,))
        when_issued = cur.fetchone()[0]
        self.ui.lineEdit_4.setText(str(when_issued))
        cur.execute("SELECT unit_code from passport_date where serial_number = %s", (serial_number,))
        unit_code = cur.fetchone()[0]
        self.ui.lineEdit_5.setText(str(unit_code))
        cur.execute("SELECT unit_code from passport_date where serial_number = %s", (serial_number,))
        address_registration = cur.fetchone()[0]
        self.ui.lineEdit_6.setText(str(address_registration))

    def ok_passport(self):
        id = id_lol
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("SELECT passport from couriers where id_courier = %s", (id,))
        serial_number = cur.fetchone()[0]
        new_place_of_birth = self.ui.lineEdit_2.text()
        new_issued_by_whom = self.ui.lineEdit_3.text()
        new_when_issued = self.ui.lineEdit_4.text()
        new_unit_code = self.ui.lineEdit_5.text()
        new_address_registration = self.ui.lineEdit_6.text()
        cur.execute("UPDATE passport_date set place_of_birth = %s where serial_number = %s",
                    (new_place_of_birth, serial_number))
        cur.execute("UPDATE passport_date set issued_by_whom = %s where serial_number = %s",
                    (new_issued_by_whom, serial_number))
        cur.execute("UPDATE passport_date set when_issued = %s where serial_number = %s",
                    (new_when_issued, serial_number))
        cur.execute("UPDATE passport_date set unit_code = %s where serial_number = %s", (new_unit_code, serial_number))
        cur.execute("UPDATE passport_date set address_registration = %s where serial_number = %s",
                    (new_address_registration, serial_number))
        con.commit()
        con.close()
        self.close()

    def not_passport(self):
        self.close()


class Requisites(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_requisites()
        self.ui.setupUi(self)
        id = id_lol
        self.ui.pushButton_4.clicked.connect(self.requisites_ok)
        self.ui.pushButton_5.clicked.connect(self.requisites_cancel)
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("SELECT bank_account from couriers where id_courier = %s", (id,))
        bank_account = cur.fetchone()[0]
        cur.execute("SELECT bik from requisites where number_account = %s", (bank_account,))
        bik = cur.fetchone()[0]
        self.ui.lineEdit_2.setText(str(bik))
        cur.execute("SELECT inn from requisites where number_account = %s", (bank_account,))
        inn = cur.fetchone()[0]
        self.ui.lineEdit_3.setText(str(inn))
        cur.execute("SELECT kpp from requisites where number_account = %s", (bank_account,))
        kpp = cur.fetchone()[0]
        self.ui.lineEdit_4.setText(str(kpp))

    def requisites_ok(self):
        id = id_lol
        con = Window1().connect_bd()
        cur = con.cursor()
        cur.execute("SELECT bank_account from couriers where id_courier = %s", (id,))
        number_account = cur.fetchone()[0]
        new_bik = self.ui.lineEdit_2.text()
        new_inn = self.ui.lineEdit_3.text()
        new_kpp = self.ui.lineEdit_4.text()
        cur.execute("UPDATE requisites set bik = %s where number_account = %s", (new_bik, number_account))
        cur.execute("UPDATE requisites set inn = %s where number_account = %s", (new_inn, number_account))
        cur.execute("UPDATE requisites set kpp = %s where number_account = %s", (new_kpp, number_account))
        self.close()

    def requisites_cancel(self):
        self.close()


# Всегда нужна. Не дает окну закрыться при запуске

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Window1()
    myapp.show()
    sys.exit(app.exec_())
