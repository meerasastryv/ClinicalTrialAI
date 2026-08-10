from models import Requirement


def classify_requirement(requirement: Requirement):

   text = requirement.text.lower()

   categories = []

   if requirement.req_type == "BRD":
       categories.append("Business")

   if requirement.req_type == "FRD":
       categories.append("Functional")

   if requirement.req_type == "NFR":
       categories.append("NonFunctional")

   if requirement.req_type == "TST":
       categories.append("Test")

   security_keywords = [
       "authentication",
       "authorization",
       "saml",
       "oauth",
       "security"
   ]

   performance_keywords = [
       "seconds",
       "response time",
       "performance",
       "load"
   ]

   compliance_keywords = [
       "audit",
       "regulatory",
       "compliance",
       "validation"
   ]

   if any(word in text for word in security_keywords):
       categories.append("Security")

   if any(word in text for word in performance_keywords):
       categories.append("Performance")

   if any(word in text for word in compliance_keywords):
       categories.append("Compliance")

   return {
       "id": requirement.id,
       "categories": categories
   }

