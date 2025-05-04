
# Investor Outreach AI Agent (Free Version)

This sub-agent is designed to help founders reach out to potential investors intelligently, using a list of investor names. It searches the web for publicly available contact emails, sends a personalized pitch deck email, and logs the process.

---

## 🎯 Features

| Feature | Description |
|--------|-------------|
| 📋 Input Investor List | Provide a list of investor names |
| 🔎 Smart Email Discovery | Uses Google scraping via SerpAPI to locate public emails |
| ✉️ Personalized Emailing | Automatically inserts name + pitch deck |
| 🔁 Follow-Up Tracker | Logs and schedules follow-up tasks |
| 📈 Email Logging | Prevents duplicate sends and stores status |

---

## 🧪 How It Works

1. Upload or paste a list of investor names (e.g., from LinkedIn or a CSV).
2. Agent searches for public email addresses using free SerpAPI.
3. For each investor with a found email:
   - Sends a personalized email with your deck link.
   - Logs status in SQLite (`email_log.db`).
   - Optionally schedules a follow-up.
4. No duplicate outreach will occur for same contacts.

---

## 🔧 Requirements

- Free [SerpAPI](https://serpapi.com/) key
- Gmail account (for sending emails, same as core agent)
- Local FastAPI environment

---

## 🛠️ Free Tools Used

| Tool | Purpose |
|------|--------|
| SerpAPI (Free Tier) | Email discovery from Google results |
| Gmail API | Sending messages |
| SQLite | Email log tracking |
| FastAPI | UI/API interface |

---

## 💎 Optional Paid Enhancements

These can make the investor outreach more powerful:

| Enhancement | Tool |
|-------------|------|
| 💼 Verified Emails from LinkedIn | Clearbit, Hunter.io |
| 🧠 Contextual Matching (e.g. Web3 investors only) | GPT-4 with profile scraping |
| 📅 Follow-up Scheduling with Queueing | Celery + Redis |
| 🧾 CRM Integration | Notion, HubSpot, or Airtable API |
| 📊 Analytics Dashboard | Supabase or Metabase for stats |

---

## 📎 Sample Email Template

```
Subject: Opening Dialogue – AImodularity Deck

Hi {{name}},

I'm Jon, founder of AImodularity.com. We're building a toggle-based AI agent platform that empowers non-technical users to automate like engineers.

Here's our intro deck:
https://gamma.app/docs/AImodularity-tfwp4h4khivmrrz

I’d love to start a conversation about our upcoming seed round and see if it aligns with your focus.

Warm regards,  
Jon Capriola
```

---

Let me know if you want me to generate the Python logic or FastAPI UI for this sub-agent next!
