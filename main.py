import requests
from bs4 import BeautifulSoup
from firebase_db import save_property
from property import Property
from dotenv import load_dotenv
import os


load_dotenv()

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

    link = item.find('a', href=True)['href']

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


    property = Property(date, title, area, price, town, address, term, announcement, link)
    properties.append(property)

for property in properties:
    print(property)
    save_property(property)
    print("-" * 50)