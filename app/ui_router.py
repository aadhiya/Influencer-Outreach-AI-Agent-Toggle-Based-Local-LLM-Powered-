from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.services.memory_service import update_memory, memory
from app.serpapi_service import search_influencers
from app.services.gmail_service import send_message, create_message, create_gmail_service
from app.services.ollama_service import parse_user_prompt
from app.email_log_service import was_email_sent, log_email
# Toggle-based modules
from app.modules.vetting_module import apply_vetting
from app.modules.personalize_module import apply_personalization
from app.modules.followup_module import schedule_followup

from app.modules.crm_module import update_crm

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()
toggle_state = {"active": True}

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "toggle": toggle_state["active"],
        "results": [],
        "message": ""
    })

@router.post("/run")
def run_agent(request: Request,
              category: str = Form(...),
              custom_category: str = Form(""),
              search_count: int = Form(...),
              send_count: int = Form(...),
              subject: str = Form(...),
              message: str = Form(...),
              vetting_enabled: bool = Form(False),
              personalized_email: bool = Form(False),
              follow_up_enabled: bool = Form(False),
              logging_enabled: bool = Form(False),
              crm_enabled: bool = Form(False)):

    if category == "other" and custom_category.strip():
        category = custom_category.strip()

    if not toggle_state["active"]:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "toggle": False,
            "results": [],
            "message": "Agent is OFF"
        })

    # Create prompt and parse
    prompt = f"search for {category} influencers with email as gmail give {search_count} results subject {subject} message {message}"
    parsed = parse_user_prompt(prompt)
    update_memory(parsed["query"], parsed["subject"], parsed["message"])

    # Run search
    emails = search_influencers(parsed["query"], parsed["num_results"])
    emails = [e for e in emails if e]  # Remove None values before processing
    print("[DEBUG] Raw influencer emails:", emails)


    # Collect toggles
    toggles = {
        "vetting_enabled": vetting_enabled,
        "personalized_email": personalized_email,
        "follow_up_enabled": follow_up_enabled,
        "logging_enabled": logging_enabled,
        "crm_enabled": crm_enabled,
    }

    # Apply vetting
    emails = apply_vetting(emails, toggles)
    memory["emails"] = emails[:send_count]

    service = create_gmail_service()
    results = []

    for email in memory["emails"]:
        if was_email_sent(email):
            print(f"[SKIP] Already emailed: {email}")
            continue

        personalized_msg = apply_personalization(memory["message"], email, toggles)
        msg = create_message(email, memory["subject"], personalized_msg)
        result = send_message(service, "me", msg)

        log_email(email, "sent" if result else "failed", toggles)
        update_crm(email, toggles)
        schedule_followup(email, toggles)

        results.append({
            "email": email,
            "status": "sent" if result else "failed"
     })

    return templates.TemplateResponse("index.html", {
        "request": request,
        "toggle": True,
        "results": results,
        "message": f"Agent completed. {len(results)} entries."
    })

@router.post("/toggle")
def toggle_agent():
    toggle_state["active"] = not toggle_state["active"]
    return RedirectResponse(url="/", status_code=303)
