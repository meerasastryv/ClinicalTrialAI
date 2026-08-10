from pathlib import Path
import yaml

from models import Requirement


def load_requirements(root_dir: str):

    requirements = []

    for file in Path(root_dir).rglob("*.yml"):

        # Skip Doorstop configuration files
        if file.name == ".doorstop.yml":
            continue

        with open(file, "r") as f:
            data = yaml.safe_load(f)

        req_id = file.stem

        parts = req_id.split("-")

        product = parts[0]
        req_type = parts[1][:3]

        # Extract only linked requirement IDs
        raw_links = data.get("links", [])

        links = []

        for item in raw_links:
            if isinstance(item, dict):
                links.extend(item.keys())
            else:
                links.append(item)

        requirement = Requirement(
            id=req_id,
            product=product,
            req_type=req_type,
            text=data.get("text", "").strip(),
            links=links
        )

        requirements.append(requirement)

    return requirements
