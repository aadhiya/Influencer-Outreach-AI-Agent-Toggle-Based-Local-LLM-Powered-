# app/services/ollama_service.py

def parse_user_prompt(prompt):
    # Dumb parsing for now (upgrade with real LLM later if needed)
    prompt = prompt.lower()
    subject = "Default Subject"
    message = "Default Message"
    num_results = 10

    if "subject" in prompt and "message" in prompt:
        parts = prompt.split("subject")
        search_part = parts[0]
        subject_message = parts[1].split("message")
        subject = subject_message[0].strip()
        message = subject_message[1].strip()
    else:
        search_part = prompt

    if "give" in search_part:
        try:
            num_results = int(search_part.split("give")[1].split()[0])
        except:
            num_results = 10

    return {
        "query": search_part.strip(),
        "subject": subject,
        "message": message,
        "num_results": num_results
    }
