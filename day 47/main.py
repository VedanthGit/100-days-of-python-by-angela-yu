import os
import smtplib
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")
# AMAZON_URL = "https://appbrewery.github.io/instant_pot/" # Static Page
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1&language=en_US&currency=INR" # INR
# AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1&language=en_US&currency=USD" # USD

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(AMAZON_URL, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

whole = soup.select_one("span.a-price-whole").get_text(strip=True)
fraction = soup.select_one("span.a-price-fraction").get_text(strip=True)

whole = whole.replace(".", "").replace(",", "")

price = float(f"{whole}.{fraction}")
print(price) 


# price_without_currency = price.split("$")[1]
# # print(price_without_currency)

# price_as_float = float(price_without_currency)
# print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 7400
if price < BUY_PRICE:
    message = f"{title} is on sale for {price}"
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD )
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{AMAZON_URL}".encode("utf-8")
        )