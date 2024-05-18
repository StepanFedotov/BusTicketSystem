"""
Файл для тестирования функций классов
Команда для теста: pytest tests/test_functions.py
"""


import json

import sys
sys.path.append(r'D:\Files of programms\Projects\PythonProjects\
                Kolyhmatov\BusTicketSystem')

from Classes.ClientClass import Client

from Classes.RouteClass import Route

from main import Update_Base


def test_Update_Base():
    """
    Функция тестирования функции Update_Base() из main
    """
    #Импорт базы Пользователей и их паролей из файла теста
    test_data = {}
    test_file = r'tests\test_file.txt'
    with open(test_file, 'w+') as file:
        json.dump(test_data, file)
    #Создаем проверочные данные и вызываем проверяемую функцию
    test_data = {'test': 'test'}
    Update_Base(test_file, test_data)
    #Проверяем, что запись в файл выполнена корректно
    with open(test_file, 'r') as file:
        response = json.load(file)
    
    assert response == test_data, "The contents of the file do not match the"\
                                  " expected value"


def test_Update_Tickets():
    """
    Функция тестирования функции Update_Tickets() из Client
    """
    #Импорт базы Пользователей и информации о них из файла теста
    test_client_base = {}
    test_file = r'tests\client_base.txt'
    with open(test_file, 'r') as file:
        test_client_base = json.load(file)
    #Создаем Клиента для теста
    test_login = "test3"
    test_client = Client(test_login, test_client_base)
    #Меняем информацию о бронированиях и билетах, вызываем функцию
    test_client.reservations = {'test': 'test'}
    test_client.tickets = {'test2': 'test2'}
    #Проверяем, что база данных обновлена корректно
    response = test_client.Update_Tickets(test_client_base)

    assert response[test_login]["reservations"] == {'test': 'test'} and \
           response[test_login]["tickets"] == {'test2': 'test2'}, \
           "The contents of the file do not match the expected value"


def test_Route_Info():
    """
    Функция тестирования функции Route_Info() из Route
    """
    #Импорт базы Рейсов и информации о них из файла теста
    test_route_base = {}
    test_file = r'tests\route_base.txt'
    with open(test_file, 'r') as file:
        test_route_base = json.load(file)
    #Создаем Рейс для теста
    test_route_num = "test"
    test_route = Route(test_route_num, test_route_base)
    #Вызываем функцию и проверяем корректность формирования информации
    response = test_route.Route_Info()    
    result = "Рейс №test, Пункт отправления: test, Пункт назначения: test,"\
             " время отправления: test\n"

    assert response == result, "The route information is incorrect"

