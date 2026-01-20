from datetime import datetime
import os
import requests

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 180
AGE = 22

NUTRITION_APP_ID = os.environ.get("NT_APP_ID")
NUTRITION_API_KEY = os.environ.get("NT_API_KEY")

NUTRITION_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
HEALTHZ_ENDPOINT = "https://app.100daysofpython.dev/healthz"

SHEETY_ENDPOINT = os.environ.get("STY_ENDPOINT")

SHEETY_TOKEN = os.environ.get("STY_TOKEN")

nutrition_headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}


sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json",
}

query = input("What have you done today? ")

nutrition_payload = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutrition_response = requests.post(
    NUTRITION_ENDPOINT,
    json=nutrition_payload,
    headers=nutrition_headers,
)

# nutrition_response.raise_for_status()
exercises = nutrition_response.json()["exercises"]

today = datetime.now().strftime("%Y-%m-%d")
now = datetime.now().strftime("%H:%M")

for exercise in exercises:
    payload = {
        "sheet1": {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": int(exercise["duration_min"]),
            "calories": int(exercise["nf_calories"]),
        }
    }

    response = requests.post(
        SHEETY_ENDPOINT,
        json=payload,
        headers=sheety_headers,
    )

    # response.raise_for_status()
    print("Logged:", payload["sheet1"])
