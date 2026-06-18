from loader import load_requirements
from search import (
    find_by_product,
    find_by_type,
    find_by_keyword,
    find_by_link
)

requirements = load_requirements(
    "../../requirements/ctp"
)

print(f"\nLoaded {len(requirements)} requirements\n")


print("=" * 80)
print("SPA Requirements")
print("=" * 80)

for req in find_by_product(requirements, "SPA"):
    print(req)


print("\n" + "=" * 80)
print("FRD Requirements")
print("=" * 80)

for req in find_by_type(requirements, "FRD"):
    print(req)


print("\n" + "=" * 80)
print("Authentication Requirements")
print("=" * 80)

for req in find_by_keyword(requirements, "authentication"):
    print(req)


print("\n" + "=" * 80)
print("Requirements linked to SPA-BRD001")
print("=" * 80)

for req in find_by_link(requirements, "SPA-BRD001"):
    print(req)
