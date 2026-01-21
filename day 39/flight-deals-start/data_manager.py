import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/338d7f7cdf9e06e2682f7709beeab535/flightDeals/prices"
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")


class DataManager:
    """Handles Google Sheet via Sheety API."""

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
            "Content-Type": "application/json",
        }

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        return response.json()["prices"]
