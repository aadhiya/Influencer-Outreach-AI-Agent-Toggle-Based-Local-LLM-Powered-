# Influencer-Outreach-AI-Agent-Toggle-Based-Local-LLM-Powered-

# Influencer Outreach AI Agent 🤖📧

A toggle-based, local LLM-powered AI agent that automates the process of discovering influencers and emailing them — without relying on OpenAI APIs.

---

## 🚀 What This Agent Does

Given a natural language prompt like:

> "search for gym influencers with email as gmail give 5 results subject ChatGPT message \<h1>Hello!</h1>\<p>Let's connect.\</p>"

The agent will:
1. Parse the prompt using a local LLM (via Ollama)
2. Search Google using SerpAPI
3. Extract Gmail addresses from influencer pages/snippets
4. Send HTML-formatted emails using Gmail API

---

## ⚙️ Workflow Overview
User Prompt ➜ Ollama (Local LLM) ➜ SerpAPI Search ➜ Gmail Extraction ➜ Gmail API ➜ Email Sent


Each run is logged in memory (with upgrades available for DB-based logging, analytics, UI, and retries).

---

## 🧠 Why SerpAPI and Gmail API?

### ✅ SerpAPI
- Handles real-time Google search
- Bypasses scraping complexity (avoids IP blocks, CAPTCHAs)
- Clean JSON results of search queries

### ✅ Gmail API
- Secure way to send authenticated emails as the user
- Logs all messages in Gmail "Sent" folder
- Complies with Google's security/auth rules (OAuth 2.0)

---
---

## 📜 License

**Copyright (c) 2025 Jon Capriola**

All rights reserved.

This software and associated files (the “Software”) may **not be used, copied, modified, merged, published, distributed, sublicensed, or sold** in any form or for any purpose without the **express written permission of the author**.

Any unauthorized use shall be considered a violation of applicable intellectual property laws.

To request permission, please contact the author directly.

## 🔑 How to Get API Keys

### 🔹 1. Get a SerpAPI Key

1. Go to [https://serpapi.com](https://serpapi.com)
2. Sign up (free plan gives 100 searches/month)
3. Copy your API key from dashboard
4. Add to `.env` file as:
SERPAPI_KEY=your_key_here


---

### 🔹 2. Set Up Gmail API

#### Step 1: Google Cloud Console

- Visit: [https://console.cloud.google.com/](https://console.cloud.google.com/)
- Create a new project

#### Step 2: Enable Gmail API

- Go to **APIs & Services** → **Library**
- Enable **Gmail API**

#### Step 3: OAuth Consent Screen

- Type: **External**
- Add yourself as **Test User**
- Save and continue

#### Step 4: Create OAuth Credentials

- Go to **Credentials** → **Create Credentials** → **OAuth Client ID**
- App Type: **Desktop App**
- Download `client_secret.json`

#### Step 5: Generate Refresh Token

Run this script:

```python
from google_auth_oauthlib.flow import InstalledAppFlow
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
creds = flow.run_local_server(port=0)
print(creds.client_id)
print(creds.client_secret)
print(creds.refresh_token)

Add to .env:
GMAIL_CLIENT_ID=your_id
GMAIL_CLIENT_SECRET=your_secret
GMAIL_REFRESH_TOKEN=your_token

✅ Run the Agent

    Start Ollama (e.g., ollama run tinyllama)

    Launch API:
uvicorn app.main:app --reload

Visit Swagger UI:
 http://127.0.0.1:8000/docs
 Use POST /process/ endpoint with a prompt.


