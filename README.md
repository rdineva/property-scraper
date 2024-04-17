# Property Scraper

Web Scraper for the register of public sales of properties by private bailiffs in Bulgaria.

Website: https://sales.bcpea.org/properties

## Tech Info
- Python (script)
- Firebase Realtime Database (properties storage)
- SendGrid (sends emails)
- Github Actions (automates running the script daily) 

## Local Dev Setup
Create `.env` file from `.env.template`

Install dependencies:

`pip install requests beautifulsoup4 firebase-admin python-dotenv sendgrid`

Install dependencies for `.yml` and Github Actions:

`pip3 freeze > requirements.txt`

## Run Locally
`python main.py`
