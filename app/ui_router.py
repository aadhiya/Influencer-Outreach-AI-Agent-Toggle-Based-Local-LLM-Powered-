
# Re-run after code execution state was reset
from pathlib import Path

# Define paths
ui_router_path = Path("/mnt/data/ui_router.py")
index_html_path = Path("/mnt/data/index.html")


from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.services.memory_service import update_memory
from app.serpapi_service import search_influencers
from app.services.gmail_service import send_emails
from app.email_log_service import init_db, was_email_sent
from app.services.ollama_service import parse_user_prompt

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
def run_agent(request: Request, prompt: str = Form(...)):
    if not toggle_state["active"]:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "toggle": toggle_state["active"],
            "results": [],
            "message": "Agent is OFF"
        })

    parsed = parse_user_prompt(prompt)
    update_memory(parsed["query"], parsed["subject"], parsed["message"])
    emails = search_influencers(parsed["query"], parsed["num_results"])
    results = send_emails()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "toggle": toggle_state["active"],
        "results": results,
        "message": f"Agent completed. {len(results)} entries."
    })

@router.post("/toggle")
def toggle_agent():
    toggle_state["active"] = not toggle_state["active"]
    return RedirectResponse(url="/", status_code=303)