import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT= "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

TWILIO_SID = os.environ.get("SID")
TWILIO_AUTH = os.environ.get("AUTH_KEY")

# ---------------------------------------------------------------------------- #

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

difference_percentage = round((difference/ float(yesterday_closing_price)) * 100) + 2
print(difference_percentage)

if difference_percentage > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_report = news_response.json()["articles"]
    articles = news_report[:3]
    print(articles)


    formatted_articles = [f"{STOCK}: {up_down}{difference_percentage}%\n Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    account_sid = TWILIO_SID
    auth_token = TWILIO_AUTH
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
        from_="whatsapp:+14155238886",
        body= article,
        to="whatsapp:+918801056751"
        )

    print(message.sid)