# app/services/gmail_service.py

import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from app.config import GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET, GMAIL_REFRESH_TOKEN
from app.services.memory_service import get_memory
from app.email_log_service import was_email_sent, log_email_sent

def create_gmail_service():
    creds = Credentials(
        None,
        refresh_token=GMAIL_REFRESH_TOKEN,
        client_id=GMAIL_CLIENT_ID,
        client_secret=GMAIL_CLIENT_SECRET,
        token_uri='https://oauth2.googleapis.com/token'
    )
    service = build('gmail', 'v1', credentials=creds)
    return service

def send_emails():
    memory = get_memory()
    service = create_gmail_service()
    sent_results = []

    for email in memory["emails"]:
        if was_email_sent(email):
            print(f"⚠️ Skipping {email} — already emailed.")
            sent_results.append({"email": email, "status": "already sent"})
            continue

        msg = create_message(email, memory["subject"], memory["message"])
        result = send_message(service, "me", msg)

        if result:
            log_email_sent(email, memory["subject"])
            sent_results.append({"email": email, "status": "sent"})
        else:
            sent_results.append({"email": email, "status": "failed"})

    return sent_results


def create_message(to, subject, body_html):
    message = MIMEText(body_html, 'html')
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f'Message Id: {message["id"]}')
        return message
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
