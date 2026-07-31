from pathlib import Path

from platform.models.engine_metadata import EngineMetadata
from platform.repositories.engine_registry import EngineRegistry

class EngineDiscoveryService:
    """
    Discovers IC folders.

    Only discovers.

    Does NOT register.
    """

    def __init__(self, registry=None):
        self.registry = registry

    def discover_folders(self, src_directory="src"):

        folders = []

        src = Path(src_directory)

        if not src.exists():
            return folders

        for item in sorted(src.iterdir()):

            if item.is_dir():

                if item.name.lower().startswith("ic"):

                    folders.append(item)

        return folders







