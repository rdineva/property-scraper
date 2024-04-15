import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

def send_email(subject, content, to_email):
    message = Mail(SMTP_EMAIL, [to_email], subject, content)

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print('Email sent successfully!')
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise