from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.services.memory_service import update_memory, memory
from app.serpapi_service import search_influencers
from app.services.gmail_service import send_emails
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
def run_agent(request: Request,
              category: str = Form(...),
              custom_category: str = Form(""),
              search_count: int = Form(...),
              send_count: int = Form(...),
              subject: str = Form(...),
              message: str = Form(...)):

    if category == "other" and custom_category.strip():
        category = custom_category.strip()

    if not toggle_state["active"]:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "toggle": False,
            "results": [],
            "message": "Agent is OFF"
        })

    prompt = f"search for {category} influencers with email as gmail give {search_count} results subject {subject} message {message}"
    parsed = parse_user_prompt(prompt)
    update_memory(parsed["query"], parsed["subject"], parsed["message"])
    emails = search_influencers(parsed["query"], parsed["num_results"])
    memory["emails"] = emails[:send_count]
    results = send_emails()

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
