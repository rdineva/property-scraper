import requests
from bs4 import BeautifulSoup
from typing import List
from models.property import Property


def scrape(url: str) -> List[Property]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    new_properties = []
    items = soup.find_all(class_="item__group")

    for item in items:
        new_property = get_property_data(item)
        new_properties.append(new_property)

    return new_properties


def get_property_data(item: str) -> Property:
    date = item.find(class_="date").text.strip()
    title = item.find(class_="title").text.strip()
    area = item.find(class_="category").text.strip()
    price = item.find(class_="price").text.strip()

    labels = item.find_all(class_="label")
    infos = item.find_all(class_="info")

    link = item.find("a", href=True)["href"]

    town = address = term = announcement = ""

    for label, info in zip(labels, infos):
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

    return Property(date, title, area, price, town, address, term, announcement, link)
