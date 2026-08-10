"""
Python module discovery service.

Discovers Python source modules within a project.

Author: ClinicalTrialAI
"""

from __future__ import annotations

import logging
from pathlib import Path


logger = logging.getLogger(__name__)


class ModuleDiscovery:
    """
    Discovers Python modules in a project.
    """

    DEFAULT_IGNORED_DIRECTORIES = {
        ".git",
        ".github",
        ".idea",
        ".vscode",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".venv",
        "venv",
        "env",
        "build",
        "dist",
        "node_modules",
        "coverage",
        "htmlcov",
    }

    def __init__(
        self,
        ignored_directories: set[str] | None = None,
    ) -> None:
        """
        Initialize the module discovery service.

        Parameters
        ----------
        ignored_directories
            Additional directory names to ignore.
        """
        self._ignored_directories = (
            self.DEFAULT_IGNORED_DIRECTORIES.copy()
        )

        if ignored_directories:
            self._ignored_directories.update(
                ignored_directories
            )

    def discover(
        self,
        project_root: Path,
    ) -> list[Path]:
        """
        Discover Python modules.

        Parameters
        ----------
        project_root
            Root directory of the project.

        Returns
        -------
        list[Path]
            Relative paths to discovered Python modules.
        """
        if not project_root.exists():
            raise FileNotFoundError(
                f"Project root does not exist: {project_root}"
            )

        if not project_root.is_dir():
            raise NotADirectoryError(project_root)

        modules: list[Path] = []

        logger.info(
            "Starting module discovery from %s",
            project_root,
        )

        self._discover_recursive(
            project_root=project_root,
            current_directory=project_root,
            modules=modules,
        )

        modules.sort()

        logger.info(
            "Discovered %d Python modules.",
            len(modules),
        )

        return modules

    def _discover_recursive(
        self,
        project_root: Path,
        current_directory: Path,
        modules: list[Path],
    ) -> None:
        """
        Recursively discover Python modules.

        Parameters
        ----------
        project_root
            Root of the project.

        current_directory
            Directory currently being scanned.

        modules
            Collection of discovered modules.
        """
        if self._should_ignore(current_directory):
            return

        try:
            children = sorted(
                current_directory.iterdir(),
                key=lambda path: path.name,
            )
        except PermissionError:
            logger.warning(
                "Skipping inaccessible directory: %s",
                current_directory,
            )
            return

        for child in children:
            if child.is_dir():
                self._discover_recursive(
                    project_root,
                    child,
                    modules,
                )
            elif self._is_python_module(child):
                modules.append(
                    child.relative_to(project_root)
                )

    def _is_python_module(
        self,
        file_path: Path,
    ) -> bool:
        """
        Determine whether a file is a Python module.

        Parameters
        ----------
        file_path
            File to evaluate.

        Returns
        -------
        bool
        """
        return (
            file_path.is_file()
            and file_path.suffix == ".py"
            and not file_path.name.startswith(".")
            and not file_path.is_symlink()
        )

    def _should_ignore(
        self,
        directory: Path,
    ) -> bool:
        """
        Determine whether a directory should be ignored.

        Parameters
        ----------
        directory
            Directory to evaluate.

        Returns
        -------
        bool
        """
        return directory.name in self._ignored_directories
