"""
Project discovery orchestrator.

Coordinates the discovery services to build a complete project
discovery result.

Author: ClinicalTrialAI
"""

from __future__ import annotations

import logging
from pathlib import Path

from ct_platform.discovery.discovery_result import DiscoveryResult
from ct_platform.discovery.file_discovery import FileDiscovery
from ct_platform.discovery.module_discovery import ModuleDiscovery
from ct_platform.discovery.package_discovery import PackageDiscovery

logger = logging.getLogger(__name__)


class ProjectDiscovery:
    """
    Orchestrates project discovery.

    This class coordinates the package, module and file discovery
    services and produces a unified DiscoveryResult.
    """

    def __init__(
        self,
        package_discovery: PackageDiscovery | None = None,
        module_discovery: ModuleDiscovery | None = None,
        file_discovery: FileDiscovery | None = None,
    ) -> None:
        """
        Initialize the project discovery service.

        Parameters
        ----------
        package_discovery
            Package discovery implementation.

        module_discovery
            Module discovery implementation.

        file_discovery
            File discovery implementation.
        """
        self._package_discovery = (
            package_discovery or PackageDiscovery()
        )

        self._module_discovery = (
            module_discovery or ModuleDiscovery()
        )

        self._file_discovery = (
            file_discovery or FileDiscovery()
        )

    def discover(
        self,
        project_root: Path,
    ) -> DiscoveryResult:
        """
        Discover the complete project structure.

        Parameters
        ----------
        project_root
            Root directory of the project.

        Returns
        -------
        DiscoveryResult
        """
        project_root = project_root.resolve()

        self._validate_project_root(project_root)

        logger.info(
            "Starting project discovery for %s",
            project_root,
        )

        result = self._file_discovery.discover(project_root)

        result.packages = self._package_discovery.discover(
            project_root
        )

        result.modules = self._module_discovery.discover(
            project_root
        )

        result.project_root = project_root
        result.source_root = self._find_source_root(
            project_root
        )

        self._populate_statistics(result)

        logger.info(
            (
                "Project discovery completed. "
                "Packages=%d Modules=%d PythonFiles=%d"
            ),
            result.total_packages,
            result.total_modules,
            result.total_python_files,
        )

        return result

    def _validate_project_root(
        self,
        project_root: Path,
    ) -> None:
        """
        Validate the supplied project root.

        Parameters
        ----------
        project_root
            Project root directory.
        """
        if not project_root.exists():
            raise FileNotFoundError(
                f"Project root does not exist: {project_root}"
            )

        if not project_root.is_dir():
            raise NotADirectoryError(project_root)

    def _find_source_root(
        self,
        project_root: Path,
    ) -> Path:
        """
        Determine the project's source root.

        Preference is given to a 'src' directory if present.

        Parameters
        ----------
        project_root
            Project root.

        Returns
        -------
        Path
        """
        src_directory = project_root / "src"

        if src_directory.exists() and src_directory.is_dir():
            return src_directory

        return project_root

    def _populate_statistics(
        self,
        result: DiscoveryResult,
    ) -> None:
        """
        Populate discovery statistics.

        Parameters
        ----------
        result
            Discovery result.
        """
        result.total_packages = len(result.packages)

        result.total_modules = len(result.modules)

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
