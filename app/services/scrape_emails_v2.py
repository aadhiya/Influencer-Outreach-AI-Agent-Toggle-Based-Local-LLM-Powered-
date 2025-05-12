import os
import requests
import re
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "google-web-search1.p.rapidapi.com"
}


def search_google_for_urls(name):
    url = "https://google-web-search1.p.rapidapi.com/"
    params = {
        "query": f'"{name}" email',
        "limit": "5"
    }
    try:
        res = requests.get(url, headers=headers, params=params)
        print(f"\n🔍 Querying for name: {name}")
        print("📤 Sent Query Params:", params)
        print("📥 Raw API Response:", res.text[:500])

        json_data = res.json()
        results = json_data.get("results", []) or json_data.get("data", [])
        if not results:
            print("⚠️ No search results returned.")
        return [r["url"] for r in results if "url" in r]
    except Exception as e:
        print(f"❌ Search error for {name}: {e}")
        return []


def extract_emails_from_url(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.get_text()
        html = str(soup)

        # Extract direct emails
        emails = re.findall(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", text)

        # Look in meta tags
        metas = " ".join([m.get("content", "") for m in soup.find_all("meta")])
        meta_emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", metas)
        emails.extend(meta_emails)

        # Detect obfuscated formats
        obfuscated = re.findall(r"[a-zA-Z0-9._%+-]+\s*\[at\]\s*[a-zA-Z0-9.-]+\s*\[dot\]\s*[a-zA-Z]{2,}", text)
        for obf in obfuscated:
            cleaned = obf.replace("[at]", "@").replace("[dot]", ".").replace(" ", "")
            emails.append(cleaned)

        return list(set(e.lower() for e in emails if len(e) <= 60))
    except:
        return []


def process_name(name):
    urls = search_google_for_urls(name)
    time.sleep(1.5)
    all_emails = []
    for u in urls:
        emails = extract_emails_from_url(u)
        all_emails.extend(emails)
    return {
        "name": name,
        "matched_urls": ", ".join(urls),
        "emails": ", ".join(set(all_emails))
    }
