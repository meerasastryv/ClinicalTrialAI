from pathlib import Path


class DirectoryInspector:
    """
    Inspects the directory structure of an Intelligence Component.
    """

    @staticmethod
    def inspect_python_files(engine_folder: Path) -> int:
        return len(list(engine_folder.rglob("*.py")))

    @staticmethod
    def inspect_services(engine_folder: Path):
        folder = engine_folder / "services"
        if not folder.exists():
            return []

        return [
            f.stem
            for f in folder.glob("*.py")
            if f.name != "__init__.py"
        ]

    @staticmethod
    def inspect_repositories(engine_folder: Path):
        folder = engine_folder / "repositories"
        if not folder.exists():
            return []

        return [
            f.stem
            for f in folder.glob("*.py")
            if f.name != "__init__.py"
        ]

    @staticmethod
    def inspect_models(engine_folder: Path):
        folder = engine_folder / "models"
        if not folder.exists():
            return []

        return [
            f.stem
            for f in folder.glob("*.py")
            if f.name != "__init__.py"
        ]

    @staticmethod
    def inspect_generators(engine_folder: Path):
        folder = engine_folder / "generators"
        if not folder.exists():
            return []

        return [
            f.stem
            for f in folder.glob("*.py")
            if f.name != "__init__.py"
        ]

    @staticmethod
    def inspect_analyzers(engine_folder: Path):
        folder = engine_folder / "analyzers"
        if not folder.exists():
            return []

        return [
            f.stem
            for f in folder.glob("*.py")
            if f.name != "__init__.py"
        ]

    @staticmethod
    def inspect_main_files(engine_folder: Path):
        return [
            f.name
            for f in engine_folder.glob("main*.py")
        ]

    @staticmethod
    def inspect_readme(engine_folder: Path):
        return (engine_folder / "README.md").exists()
