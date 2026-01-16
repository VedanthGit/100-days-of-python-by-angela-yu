# RAIN ALERT
import os
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("OWM_ACCOUNT_SID")
auth_token = os.environ.get("OWM_AUTH_TOKEN")
# client = Client(account_sid, auth_token)

weather_params={
    "lat" : -19.258965,
    "lon" : 146.816956,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)

response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+15188083035",
        body="It’s going to rain today. Bring an umbrella ☔",
        to="+18777804236"
    )
    print(message.sid)
else:
    print("No rain expected. No SMS sent.")
