import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

smtp_password = os.getenv("SMTP_PASSWORD")

def send_email(subject, message, to_email):
    # ABV.bg SMTP server configuration
    SMTP_SERVER = 'smtp.abv.bg'
    SMTP_PORT = 465
    SMTP_USERNAME = 'spacex13@abv.bg'
    SMTP_PASSWORD = smtp_password

    # Create the email message
    msg = MIMEMultipart()
    msg.attach(MIMEText(message, 'plain', 'utf-8'))
    msg['Subject'] = subject
    msg['From'] = SMTP_USERNAME
    msg['To'] = to_email

    # Send the email
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, [to_email], msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
