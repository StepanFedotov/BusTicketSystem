class Route():
    """
    Класс Рейса
    """
    def __init__(self, route, route_base):
        """
        Инициализация объекта класса
        """
        self.route = route
        self.depart_point = route_base[route]["depart_point"]
        self.destin_point = route_base[route]["destin_point"]
        self.depart_time = route_base[route]["depart_time"]
        self.ticket_price = route_base[route]["ticket_price"]
        self.seats = route_base[route]["seats"]

    def Route_Info(self):
        """
        Функция получения информации о рейсе
        """
        info_str = "Рейс №" + self.route + ", Пункт отправления: " \
                   + self.depart_point + ", Пункт назначения: " \
                   + self.destin_point + ", время отправления: " \
                   + self.depart_time + "\n"
        return(info_str)