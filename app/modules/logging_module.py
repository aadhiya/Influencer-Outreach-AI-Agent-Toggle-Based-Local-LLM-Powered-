
import datetime
def log_email(email, status, toggles):
    if not toggles.get("logging_enabled"):
        return
    with open("email_log.txt", "a") as f:
        f.write(f"{datetime.datetime.utcnow()} | {email} | {status}\n")
