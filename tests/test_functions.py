import json

import sys
sys.path.append(r'D:\Files of programms\Projects\PythonProjects\Kolyhmatov\BusTicketSystem')

from Classes.ClientClass import Client

from Classes.RouteClass import Route

from main import Update_Base

"""
Команды для теста:
D:\Files of programms\Projects\PythonProjects\Kolyhmatov\BusTicketSystem> pytest tests/test_functions.py
"""

def test_Update_Base():
    """

    """
    test_data = {}
    test_file = r'tests\test_file.txt'
    with open(test_file, 'w+') as file:
        json.dump(test_data, file)
    test_data = {'test': 'test'}
    Update_Base(test_file, test_data)
    with open(test_file, 'r') as file:
        response = json.load(file)
    assert response == test_data, "The contents of the file do not match the expected value"

def test_Update_Tickets():
    """

    """
    test_client_base = {}
    test_file = r'tests\client_base.txt'
    with open(test_file, 'r') as file:
        test_client_base = json.load(file)
    test_login = "test3"
    test_client = Client(test_login, test_client_base)
    test_client.reservations = {'test': 'test'}
    test_client.tickets = {'test2': 'test2'}
    response = test_client.Update_Tickets(test_client_base)

    assert response[test_login]["reservations"] == {'test': 'test'} and response[test_login]["tickets"] == {'test2': 'test2'}, "The contents of the file do not match the expected value"

def test_Route_Info():
    """

    """
    test_route_base = {}
    test_file = r'tests\route_base.txt'
    with open(test_file, 'r') as file:
        test_route_base = json.load(file)
    test_route_num = "test"
    test_route = Route(test_route_num, test_route_base)
    result = "Рейс №test, Пункт отправления: test, Пункт назначения: test, время отправления: test\n"
    response = test_route.Route_Info()

    assert response == result, "The route information is incorrect"

