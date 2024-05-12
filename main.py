import json

from PyQt5 import QtWidgets
from PyQt5.Qt import *

import sys
  
                                                                                
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
        self.signin_user_line = QLineEdit()
        self.signin_pwd_line = QLineEdit()
        self.signin_pwd2_line = QLineEdit()
        self.signin_button = QPushButton('Sign in')

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
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

        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
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
           self.signin_pwd2_line.text():
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
            QMessageBox.information(self, 'Info', 'Register Successfully')
            self.close()
            Update_PWD()
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

        
class WindowUser(QtWidgets.QMainWindow):
    """
    Класс окна Пользователя
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
        
        user = self.user_line.text().split('@')[0]
        if user == 'admin':
            self.windowAdmin = WindowAdmin(user)
            self.windowAdmin.show()
        else:
            self.windowUser = WindowUser(user)
            self.windowUser.show()
            
        self.close()   

    
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
    