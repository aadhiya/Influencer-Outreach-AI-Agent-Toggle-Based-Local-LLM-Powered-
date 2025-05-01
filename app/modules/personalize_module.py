
def apply_personalization(message, email, toggles):
    if not toggles.get("personalized_email"):
        return message
    name_part = email.split('@')[0].replace('.', ' ').replace('_', ' ').title()
    return message.replace("{{name}}", name_part)
