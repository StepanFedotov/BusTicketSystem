from Classes.ClientClass import Client

from Classes.RouteClass import Route

import json

from PyQt5 import QtWidgets
from PyQt5.Qt import *

import sys
  

#Импорт базы Рейсов и информации о них
route_base = {}
with open('route_base.txt', 'r') as file:
    route_base = json.load(file)

def Update_Route_Base():
    """
    Функция обновления базы Рейсов и информации о них
    """
    with open('route_base.txt', 'w+') as file:
        json.dump(route_base, file)


#Импорт базы Пользователей и информации о них
client_base = {}
with open('client_base.txt', 'r') as file:
    client_base = json.load(file)

def Update_Client_Base():
    """
    Функция обновления базы Пользователей и информации о них
    """
    with open('client_base.txt', 'w+') as file:
        json.dump(client_base, file)

                                                                                
#Импорт базы Пользователей и их паролей из файла
pwd_dictionary = {}
with open('pwd_dictionary.txt', 'r') as file:
    pwd_dictionary = json.load(file)

def Update_PWD():
    """
    Функция обновления базы Пользователей и паролей
    """
    with open('pwd_dictionary.txt', 'w+') as file:
        json.dump(pwd_dictionary, file)


class SigninPage(QDialog):
    """
    Класс окна регистрации
    """
    def __init__(self):
        """
        Инициализация через конструктор класса QDialog, добавление элементов
        """
        super(SigninPage, self).__init__()
        self.signin_user_label = QLabel('E-mail:')
        self.signin_pwd_label = QLabel('Password:')
        self.signin_pwd2_label = QLabel('Password:')
        self.signin_fio_label = QLabel('Ваше ФИО:')
        self.signin_passport_label = QLabel('Паспортные данные:')
        self.signin_phone_label = QLabel('Номер телефона:')
        
        self.signin_user_line = QLineEdit()
        self.signin_pwd_line = QLineEdit()
        self.signin_pwd2_line = QLineEdit()
        self.signin_fio_line = QLineEdit()
        self.signin_passport_line = QLineEdit()
        self.signin_phone_line = QLineEdit()
        self.signin_button = QPushButton('Sign in')

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
        self.fio_h_layout = QHBoxLayout()
        self.passport_h_layout = QHBoxLayout()
        self.phone_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()

    
    def layout_init(self):
        """
        Функция инициализации слоя - добавления виджетов
        """
        self.user_h_layout.addWidget(self.signin_user_label)
        self.user_h_layout.addWidget(self.signin_user_line)
        self.pwd_h_layout.addWidget(self.signin_pwd_label)
        self.pwd_h_layout.addWidget(self.signin_pwd_line)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_label)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_line)
        self.fio_h_layout.addWidget(self.signin_fio_label)
        self.fio_h_layout.addWidget(self.signin_fio_line)
        self.passport_h_layout.addWidget(self.signin_passport_label)
        self.passport_h_layout.addWidget(self.signin_passport_line)
        self.phone_h_layout.addWidget(self.signin_phone_label)
        self.phone_h_layout.addWidget(self.signin_phone_line)

        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addLayout(self.fio_h_layout)
        self.all_v_layout.addLayout(self.passport_h_layout)
        self.all_v_layout.addLayout(self.phone_h_layout)
        self.all_v_layout.addWidget(self.signin_button)

        self.setLayout(self.all_v_layout)

     
    def lineedit_init(self):
        """
        Функция инициализации поля ввода, подключения функции активности
        кнопки signin_button
        """
        self.signin_pwd_line.setEchoMode(QLineEdit.Password)
        self.signin_pwd2_line.setEchoMode(QLineEdit.Password)

        self.signin_user_line.textChanged.connect(self.check_input_func)
        self.signin_pwd_line.textChanged.connect(self.check_input_func)
        self.signin_pwd2_line.textChanged.connect(self.check_input_func)
        self.signin_fio_line.textChanged.connect(self.check_input_func)
        self.signin_passport_line.textChanged.connect(self.check_input_func)
        self.signin_phone_line.textChanged.connect(self.check_input_func)
    
    
    def pushbutton_init(self):
        """
        Функция инициализации кнопки signin_button, подключения хэндлера
        """
        self.signin_button.setEnabled(False)
        self.signin_button.clicked.connect(self.check_signin_func)

    
    def check_input_func(self):
        """
        Функция контроля активности кнопки signin_button
        """
        if self.signin_user_line.text() and \
            self.signin_pwd_line.text() and \
            self.signin_pwd2_line.text() and \
            self.signin_fio_line.text() and \
            self.signin_passport_line.text() and \
            self.signin_phone_line.text():
            self.signin_button.setEnabled(True)
        else:
            self.signin_button.setEnabled(False)

    
    def check_signin_func(self):
        """
        Функция хэндлер нажатия на кнопку signin_button
        """
        if self.signin_pwd_line.text() != self.signin_pwd2_line.text():
            QMessageBox.critical(self, 'Wrong', 'Two Passwords Typed Are Not'\
                                                'Same!')
        elif self.signin_user_line.text() not in pwd_dictionary:
            pwd_dictionary[self.signin_user_line.text()] = self\
                               .signin_pwd_line.text()
            client_base[self.signin_user_line.text()] = {
                            "fio": self.signin_fio_line.text(),
                            "passport": self.signin_passport_line.text(),
                            "phone": self.signin_phone_line.text(),
                            "reservations": {},
                            "tickets": {}
                            }
            QMessageBox.information(self, 'Info', 'Register Successfully')
            self.close()
            Update_PWD()
            Update_Client_Base()
        else:
            QMessageBox.critical(self, 'Wrong', 'This Username Has Been'\
                                                ' Registered!')

        self.signin_user_line.clear()
        self.signin_pwd_line.clear()
        self.signin_pwd2_line.clear()


class WindowAdmin(QtWidgets.QMainWindow):
    """
    Класс окна Администратора
    """
    def __init__(self, name):
        """
        Инициализация через конструктор класса QMainWindow, добавление
        элементов
        """
        super().__init__()
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        
        self.label = QtWidgets.QLabel(f'<h1>Привет, {name}!</h1>', 
                                      alignment=Qt.AlignCenter)
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


class Pay_Window(QDialog):
    """
    Класс окна Оплаты
    """
    def __init__(self, client):
        """
        Инициализация через конструктор класса QDialog, добавление элементов
        """
        super(Pay_Window, self).__init__()
        self.client = client
        reserv = list(client.reservations.items())
        reserv_str = "\n"
        for each in reserv:
            reserv_str += f"Рейс №{each[0]} Место №{each[1]}\n"
        self.paywin_reserv_label = QLabel('У вас есть следующие '\
                                          'неоплаченные бронирования: ' \
                                          + reserv_str)
        reserv = list(self.client.reservations.items())
        cost = 0
        for each in reserv:
            route = Route(each[0],route_base)
            cost += route.ticket_price
        self.paywin_cost_label = QLabel(f'Общая стоимость: {cost}$')
        self.pay_button = QPushButton('Оплатить')
            
        self.all_v_layout = QVBoxLayout()
        
        self.pushbutton_init()
        self.layout_init()
        
        
    def layout_init(self):
        """
        Функция инициализации слоя - добавления виджетов
        """
        self.all_v_layout.addWidget(self.paywin_reserv_label)
        self.all_v_layout.addWidget(self.paywin_cost_label)
        self.all_v_layout.addWidget(self.pay_button)
        
        self.setLayout(self.all_v_layout)
       
        
    def pushbutton_init(self):
        """
        Функция инициализации кнопки pay_button, подключения хэндлера
        """
        self.pay_button.clicked.connect(self.check_pay_func)
        

    def check_pay_func(self):
        """
        Функция хэндлер нажатия на кнопку pay_button
        """
        QMessageBox.information(self, 'Info', 'Оплата прошла успешно!')
        self.client.tickets.update(self.client.reservations)
        self.client.reservations = {}
        global client_base
        client_base = self.client.Update_Tickets(client_base)
        Update_Client_Base()
        self.close()

        
class WindowUser(QDialog):
    """
    Класс окна Пользователя
    """
    def __init__(self, client):
        """
        Инициализация через конструктор класса QDialog, добавление элементов
        """
        super(WindowUser, self).__init__()
        self.client = client
        self.winuser_welcome_label = QLabel('Добро пожаловать, ' + client.fio)
        self.winuser_login_label = QLabel('Вы зашли под login: ' \
                                          + client.login)
        self.winuser_phone_label = QLabel('Привязанный номер телефона: ' \
                                        + client.phone)
        self.winuser_passport_label = QLabel('Паспортные данные : ' \
                                             + client.passport)
        reserv = list(client.reservations.items())
        reserv_str = "\n"
        for each in reserv:
            reserv_str += f"Рейс №{each[0]} Место №{each[1]}\n"
        self.winuser_reserv_label = QLabel('У вас есть следующие '\
                                           'неоплаченные бронирования: ' \
                                           + reserv_str)
        tickets = list(client.tickets.items())
        tickets_str = "\n"
        for each in tickets:
            tickets_str += f"Рейс №{each[0]} Место №{each[1]}\n"
        self.winuser_tickets_label = QLabel('У вас есть следующие '\
                                            'билеты: ' \
                                            + tickets_str)
        self.route_info_button = QPushButton('Информация о моих рейсах')
        self.resrv_pay_button = QPushButton('Оплатить бронирования')
            
        self.buttons_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()
        
        self.pushbutton_init()
        self.layout_init()
        
        
    def layout_init(self):
        """
        Функция инициализации слоя - добавления виджетов
        """
        self.buttons_h_layout.addWidget(self.route_info_button)
        self.buttons_h_layout.addWidget(self.resrv_pay_button)
        
        self.all_v_layout.addWidget(self.winuser_welcome_label)
        self.all_v_layout.addWidget(self.winuser_login_label)
        self.all_v_layout.addWidget(self.winuser_phone_label)
        self.all_v_layout.addWidget(self.winuser_passport_label)
        self.all_v_layout.addWidget(self.winuser_reserv_label)
        self.all_v_layout.addWidget(self.winuser_tickets_label)
        self.all_v_layout.addLayout(self.buttons_h_layout)
        
        self.setLayout(self.all_v_layout)
       
        
    def pushbutton_init(self):
        """
        Функция инициализации кнопки route_info_button, подключения хэндлера
        """
        self.route_info_button.clicked.connect(self.check_route_info_func)
        self.resrv_pay_button.clicked.connect(self.check_reserv_pay_func)


    def check_route_info_func(self):
        """
        Функция хэндлер нажатия на кнопку route_info_button
        """
        if self.client.reservations == {} and self.client.tickets == {}:
            QMessageBox.critical(self, 'Wrong', 'У вас нет бронирований'\
                                                ' или купленных билетов!')
        else:
            reserv = list(self.client.reservations.items())
            info_str = "Ваши рейсы:\n"
            for each in reserv:
                route = Route(each[0],route_base)
                info_str += route.Route_Info()
            tickets = list(self.client.tickets.items())
            for each in tickets:
                route = Route(each[0],route_base)
                info_str += route.Route_Info()
            QMessageBox.information(self, 'Информация о рейсах', info_str)
            

    def check_reserv_pay_func(self):
        """
        Функция хэндлер нажатия на кнопку reserv_pay_button
        """
        if self.client.reservations == {}:
            QMessageBox.critical(self, 'Wrong', 'У вас нет бронирований')
        else:
            self.paywin = Pay_Window(self.client)
            self.paywin.exec_()
            self.close()
            

class Login(QWidget):
    """
    Класс окна Авторизации
    """
    def __init__(self):
        """
        Инициализация через конструктор класса QWidget, добавление элементов
        """
        super(Login, self).__init__()
        self.resize(300, 100)

        self.user_label = QLabel('E-mail address:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.user_line.setClearButtonEnabled(True)
        self.pwd_line = QLineEdit(self)
        self.pwd_line.setClearButtonEnabled(True)
        self.login_button = QPushButton('Войти', self)
        self.signin_button = QPushButton('Зарегистрироватся', self)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()
        self.signin_page = SigninPage()            

    
    def layout_init(self):
        """
        Функция инициализации слоя - добавления виджетов
        """
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    
    def lineedit_init(self):
        """
        Функция инициализации поля ввода, подключения функции активности
        кнопки login_button
        """
        self.user_line.setPlaceholderText('Please enter your email')
        self.pwd_line.setPlaceholderText('Please enter your password')
        self.pwd_line.setEchoMode(QLineEdit.Password)

        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

    
    def pushbutton_init(self):
        """
        Функция инициализации кнопок, подключения хэндлера
        """
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self.check_login_func)
        self.signin_button.clicked.connect(self.show_signin_page_func)

    
    def check_login_func(self):
        """
        Функция хэндлер нажатия на кнопку login_button
        """
        password = pwd_dictionary.get(self.user_line.text())
        if password != self.pwd_line.text():
            QMessageBox.critical(self, 'Wrong', 'Wrong Username or Password!')
            return
        
        user = self.user_line.text()
        self.user_line.clear()
        self.pwd_line.clear()
        if user == 'admin@gmail.com':
            self.windowAdmin = WindowAdmin(user)
            self.windowAdmin.exec_()
        else:
            client = Client(user, client_base)
            self.windowUser = WindowUser(client)
            self.windowUser.exec_()   

    
    def show_signin_page_func(self):
        """
        Функция хэндлер нажатия на кнопку signin_button
        """
        self.signin_page.exec_()

    
    def check_input_func(self):
        """
        Функция контроля активности кнопки login_button
        """
        if self.user_line.text() and self.pwd_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

#Основной процесс программы
if __name__ == '__main__':
    #Создание приложения
    app = QApplication(sys.argv)
    #Создание и открытие окна авторизации
    start_window = Login()
    start_window.show()
    #Остановка выполнения
    sys.exit(app.exec_())
    