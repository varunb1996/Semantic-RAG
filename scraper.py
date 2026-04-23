import requests
from bs4 import BeautifulSoup
import json
import os
from tqdm import tqdm
import time

URLS = [
    "https://en.wikipedia.org/wiki/Kubernetes",
    "https://en.wikipedia.org/wiki/Docker_(software)",
    "https://en.wikipedia.org/wiki/Apache_Kafka",
    "https://en.wikipedia.org/wiki/Microservices",
    "https://en.wikipedia.org/wiki/Continuous_integration"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        paragraphs = soup.select("p")

        text = " ".join([
            p.get_text().strip()
            for p in paragraphs
            if len(p.get_text().strip()) > 50
        ])

        return text

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

def main():
    os.makedirs("../data/raw", exist_ok=True)

    data = []

    for url in tqdm(URLS):
        text = scrape(url)

        print(f"{url} → length: {len(text)}")

        if len(text) < 200:
            print(f"Skipping {url} (too little content)")
            continue

        data.append({
            "url": url,
            "text": text
        })

        time.sleep(1)  # prevent blocking

    with open("../data/raw/scraped.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("Scraping complete")

if __name__ == "__main__":
    main()