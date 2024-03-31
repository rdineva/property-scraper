import requests
from bs4 import BeautifulSoup
from firebase_db import save_property, get_properties
from property import Property
from dotenv import load_dotenv
import os


load_dotenv()

url = "https://sales.bcpea.org/properties?perpage=2000"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

new_properties = []
items = soup.find_all(class_="item__group")

for item in items:
    date = item.find(class_="date").text.strip()
    title = item.find(class_="title").text.strip()
    area = item.find(class_="category").text.strip()
    price = item.find(class_="price").text.strip()

    labels = item.find_all(class_="label")
    infos = item.find_all(class_="info")

    link = item.find("a", href=True)["href"]

    town = address = term = announcement = ""

    for index, (label, info) in enumerate(zip(labels, infos)):
        key = label.text.strip()
        value = info.text.strip()

        if "НАСЕЛЕНО МЯСТО" in key:
            town = value
        elif "Адрес" in key:
            address = value
        elif "СРОК" in key:
            term = value
        elif "ОБЯВЯВАНЕ НА" in key:
            announcement = value


    property = Property(date, title, area, price, town, address, term, announcement, link)
    new_properties.append(property)

ref = get_properties()

for property in new_properties:
    same_properties = ref.order_by_child("link").equal_to(property.link).get()
    if not same_properties:
        save_property(property)
