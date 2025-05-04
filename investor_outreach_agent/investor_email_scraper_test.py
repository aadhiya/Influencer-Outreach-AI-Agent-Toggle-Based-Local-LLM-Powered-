import requests
import re

def extract_emails(text):
    return re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

def search_email(investor_name):
    query = f"{investor_name} email contact site:linkedin.com OR site:twitter.com OR site:vcfirm.com"
    print(f"🔍 Searching for: {query}")
    
    # Use DuckDuckGo for free scraping (Google blocks unauth)
    ddg_url = "https://lite.duckduckgo.com/lite"
    params = {"q": query}
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(ddg_url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        emails = extract_emails(response.text)
        return list(set(emails))[:3]  # Max 3 emails per person
    except Exception as e:
        print(f"[ERROR] {investor_name}: {e}")
        return []

# Example test list of investors
investors = [
    "Aneel Ranadive Soma Capital",
    "Pejman Nozad Pear VC",
    "Ann Miura-Ko Floodgate"
]

print("\n📧 Scraped Emails:")
for investor in investors:
    emails = search_email(investor)
    print(f"{investor}: {emails}")
