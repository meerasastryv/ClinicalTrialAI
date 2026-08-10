from models import Requirement


def generate_acceptance_criteria(req: Requirement):
    """
    Generate acceptance criteria from a requirement.
    """

    criteria = []

    text = req.text.lower()

    if "saml" in text:
        criteria.append("User can authenticate using SAML")

    if "oauth" in text:
        criteria.append("User can authenticate using OAuth2")

    if "create" in text:
        criteria.append("User can create records")

    if "modify" in text:
        criteria.append("User can modify records")

    if "approve" in text:
        criteria.append("User can approve records")

    if "retire" in text:
        criteria.append("User can retire records")

    if "retrieve" in text:
        criteria.append("User can retrieve data")

    if "store" in text:
        criteria.append("User can store data")

    if "audit" in text:
        criteria.append("System shall maintain audit history")

    if not criteria:
        criteria.append("Requirement shall be implemented successfully")

    return {
        "id": req.id,
        "acceptance_criteria": criteria
    }
