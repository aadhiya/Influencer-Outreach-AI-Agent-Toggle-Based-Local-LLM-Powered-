# app/services/memory_service.py

memory = {
    "prompt": None,
    "emails": [],
    "subject": None,
    "message": None
}

def update_memory(prompt, subject, message):
    memory["prompt"] = prompt
    memory["subject"] = subject
    memory["message"] = message
    memory["emails"] = []

def add_email(email):
    memory["emails"].append(email)

def get_memory():
    return memory
