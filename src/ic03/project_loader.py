from pathlib import Path


class ProjectLoader:
    """Loads and validates a source code project."""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path).expanduser().resolve()

    def exists(self) -> bool:
        return self.project_path.exists()

    def is_directory(self) -> bool:
        return self.project_path.is_dir()

    def validate(self):
        if not self.exists():
            raise FileNotFoundError(
                f"Project does not exist: {self.project_path}"
            )

        if not self.is_directory():
            raise NotADirectoryError(
                f"Not a directory: {self.project_path}"
            )

    def get_project_root(self) -> Path:
        self.validate()
        return self.project_path
