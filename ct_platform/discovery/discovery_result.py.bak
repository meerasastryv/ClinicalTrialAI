"""
Discovery result model.

Represents the complete output of the Platform Discovery Engine.

Author: ClinicalTrialAI
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class DiscoveryResult:
    """
    Represents the discovered structure of a project.

    This model is intentionally generic so it can be reused by all
    Intelligence Components within the ClinicalTrialAI platform.
    """

    project_root: Path
    source_root: Path | None = None

    packages: list[Path] = field(default_factory=list)
    modules: list[Path] = field(default_factory=list)
    python_files: list[Path] = field(default_factory=list)

    configuration_files: list[Path] = field(default_factory=list)
    markdown_files: list[Path] = field(default_factory=list)
    json_files: list[Path] = field(default_factory=list)
    yaml_files: list[Path] = field(default_factory=list)
    toml_files: list[Path] = field(default_factory=list)
    csv_files: list[Path] = field(default_factory=list)

    report_directories: list[Path] = field(default_factory=list)

    ignored_directories: list[Path] = field(default_factory=list)
    ignored_files: list[Path] = field(default_factory=list)

    total_packages: int = 0
    total_modules: int = 0
    total_python_files: int = 0
    total_configuration_files: int = 0
    total_files: int = 0

    def as_dict(self) -> dict[str, object]:
        """
        Convert the discovery result into a JSON-serializable dictionary.

        Returns
        -------
        dict[str, object]
            Dictionary representation of the discovery result.
        """
        return {
            "project_root": str(self.project_root),
            "source_root": (
                str(self.source_root)
                if self.source_root is not None
                else None
            ),
            "packages": [str(path) for path in self.packages],
            "modules": [str(path) for path in self.modules],
            "python_files": [str(path) for path in self.python_files],
            "configuration_files": [
                str(path) for path in self.configuration_files
            ],
            "markdown_files": [
                str(path) for path in self.markdown_files
            ],
            "json_files": [str(path) for path in self.json_files],
            "yaml_files": [str(path) for path in self.yaml_files],
            "toml_files": [str(path) for path in self.toml_files],
            "csv_files": [str(path) for path in self.csv_files],
            "report_directories": [
                str(path) for path in self.report_directories
            ],
            "ignored_directories": [
                str(path) for path in self.ignored_directories
            ],
            "ignored_files": [
                str(path) for path in self.ignored_files
            ],
            "total_packages": self.total_packages,
            "total_modules": self.total_modules,
            "total_python_files": self.total_python_files,
            "total_configuration_files": (
                self.total_configuration_files
            ),
            "total_files": self.total_files,
        }

    @property
    def has_source_root(self) -> bool:
        """
        Return True if a source root was discovered.
        """
        return self.source_root is not None

    @property
    def is_empty(self) -> bool:
        """
        Return True if no project content was discovered.
        """
        return (
            self.total_packages == 0
            and self.total_modules == 0
            and self.total_files == 0
        )
