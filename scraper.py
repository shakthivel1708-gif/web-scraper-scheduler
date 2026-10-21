import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
import schedule
import time
from datetime import datetime

URL = "https://books.toscrape.com/"
DB_FILE = "books.db"
CSV_FILE = "books.csv"


def scrape_books():
    print(f"[{datetime.now()}] Scraping started...")
    response = requests.get(URL, timeout=10)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    for item in soup.select("article.product_pod"):
        title = item.h3.a["title"]
        price = item.select_one("p.price_color").text.strip()
        rating = item.select_one("p.star-rating")["class"][1]
        books.append((title, price, rating))

    print(f"Found {len(books)} books")
    return books


def save_to_sqlite(books):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            rating TEXT,
            scraped_at TEXT
        )
    """)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for title, price, rating in books:
        cur.execute(
            "INSERT INTO books (title, price, rating, scraped_at) VALUES (?, ?, ?, ?)",
            (title, price, rating, now),
        )
    conn.commit()
    conn.close()
    print("Saved to SQLite")


def save_to_csv(books):
    with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Rating"])
        writer.writerows(books)
    print("Saved to CSV")


def job():
    try:
        books = scrape_books()
        save_to_sqlite(books)
        save_to_csv(books)
        print("Job completed!\n")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    job()  # run once immediately
    schedule.every(1).minutes.do(job)  # then every 1 minute
    print("Scheduler running... Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)