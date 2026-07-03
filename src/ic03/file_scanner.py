from pathlib import Path
from datetime import datetime

from .config import SUPPORTED_EXTENSIONS, IGNORE_DIRECTORIES
from .models.source_file import SourceFile

class FileScanner:

    def __init__(self, project_root: Path):
        self.project_root = project_root

    def scan(self):

        discovered_files = []

        for path in self.project_root.rglob("*"):

            if not path.is_file():
                continue

            if any(part in IGNORE_DIRECTORIES for part in path.parts):
                continue

            extension = path.suffix.lower()

            if extension not in SUPPORTED_EXTENSIONS:
                continue

            stat = path.stat()

            discovered_files.append(
                SourceFile(
                    path=path,
                    relative_path=path.relative_to(self.project_root),
                    file_name=path.name,
                    extension=extension,
                    language=SUPPORTED_EXTENSIONS[extension],
                    size=stat.st_size,
                    last_modified=datetime.fromtimestamp(stat.st_mtime),
                )
            )

        return discovered_files
