# Properties Web Scraper

Web Scraper for the register of public sales of properties by private bailiffs in Bulgaria.

Website: https://sales.bcpea.org/properties

## How it works
The python script scrapes the website, extracting all information about the properties for sale given a specific criteria. It then compares the existing properties in the _Firebase Realtime Database_ and inserts the new ones. Then via _SendGrid_ it sends the information about the new properties for sale to a personal email of your choice. The script is run automatically via _GitHub Actions_ and it runs daily.

## Technologies
- **Python** - _script_
- **Firebase Realtime Database** - _for storing the scraped properties_
- **SendGrid** - _for sending emails; used this service specifically so as not to have the emails marked as "Spam" by some email services_
- **Github Actions** - _automates running the script daily_

## Local Dev Setup

1. Install dependencies

```shell
pip install requests beautifulsoup4 firebase-admin python-dotenv sendgrid
```

2. Install dependencies for `.yml` and Github Actions

```shell
pip3 freeze > requirements.txt
```

3. Create an `.env` file from `.env.template`

4. Create a database in _Firebase Realtime Database_ to store the properties and update the `.env` file with your corresponding `FIREBASE_DATABASE_URL` and `FIREBASE_CREDENTIALS`.

5. Register in _SendGrid_ to get a personal API key for it and update the `SENDGRID_API_KEY` in the `.env` file. 

6. Update the `RECEIVER_EMAIL` in `.env` to the email you want the properties to be sent to. The `SMTP_EMAIL` can be any other email you've chosen. 

## Run Locally
```shell
python main.py
```
