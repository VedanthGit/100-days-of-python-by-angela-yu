import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
TWILIO_VERIFIED_NUMBER=os.getenv("TWILIO_VERIFIED_NUMBER")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
EMAIL_PROVIDER_SMTP_ADDRESS=os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS")

class NotificationManager:

    def __init__(self):
        self.smtp_address = EMAIL_PROVIDER_SMTP_ADDRESS
        self.email = MY_EMAIL
        self.email_password = MY_EMAIL_PASSWORD
        self.whatsapp_number = TWILIO_WHATSAPP_NUMBER
        self.twilio_verified_number = TWILIO_VERIFIED_NUMBER
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=self.whatsapp_number,
            body=message_body,
            to=self.twilio_verified_number
        )
        print(message.sid)
        
    def send_emails(self, email_list, email_body):
        with smtplib.SMTP(self.smtp_address, 587) as connection:
            connection.starttls()
            connection.login(self.email, self.email_password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )