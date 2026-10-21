\# Automated Web Scraper with Scheduler



\## Description

A Python tool that scrapes book data (title, price, rating) from

books.toscrape.com, stores it in SQLite and CSV, and re-runs

automatically on a schedule.



\## Technologies

\- Python

\- Requests

\- BeautifulSoup

\- SQLite

\- Schedule



\## Features

\- Scrapes 20 books from the website

\- Saves data to SQLite database (books.db)

\- Exports data to CSV file (books.csv)

\- Runs automatically every 1 minute using a scheduler



\## How to Run

1\. Install libraries:

&#x20;  pip install requests beautifulsoup4 schedule

2\. Run the script:

&#x20;  python scraper.py

3\. Press Ctrl+C to stop the scheduler.



\## Output

\- books.db : SQLite database with scraped data

\- books.csv : CSV file with scraped data



\## Outcome

Automated data collection with scheduling and export to CSV or a database.

