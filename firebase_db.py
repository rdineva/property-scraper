import firebase_admin
from firebase_admin import credentials, db
import os
import json
from dotenv import load_dotenv

load_dotenv()

firebase_credentials = json.loads(os.getenv("FIREBASE_CREDENTIALS"))
firebase_admin.initialize_app(credentials.Certificate(firebase_credentials), {
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL")
})

def get_properties():
    return db.reference("/properties")

def save_properties(properties_list):
    ref = get_properties()
    properties_to_save = {}

    for property_obj in properties_list:
        property_key = ref.push().key
        properties_to_save[property_key] = {
            "date": property_obj.date,
            "title": property_obj.title,
            "area": property_obj.area,
            "price": property_obj.price,
            "town": property_obj.town,
            "address": property_obj.address,
            "term": property_obj.term,
            "announcement": property_obj.announcement
        }

    ref.update(properties_to_save)
