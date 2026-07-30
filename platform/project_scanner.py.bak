from pathlib import Path
from typing import List

from platform.module_info import ModuleInfo
from platform.utils import get_project_root


class ProjectScanner:
    """
    Scans the ClinicalTrialAI project.
    """

    def __init__(self):

        self.project_root = get_project_root()
        self.src_path = self.project_root / "src"

    def discover_ic_folders(self) -> List[Path]:

        folders = []

        if not self.src_path.exists():
            return folders

        for item in sorted(self.src_path.iterdir()):

            if item.is_dir() and item.name.startswith("ic"):
                folders.append(item)

        return folders

    def discover_python_modules(self) -> List[ModuleInfo]:

        modules = []

        for ic_folder in self.discover_ic_folders():
            ic_name = ic_folder.name
            for py_file in ic_folder.rglob("*.py"):
                # Ignore package initialization files
                if py_file.stem == "__init__":
                    continue
                relative = py_file.relative_to(ic_folder)
                parts = relative.parts

                if len(parts) > 1:
                    module_type = parts[0]
                else:
                    module_type = "root"

                modules.append(
                    ModuleInfo(
                        ic_name=ic_name,
                        module_name=py_file.stem,
                        module_path=str(py_file),
                        module_type=module_type,
                    )
                )

        return modules
