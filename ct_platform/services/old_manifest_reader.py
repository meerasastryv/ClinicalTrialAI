from pathlib import Path

from ct_platform.models.engine_metadata import EngineMetadata


class ManifestReader:
    """
    Automatically generates metadata by inspecting
    an Intelligence Component directory.
    """

    def read(self, engine_folder: Path) -> EngineMetadata:

        metadata = EngineMetadata(
            engine_id=engine_folder.name.upper(),
            name=engine_folder.name.upper(),
            description=f"Auto generated metadata for {engine_folder.name.upper()}",
        )

        metadata.file_count = len(list(engine_folder.rglob("*.py")))

        services = engine_folder / "services"
        if services.exists():
            metadata.services = [
                f.stem
                for f in services.glob("*.py")
                if f.name != "__init__.py"
            ]

        repositories = engine_folder / "repositories"
        if repositories.exists():
            metadata.repositories = [
                f.stem
                for f in repositories.glob("*.py")
                if f.name != "__init__.py"
            ]

        models = engine_folder / "models"
        if models.exists():
            metadata.models = [
                f.stem
                for f in models.glob("*.py")
                if f.name != "__init__.py"
            ]

        generators = engine_folder / "generators"
        if generators.exists():
            metadata.generators = [
                f.stem
                for f in generators.glob("*.py")
                if f.name != "__init__.py"
            ]

        analyzers = engine_folder / "analyzers"
        if analyzers.exists():
            metadata.analyzers = [
                f.stem
                for f in analyzers.glob("*.py")
                if f.name != "__init__.py"
            ]

        metadata.main_files = [
            f.name
            for f in engine_folder.glob("main*.py")
        ]

        metadata.readme = (engine_folder / "README.md").exists()

        return metadata
