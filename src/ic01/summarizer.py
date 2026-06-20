from models import Requirement


def summarize_requirement(req: Requirement):
    """
    Generate a concise summary of a requirement.
    """

    text = req.text

    if len(text) <= 80:
        summary = text
    else:
        summary = text[:80] + "..."

    return {
        "id": req.id,
        "summary": summary
    }
