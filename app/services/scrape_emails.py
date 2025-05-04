# scrape_emails.py (SerpAPI-powered)

import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")


def search_email_via_serpapi(name):
    query = f"{name} investor email contact"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 10
    }

    response = requests.get("https://serpapi.com/search.json", params=params)
    data = response.json()

    emails = set()
    if "organic_results" in data:
        for result in data["organic_results"]:
            snippet = result.get("snippet", "")
            link = result.get("link", "")
            text = f"{snippet} {link}"
            matches = re.findall(r"[\w\.-]+@[\w\.-]+", text)
            for match in matches:
                if not match.endswith("@duckduckgo.com"):
                    emails.add(match)
    return list(emails)


def batch_search_emails(names):
    results = []
    for name in names:
        found = search_email_via_serpapi(name)
        results.append({"name": name, "emails": ", ".join(found) if found else "Not Found"})
    return results
