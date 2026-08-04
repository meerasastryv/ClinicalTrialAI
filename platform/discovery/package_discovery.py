"""
Python package discovery service.

Discovers Python packages within a project by locating directories
containing an __init__.py file.

Author: ClinicalTrialAI
"""

from __future__ import annotations

import logging
from pathlib import Path


logger = logging.getLogger(__name__)


class PackageDiscovery:
    """
    Discovers Python packages in a project.
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
        Initialize the package discovery service.

        Parameters
        ----------
        ignored_directories
            Additional directories to ignore.
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
        Discover all Python packages.

        Parameters
        ----------
        project_root
            Root directory of the project.

        Returns
        -------
        list[Path]
            Sorted list of discovered package directories.
        """
        if not project_root.exists():
            raise FileNotFoundError(
                f"Project root does not exist: {project_root}"
            )

        if not project_root.is_dir():
            raise NotADirectoryError(project_root)

        packages: list[Path] = []

        logger.info(
            "Starting package discovery from %s",
            project_root,
        )

        self._discover_recursive(
            project_root=project_root,
            current_directory=project_root,
            packages=packages,
        )

        packages.sort()

        logger.info(
            "Discovered %d Python packages.",
            len(packages),
        )

        return packages

    def _discover_recursive(
        self,
        project_root: Path,
        current_directory: Path,
        packages: list[Path],
    ) -> None:
        """
        Recursively discover packages.

        Parameters
        ----------
        project_root
            Root of the project.

        current_directory
            Current directory being scanned.

        packages
            Collection of discovered packages.
        """
        if self._should_ignore(current_directory):
            return

        if self._is_python_package(current_directory):
            packages.append(
                current_directory.relative_to(project_root)
            )

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
                    packages,
                )

    def _is_python_package(
        self,
        directory: Path,
    ) -> bool:
        """
        Determine whether a directory is a Python package.

        Parameters
        ----------
        directory
            Directory to evaluate.

        Returns
        -------
        bool
        """
        return (directory / "__init__.py").is_file()

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
