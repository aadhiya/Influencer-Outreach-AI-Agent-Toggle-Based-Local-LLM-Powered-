
## ✅ Key Toggle Features

| Toggle | Function |
|--------|----------|
| 🧠 **Vetting** | Filters influencers by relevance (e.g., only include emails with 'fit' or 'pro') |
| ✨ **Personalized Messages** | Inserts influencer's name into the email dynamically |
| 🔁 **Auto Follow-Up** | Schedules a follow-up email if no reply is received |
| 📈 **Email Logging** | Logs all sent email addresses, timestamps, and status in `email_log.txt` |
| 🗂️ **CRM Tracking** | Stores influencer emails into a local CRM log (`crm_log.txt`) |

---

## 🧪 Example: Gym Collaboration Campaign

User Input in UI:

- **Influencer Type**: `Fitness`
- **Search Count**: `10`
- **Send Count**: `5`
- **Subject**: `Let's Collaborate: AI for Fitness`
- **Message (HTML)**:

```html
<h1>Hello {{name}},</h1>
<p>We're launching an AI-powered fitness assistant and would love to collaborate with you on Instagram!</p>
<p>We believe your content aligns perfectly with our vision.</p>
<p>No links here — just reply if you're interested and I’ll share the full brief.</p>
<p>- Team FitAI</p>
```
---
✅ Toggles enabled:

    Vet Influencers

    Personalized Emails

    Auto Follow-Up

    Log Emails

    CRM Tracking
    ---

    
## 🔍 Log Output Breakdown
    [SERPAPI EXTRACTED EMAILS]
['thefitnessmarshall@gmail.com', 'isabella.lanter@thestation.io', 'Isabellamichellelanter@gmail.com', 'thebloomcafe24@gmail.com']

[DEBUG] Raw influencer emails:
['thefitnessmarshall@gmail.com', 'isabella.lanter@thestation.io', 'Isabellamichellelanter@gmail.com', 'thebloomcafe24@gmail.com']

[VETTING] Filtered 4 -> 1 emails

Message Id: 1968a6a3fb4bf4be

[FOLLOW-UP] Would schedule a follow-up for: thefitnessmarshall@gmail.com

---
🧠 What Happened

    Vetting filtered out all but thefitnessmarshall@gmail.com

    Personalized message said: Hello Thefitnessmarshall

    Email was sent and logged in email_log.txt

    CRM log updated in crm_log.txt

    Follow-up task logged for future send
---
📸 Screenshot Example
![Screenshot 2025-05-01 091437](https://github.com/user-attachments/assets/bbf4ace8-dd5a-47a6-88f1-4e95f022ebab)
![Screenshot 2025-05-01 091501](https://github.com/user-attachments/assets/70e0c4f6-9319-4a0f-8307-19c5d42cb260)
![Screenshot 2025-05-01 093814](https://github.com/user-attachments/assets/e2231260-3e7e-44aa-91bf-aa19ea5c824f)

---
📁 Log Files

File	Description

email_log.txt	Tracks send status for each email

crm_log.txt	Stores all contacted influencers

(Future)	followup_tasks.db or similar




    

