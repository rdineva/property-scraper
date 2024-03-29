import requests
from bs4 import BeautifulSoup

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
            f"Дата: {date}\n"
            f"Заглавие: {title}\n"
            f"Площ: {area}\n"
            f"Цена: {price}\n"
            f"Населено място: {town}\n"
            f"Адрес: {address}\n"
            f"Срок: {term}\n"
            f"Обявяване на: {announcement}\n"
        )

url = "https://sales.bcpea.org/properties"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

properties = []
items = soup.find_all(class_='item__group')

for item in items:
    date = item.find(class_='date').text.strip()
    title = item.find(class_='title').text.strip()
    area = item.find(class_='category').text.strip()
    price = item.find(class_='price').text.strip()

    labels = item.find_all(class_='label')
    infos = item.find_all(class_='info')

    town = address = term = announcement = ""

    for index, (label, info) in enumerate(zip(labels, infos)):
        key = label.text.strip()
        value = info.text.strip()

        if 'НАСЕЛЕНО МЯСТО' in key:
            town = value
        elif 'Адрес' in key:
            address = value
        elif 'СРОК' in key:
            term = value
        elif 'ОБЯВЯВАНЕ НА' in key:
            announcement = value


    property = Property(date, title, area, price, town, address, term, announcement)
    properties.append(property)

for property in properties:
    print(property)
    print("-" * 50)