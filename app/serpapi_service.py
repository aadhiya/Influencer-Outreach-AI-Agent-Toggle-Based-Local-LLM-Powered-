# app/services/serpapi_service.py

import requests
from app.config import SERPAPI_KEY
from app.services.memory_service import add_email

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

    results = []
    if "organic_results" in data:
        for item in data["organic_results"]:
            snippet = item.get("snippet", "")
            link = item.get("link", "")
            if "gmail.com" in snippet.lower() or "gmail.com" in link.lower():
                results.append(extract_email(snippet))

    # Save in memory
    for email in results:
        if email:
            add_email(email)

    return results

def extract_email(text):
    import re
    match = re.search(r"[a-zA-Z0-9_.+-]+@gmail\.com", text)
    if match:
        return match.group()
    return None
