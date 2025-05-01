
def update_crm(email, toggles):
    if not toggles.get("crm_enabled"):
        return
    with open("crm_log.txt", "a") as f:
        f.write(f"{email}\n")
