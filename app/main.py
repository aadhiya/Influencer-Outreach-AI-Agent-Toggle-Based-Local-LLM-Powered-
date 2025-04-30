from fastapi import FastAPI
from app.services.memory_service import update_memory, get_memory
from app.serpapi_service import search_influencers
from app.services.gmail_service import send_emails
from app.services.ollama_service import parse_user_prompt

app = FastAPI()

# Toggle control
toggle_active = True

@app.post("/process/")
def process_user_prompt(prompt: str):
    if not toggle_active:
        return {"status": "Toggle is OFF."}

    # Step 1: Parse the prompt
    parsed = parse_user_prompt(prompt)

    # Step 2: Update memory
    update_memory(parsed["query"], parsed["subject"], parsed["message"])

    # Step 3: Search influencers
    found_emails = search_influencers(parsed["query"], parsed["num_results"])

    # Step 4: Error if no emails found
    if not found_emails:
        return {"status": "No influencers found with Gmail emails."}

    # Step 5: Send emails
    send_emails()

    return {
        "status": f"Emails sent to {len(found_emails)} influencers.",
        "emails": found_emails
    }

@app.get("/memory/")
def view_memory():
    return get_memory()
