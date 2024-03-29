class Property:
    def __init__(self, date, title, area, price, town, address, term, announcement):
        self.date = date
        self.title = title
        self.area = area
        self.price = price
        self.town = town
        self.address = address
        self.term = term
        self.announcement = announcement

    def __str__(self):
        return(
            f"Дата: {self.date}\n"
            f"Заглавие: {self.title}\n"
            f"Площ: {self.area}\n"
            f"Цена: {self.price}\n"
            f"Населено място: {self.town}\n"
            f"Адрес: {self.address}\n"
            f"Срок: {self.term}\n"
            f"Обявяване на: {self.announcement}\n"
        )