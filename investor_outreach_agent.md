
# 📬 Investor Outreach Agent (Streamlit + SERPAPI + Ollama + Gmail)

This agent automates personalized investor outreach. Upload a CSV with investor names, and it finds contact emails, personalizes the message (with Ollama), and sends the pitch. Optionally attach a deck and schedule follow-ups.

---

## 📁 Project Structure

```
investor_outreach_agent/
├── email_scraper_ui.py         # Streamlit interface
├── investor_main.py            # FastAPI entry (if hosted)
├── investor_router.py          # Route logic
├── investor_outreach_agent.md  # This README
├── app/
│   └── services/
│       ├── scrape_emails.py           # Finds investor emails via SERPAPI
│       ├── gmail_service.py           # Sends emails via Gmail API
│       ├── ollama_service.py          # (Planned) Message personalization
│       └── memory_service.py          # Session memory
```

---

## 🛠️ How It Works

1. **Upload CSV** with a column named `name` for investor names.
2. **Email Extraction**: Uses SERPAPI to search for public email addresses.
3. **Email Personalization**: (Optional) Ollama customizes message per investor.
4. **Compose & Send**:
   - Inputs: Subject, HTML body, optional file attachment.
   - Each email is sent only once (tracked in `email_log_service.py`)
5. **Follow-up Logic**:
   - Automatically schedules a follow-up in X days if enabled.

---

## 💻 Streamlit UI Features

- CSV upload
- Email preview table
- Edit subject + HTML body
- Upload pitch deck
- Enable/disable personalization & follow-up
- Download outreach results

---
## 🚀 How to Run and Test Locally

    Clone the repository:

git clone https://github.com/YOUR_USERNAME/Influencer-Outreach-AI-Agent-Toggle-Based-Local-LLM-Powered-.git
cd Influencer-Outreach-AI-Agent-Toggle-Based-Local-LLM-Powered-

Install dependencies:

pip install -r requirements.txt

Set environment variables:
Create a .env file in the root with the following:

SERPAPI_KEY=your_serpapi_key
GMAIL_CLIENT_ID=your_gmail_client_id
GMAIL_CLIENT_SECRET=your_gmail_client_secret
GMAIL_REFRESH_TOKEN=your_gmail_refresh_token

Run the Streamlit UI:

streamlit run investor_outreach_agent/email_scraper_ui.py

Test:

    Upload a CSV file with a column name containing investor names.

    Customize the message.

    Run the agent to fetch emails and send outreach messages.

    Download the result log.

 ---
## 📸 Screenshots

_Add screenshots below once UI is finalized._

---

## 🧠 Notes

- Emails are never resent to the same investor.
- Works entirely locally with .env config for SERPAPI & Gmail.
- Modular: switch between DuckDuckGo, Google, ScrapeAPI etc.

---

## 🚀 Future Add-ons

- Scheduling real follow-up emails via background job
- CRM dashboard to track investor engagement
- LinkedIn scraping (manual review first)
- GPT-based pitch tailoring per fund
