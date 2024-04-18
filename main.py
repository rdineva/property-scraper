from scraper import scrape, save_scraped_data
from email_service import send_email
from property import concatenate_properties
from constants import BASE_PROPERTIES_URL, SOFIA_QUERY_PARAMS, PLOVDIV_QUERY_PARAMS, PER_PAGE_PARAM
import os
from dotenv import load_dotenv


load_dotenv()

RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

scraped_properties = []

sofia_scraped = scrape(f"{BASE_PROPERTIES_URL}?{PER_PAGE_PARAM}&{SOFIA_QUERY_PARAMS}")
scraped_properties.append(sofia_scraped)

plovdiv_scraped = scrape(f"{BASE_PROPERTIES_URL}?{PER_PAGE_PARAM}&{PLOVDIV_QUERY_PARAMS}")
scraped_properties.append(plovdiv_scraped)

def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

properties = flatten(scraped_properties)
new_properties = save_scraped_data(properties)

if new_properties:
    property_details = concatenate_properties(new_properties)
    send_email("Нови Имоти от ЧСИ", property_details, RECEIVER_EMAIL)
else:
    send_email("Няма нови имоти", "-", RECEIVER_EMAIL)
    print("Няма нови имоти според зададените критерии!")