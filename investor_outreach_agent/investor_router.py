# investor_outreach_agent/investor_router.py

from fastapi import APIRouter, Request, UploadFile, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import csv, io

from app.email_log_service import was_email_sent, log_email
from app.services.gmail_service import create_gmail_service, create_message, send_message

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/investors")
def investor_ui(request: Request):
    return templates.TemplateResponse("investor_index.html", {
        "request": request,
        "results": [],
        "message": ""
    })

@router.post("/investors/run")
async def run_investor_agent(
    request: Request,
    file: UploadFile,
    subject: str = Form(...),
    message: str = Form(...),
    log_emails: bool = Form(False),
    follow_up: bool = Form(False)
):
    contents = await file.read()
    text = contents.decode("utf-8")
    names = [line.strip() for line in text.splitlines() if line.strip()]

    results = []
    service = create_gmail_service()

    for name in names:
        email = search_email_simulated(name)  # Placeholder for real search
        if not email or was_email_sent(email):
            continue

        personalized_msg = message.replace("{{name}}", name)
        msg = create_message(email, subject, personalized_msg)
        sent = send_message(service, "me", msg)

        if log_emails:
            log_email(email, "sent" if sent else "failed", {})

        # Follow-up simulation
        if follow_up:
            print(f"[FOLLOW-UP] Would schedule for {email}")

        results.append({
            "name": name,
            "email": email,
            "status": "sent" if sent else "failed"
        })

    return templates.TemplateResponse("investor_index.html", {
        "request": request,
        "results": results,
        "message": f"Agent completed. {len(results)} entries."
    })


def search_email_simulated(name):
    """Simulate email lookup for investor name"""
    fake_directory = {
        "George Kachanouski": "george@examplevc.com",
        "Adam Draper": "adam@boost.vc",
        "Elon Musk": "elon@spacex.com"
    }
    return fake_directory.get(name)
