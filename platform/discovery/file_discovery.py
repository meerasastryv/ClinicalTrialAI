"""
Project file discovery service.

Discovers and categorizes project files.

Author: ClinicalTrialAI
"""

from __future__ import annotations

import logging
from pathlib import Path

from platform.discovery.discovery_result import DiscoveryResult

logger = logging.getLogger(__name__)


class FileDiscovery:
    """
    Discovers and categorizes project files.
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

    CONFIG_FILE_NAMES = {
        "pyproject.toml",
        "requirements.txt",
        "requirements-dev.txt",
        "setup.py",
        "setup.cfg",
        "Dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        ".gitignore",
        ".env",
        "Makefile",
        "tox.ini",
    }

    def __init__(
        self,
        ignored_directories: set[str] | None = None,
    ) -> None:
        """
        Initialize the file discovery service.

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
    ) -> DiscoveryResult:
        """
        Discover and categorize project files.

        Parameters
        ----------
        project_root
            Root directory of the project.

        Returns
        -------
        DiscoveryResult
        """
        if not project_root.exists():
            raise FileNotFoundError(project_root)

        if not project_root.is_dir():
            raise NotADirectoryError(project_root)

        result = DiscoveryResult(project_root=project_root)

        logger.info(
            "Starting file discovery from %s",
            project_root,
        )

        self._discover_recursive(
            project_root=project_root,
            current_directory=project_root,
            result=result,
        )

        self._sort_result(result)
        self._populate_statistics(result)

        logger.info(
            "Discovered %d files.",
            result.total_files,
        )

        return result

    def _discover_recursive(
        self,
        project_root: Path,
        current_directory: Path,
        result: DiscoveryResult,
    ) -> None:
        """
        Recursively discover project files.
        """
        if self._should_ignore(current_directory):
            result.ignored_directories.append(
                current_directory.relative_to(project_root)
            )
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
                    result,
                )
            elif child.is_file():
                self._categorize_file(
                    project_root,
                    child,
                    result,
                )

    def _categorize_file(
        self,
        project_root: Path,
        file_path: Path,
        result: DiscoveryResult,
    ) -> None:
        """
        Categorize a discovered file.
        """
        relative_path = file_path.relative_to(project_root)
        suffix = file_path.suffix.lower()

        if suffix == ".py":
            result.python_files.append(relative_path)

        elif suffix in {".md", ".markdown"}:
            result.markdown_files.append(relative_path)

        elif suffix == ".json":
            result.json_files.append(relative_path)

        elif suffix in {".yaml", ".yml"}:
            result.yaml_files.append(relative_path)

        elif suffix == ".toml":
            result.toml_files.append(relative_path)

        elif suffix == ".csv":
            result.csv_files.append(relative_path)

        elif suffix in {
            ".ini",
            ".cfg",
            ".conf",
        }:
            result.configuration_files.append(relative_path)

        if file_path.name in self.CONFIG_FILE_NAMES:
            if relative_path not in result.configuration_files:
                result.configuration_files.append(
                    relative_path
                )

        if "report" in relative_path.parts:
            parent = relative_path.parent
            if parent not in result.report_directories:
                result.report_directories.append(parent)

    def _populate_statistics(
        self,
        result: DiscoveryResult,
    ) -> None:
        """
        Populate summary statistics.
        """
        result.total_python_files = len(
            result.python_files
        )

        result.total_configuration_files = len(
            result.configuration_files
        )

        result.total_files = (
            len(result.python_files)
            + len(result.markdown_files)
            + len(result.json_files)
            + len(result.yaml_files)
            + len(result.toml_files)
            + len(result.csv_files)
            + len(result.configuration_files)
        )

    def _sort_result(
        self,
        result: DiscoveryResult,
    ) -> None:
        """
        Sort discovered collections.
        """
        result.python_files.sort()
        result.markdown_files.sort()
        result.json_files.sort()
        result.yaml_files.sort()
        result.toml_files.sort()
        result.csv_files.sort()
        result.configuration_files.sort()
        result.report_directories.sort()
        result.ignored_directories.sort()

    def _should_ignore(
        self,
        directory: Path,
    ) -> bool:
        """
        Determine whether a directory should be ignored.
        """
        return directory.name in self._ignored_directories
