# Property Scraper

Web Scraper for scraping the register of public sales of properties by private bailiffs in Bulgaria.

Website: https://sales.bcpea.org/properties

## Setup
Create `.env` file from `.env.template`

Install dependencies
`pip install requests beautifulsoup4 firebase-admin python-dotenv`

Install dependencies for `.yml` and Github Actions
`pip3 freeze > requirements.txt`

## Run Locally
`python main.py`