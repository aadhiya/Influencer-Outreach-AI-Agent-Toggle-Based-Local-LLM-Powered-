
def apply_vetting(emails, toggles):
    if not toggles.get("vetting_enabled"):
        return emails
    # Safely filter out None and low-quality emails
    vetted = [e for e in emails if e and ("fit" in e.lower() or "pro" in e.lower())]
    print(f"[VETTING] Filtered {len(emails)} -> {len(vetted)} emails")
    return vetted

