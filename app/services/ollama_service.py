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
import requests

def personalize_message(name, base_message):
    try:
        ollama_payload = {
            "model": "llama3",  # or any model you have installed locally
            "prompt": f"Personalize the following outreach message for an investor named {name}:\n\n{base_message}",
            "stream": False
        }

        response = requests.post("http://localhost:11434/api/generate", json=ollama_payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", base_message)

    except Exception as e:
        print(f"[Ollama Error] Falling back to default message for {name}: {e}")
        return base_message
