from typing import List
from models.property import Property
from firebase_db import get_properties, save_properties

def save_scraped_data(scraped_properties: List[Property]):
    ref = get_properties()
    new_properties = []

    for property in scraped_properties:
        same_properties = ref.order_by_child("link").equal_to(property.link).get()
        if not same_properties:
            new_properties.append(property)

    save_properties(new_properties)
    return new_properties