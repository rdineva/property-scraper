import requests
from bs4 import BeautifulSoup
from firebase_db import save_properties, get_properties
from property import Property
from typing import List


def scrape(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    new_properties = []
    items = soup.find_all(class_="item__group")

    for item in items:
        new_property = get_property_data(item)
        new_properties.append(new_property)

    return new_properties


def get_property_data(item: str):
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
    return property


def save_scraped_data(scraped_properties: List[Property]):
    ref = get_properties()

    new_properties = []
    for property in scraped_properties:
        same_properties = ref.order_by_child("link").equal_to(property.link).get()

        if not same_properties:
            new_properties.append(property)

    save_properties(new_properties)
    return new_properties
