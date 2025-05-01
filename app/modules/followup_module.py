
def schedule_followup(email, toggles):
    if not toggles.get("follow_up_enabled"):
        return
    print(f"[FOLLOW-UP] Would schedule a follow-up for: {email}")
    # In real use, you'd store this in a DB or task scheduler like Celery
