import firebase_admin
from firebase_admin import credentials, db
from typing import List
import json
import os
from models.property import Property

def initialize_firebase():
    firebase_credentials = json.loads(os.getenv("FIREBASE_CREDENTIALS"))
    firebase_admin.initialize_app(credentials.Certificate(firebase_credentials), {
        "databaseURL": os.getenv("FIREBASE_DATABASE_URL")
    })

def get_properties() -> db.Reference:
    return db.reference("/properties")

def save_properties(properties: List[Property]):
    ref = get_properties()
    batch_update = {}

    for property in properties:
        property_key = ref.push().key
        batch_update[property_key] = {
            "date": property.date,
            "title": property.title,
            "area": property.area,
            "price": property.price,
            "town": property.town,
            "address": property.address,
            "term": property.term,
            "announcement": property.announcement,
            "link": property.link,
        }

    if len(batch_update) > 0:
        try:
            ref.update(batch_update)
        except Exception as e:
            raise Exception(f"Failed to save to Firebase: {e}")