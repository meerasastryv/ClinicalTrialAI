from models import Requirement


def extract_metadata(requirement: Requirement):

    text = requirement.text.lower()

    metadata = {
        "id": requirement.id,
        "product": requirement.product,
        "type": requirement.req_type,
        "actor": "Unknown",
        "domain": "General",
        "priority": "Medium"
    }

    # Domain detection

    if any(word in text for word in
           ["authentication", "authorization", "saml", "oauth"]):
        metadata["domain"] = "Security"

    elif any(word in text for word in
             ["audit", "compliance", "regulatory", "validation"]):
        metadata["domain"] = "Compliance"

    elif any(word in text for word in
             ["response", "performance", "seconds", "load"]):
        metadata["domain"] = "Performance"

    elif any(word in text for word in
             ["study", "protocol", "configuration"]):
        metadata["domain"] = "Clinical"

    # Priority detection

    if requirement.req_type == "BRD":
        metadata["priority"] = "High"

    elif requirement.req_type == "FRD":
        metadata["priority"] = "High"

    elif requirement.req_type == "NFR":
        metadata["priority"] = "Medium"

    elif requirement.req_type == "TST":
        metadata["priority"] = "Low"

    # Actor detection

    if "user" in text:
        metadata["actor"] = "User"

    elif "system" in text:
        metadata["actor"] = "System"

    return metadata
