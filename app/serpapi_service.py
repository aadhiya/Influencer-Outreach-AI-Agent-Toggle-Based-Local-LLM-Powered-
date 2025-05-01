import requests
import re
from app.config import SERPAPI_KEY
from app.services.memory_service import add_email

def extract_emails(text):
    # Extract all emails (any domain)
    return re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

def search_influencers(query, num_results=10):
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google",
        "q": query,
        "num": num_results,
        "api_key": SERPAPI_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    print("[SERPAPI RAW RESULTS]", data)

    results = []

    if "organic_results" in data:
        for item in data["organic_results"]:
            snippet = item.get("snippet", "")
            link = item.get("link", "")

            # Search both snippet and link text for emails
            found = extract_emails(snippet) + extract_emails(link)
            for email in found:
                if email and email not in results:
                    results.append(email)

    print("[SERPAPI EXTRACTED EMAILS]", results)

    for email in results:
        add_email(email)

    return results
