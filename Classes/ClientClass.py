class Client():
    """
    Класс клиента (пассажира)
    """
    def __init__(self, login, client_base):
        """
        Инициализация объекта класса
        """
        self.fio = client_base[login]["fio"]
        self.passport = client_base[login]["passport"]
        self.phone = client_base[login]["phone"]
        self.login = login
        self.reservations = client_base[login]["reservations"]
        self.tickets = client_base[login]["tickets"]
        
        
    def Update_Tickets(self, client_base):
        """
        Обновление информации о билетах и бронированиях
        """
        client_base[self.login]["reservations"] = self.reservations
        client_base[self.login]["tickets"] = self.tickets
        
        return client_base