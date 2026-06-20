from loader import load_requirements
from vector_store import store_requirement

requirements = load_requirements(
    "requirements/ctp"
)

for req in requirements:
    store_requirement(req)

print(
    f"Stored {len(requirements)} requirements"
)
