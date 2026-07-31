from pathlib import Path

from platform.models.engine_metadata import EngineMetadata
from platform.services.directory_inspector import DirectoryInspector


class ManifestReader:
    """
    Builds EngineMetadata by inspecting an Intelligence Component.
    """

    def read(self, engine_folder: Path) -> EngineMetadata:

        inspector = DirectoryInspector()

        metadata = EngineMetadata(
            engine_id=engine_folder.name.upper(),
            name=engine_folder.name.upper(),
            description=f"Auto generated metadata for {engine_folder.name.upper()}",
        )

        metadata.file_count = inspector.inspect_python_files(engine_folder)

        metadata.services = inspector.inspect_services(engine_folder)

        metadata.repositories = inspector.inspect_repositories(engine_folder)

        metadata.models = inspector.inspect_models(engine_folder)

        metadata.generators = inspector.inspect_generators(engine_folder)

        metadata.analyzers = inspector.inspect_analyzers(engine_folder)

        metadata.main_files = inspector.inspect_main_files(engine_folder)

        metadata.readme = inspector.inspect_readme(engine_folder)

        return metadata
