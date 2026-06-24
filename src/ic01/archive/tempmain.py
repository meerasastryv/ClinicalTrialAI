from loader import load_requirements


requirements = load_requirements(
   "../../requirements/ctp"
)

print(f"\nLoaded {len(requirements)} requirements\n")

for req in requirements:
   print(req)

