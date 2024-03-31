from scraper import scrape, save_scraped_data


BASE_URL = "https://sales.bcpea.org/properties"
PLOVDIV_QUERY_PARAMS = "court=16&city=3598"
SOFIA_QUERY_PARAMS = "court=28&city=4389"

# Sofia
scraped_properties = scrape(f"{BASE_URL}?{SOFIA_QUERY_PARAMS}")
save_scraped_data(scraped_properties)

# Plovdiv
scraped_properties = scrape(f"{BASE_URL}?{PLOVDIV_QUERY_PARAMS}")
save_scraped_data(scraped_properties)
