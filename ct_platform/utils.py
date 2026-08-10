from pathlib import Path


def get_project_root() -> Path:
    """
    Returns the ClinicalTrialAI project root.
    """

    current = Path(__file__).resolve()

    while current.parent != current:
        if (current / "src").exists():
            return current
        current = current.parent

    raise RuntimeError("Unable to locate project root.")
