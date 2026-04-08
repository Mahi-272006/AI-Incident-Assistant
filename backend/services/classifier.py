def classify_ticket(text):

    text = text.lower()

    if "vpn" in text:
        return "Network Issue"

    elif "password" in text:
        return "Authentication Issue"

    elif "email" in text:
        return "Email Problem"

    else:
        return "General IT Issue"