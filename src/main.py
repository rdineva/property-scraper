from firebase_db import initialize_firebase
from services.scraper_service import scrape
from services.database_service import save_scraped_data
from services.email_service import send_email
from models.property import concatenate_properties
from constants import BASE_PROPERTIES_URL, SOFIA_QUERY_PARAMS, PLOVDIV_QUERY_PARAMS, PER_PAGE_PARAM, NO_PROPERTIES_FOUND_TEXT, SUCCESS_EMAIL_TITLE, NO_PROPERTIES_FOUND_TITLE
from utils.helpers import flatten
import os
from dotenv import load_dotenv

load_dotenv()

RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

def main():
    # Initialize database
    initialize_firebase()

    # Scrape properties
    sofia_scraped = scrape(f"{BASE_PROPERTIES_URL}?{PER_PAGE_PARAM}&{SOFIA_QUERY_PARAMS}")
    plovdiv_scraped = scrape(f"{BASE_PROPERTIES_URL}?{PER_PAGE_PARAM}&{PLOVDIV_QUERY_PARAMS}")
    scraped_properties = flatten([sofia_scraped, plovdiv_scraped])

    # Save the new scraped properties
    new_properties = save_scraped_data(scraped_properties)

    # Send email notification
    if new_properties:
        property_details = concatenate_properties(new_properties)
        send_email(SUCCESS_EMAIL_TITLE, property_details, RECEIVER_EMAIL)
    else:
        send_email(NO_PROPERTIES_FOUND_TITLE, NO_PROPERTIES_FOUND_TEXT, RECEIVER_EMAIL)
        print(NO_PROPERTIES_FOUND_TEXT)

if __name__ == "__main__":
    main()