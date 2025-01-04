# Property Scraper

Web Scraper for the register of public sales of properties by private bailiffs in Bulgaria.

Website: https://sales.bcpea.org/properties

## How it works
The python script scrapes the website, extracting all information about the properties for sale given a specific criteria. It then compares the existing properties in the Firebase Realtime Database and inserts the new ones. Then via SendGrid it sends the information about the new properties for sale to a personal email of your choice. The script is run automatically via GitHub actions and it runs daily.

## Tech Stack 
- Python (script)
- Firebase Realtime Database (for storing the scraped properties)
- SendGrid (for sending emails; used this service specifically so as not to have the emails marked as Spam by some email services)
- Github Actions (automates running the script daily)

## Local Dev Setup
1. Create `.env` file from `.env.template`

2. Install dependencies:

`pip install requests beautifulsoup4 firebase-admin python-dotenv sendgrid`

3. Install dependencies for `.yml` and Github Actions:

`pip3 freeze > requirements.txt`

4. Create a database in _Firebase Realtime Database_ to store the properties and update the `.env` file with your corresponding `FIREBASE_DATABASE_URL` and `FIREBASE_CREDENTIALS`.

5. Register in _SendGrid_ to get a personal API key for it and update the `SENDGRID_API_KEY` in the `.env` file. 

6. Update the `RECEIVER_EMAIL` in `.env` to the email you want the properties to be sent to. The `SMTP_EMAIL` can be any other email you've chosen. 

## Running Locally
`python main.py`
