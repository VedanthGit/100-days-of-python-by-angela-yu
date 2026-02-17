import time
import csv
from typing import Dict, List
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import pandas as pd
import requests


BASE_URL = "https://books.toscrape.com/"
START_PATH = "catalogue/page-1.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; CustomScraper/1.0; +https://example.com/bot-info)"
}

RATE_LIMIT_SECONDS = 1.0


def fetch(url: str, retries=2):
    for attempt in range(retries + 1):
        res = requests.get(url, headers=HEADERS, timeout=15)
        if res.ok:
            return res.text
        if attempt == retries:
            res.raise_for_status()
        time.sleep(1)


def parse_books(html: str) -> List[Dict]:
    soup = BeautifulSoup(html, "lxml")
    items = []

    for card in soup.select(".product_pod"):
        title = card.h3.a["title"].strip()
        price = card.select_one(".price_color").text.strip()
        rating = card.select_one(".star-rating")["class"][-1]
        items.append({"title": title, "price": price, "rating": rating})

    return items


def get_next_page_url(current_url: str, html: str) -> str | None:
    soup = BeautifulSoup(html, "lxml")
    next_link = soup.select_one("li.next a")
    if not next_link:
        return None
    return urljoin(current_url, next_link["href"])


def scrape_all(start_url: str, max_pages: int = 5):
    url = start_url
    all_items = []
    page = 1

    while url and page <= max_pages:
        print(f"[INFO] Scraping page {page}: {url}")
        html = fetch(url)
        items = parse_books(html)
        all_items.extend(items)

        url = get_next_page_url(url, html)
        page += 1
        time.sleep(RATE_LIMIT_SECONDS)

    return all_items


def save_csv(rows: List[Dict], path: str = "data.csv"):
    if not rows:
        print("[WARN] No data to save")
        return
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    print(f"Saved {len(rows)} rows rows to {path}")


if __name__ == "__main__":
    start_url = urljoin(BASE_URL, START_PATH)
    data = scrape_all(start_url, max_pages=10)
    save_csv(data, "books.csv")
