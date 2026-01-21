import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TO_TWILIO_VIRTUAL_NUMBER = os.getenv("TO_TWILIO_VIRTUAL_NUMBER")


class NotificationManager:
    """Responsible for sending WhatsApp notifications."""

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_whatsapp(self, message_body: str):
        message = self.client.messages.create(
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TO_TWILIO_VIRTUAL_NUMBER,
            body=message_body
        )
        print(f"WhatsApp sent | SID: {message.sid}")
