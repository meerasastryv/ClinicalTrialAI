"""
Platform configuration models.

Defines the strongly typed configuration objects used throughout
the ClinicalTrialAI Platform Foundation.

Author: ClinicalTrialAI
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class DiscoveryConfiguration:
    """
    Configuration for the Platform Discovery Engine.
    """

    ignored_directories: set[str] = field(default_factory=set)
    follow_symlinks: bool = False
    include_hidden_files: bool = False


@dataclass(slots=True)
class ReportingConfiguration:
    """
    Configuration for platform reporting.
    """

    output_directory: Path = Path("reports")
    generate_markdown: bool = True
    generate_json: bool = True
    generate_csv: bool = True


@dataclass(slots=True)
class LoggingConfiguration:
    """
    Configuration for logging.
    """

    level: str = "INFO"
    log_to_console: bool = True
    log_to_file: bool = False
    log_directory: Path = Path("logs")
    log_file_name: str = "clinicaltrialai.log"


@dataclass(slots=True)
class PlatformConfiguration:
    """
    Global platform configuration.
    """

    project_root: Path = Path(".")
    source_root: Path = Path("src")
    platform_name: str = "ClinicalTrialAI"
    platform_version: str = "1.0.0"

    discovery: DiscoveryConfiguration = field(
        default_factory=DiscoveryConfiguration
    )

    reporting: ReportingConfiguration = field(
        default_factory=ReportingConfiguration
    )

    logging: LoggingConfiguration = field(
        default_factory=LoggingConfiguration
    )

    def resolve_paths(self) -> None:
        """
        Resolve all configured filesystem paths.
        """
        self.project_root = self.project_root.resolve()
        self.source_root = self.source_root.resolve()
        self.reporting.output_directory = (
            self.reporting.output_directory.resolve()
        )
        self.logging.log_directory = (
            self.logging.log_directory.resolve()
        )

    def as_dict(self) -> dict[str, object]:
        """
        Return a serializable dictionary representation.
        """
        return {
            "platform_name": self.platform_name,
            "platform_version": self.platform_version,
            "project_root": str(self.project_root),
            "source_root": str(self.source_root),
            "discovery": {
                "ignored_directories": sorted(
                    self.discovery.ignored_directories
                ),
                "follow_symlinks": self.discovery.follow_symlinks,
                "include_hidden_files": (
                    self.discovery.include_hidden_files
                ),
            },
            "reporting": {
                "output_directory": str(
                    self.reporting.output_directory
                ),
                "generate_markdown": (
                    self.reporting.generate_markdown
                ),
                "generate_json": self.reporting.generate_json,
                "generate_csv": self.reporting.generate_csv,
            },
            "logging": {
                "level": self.logging.level,
                "log_to_console": self.logging.log_to_console,
                "log_to_file": self.logging.log_to_file,
                "log_directory": str(
                    self.logging.log_directory
                ),
                "log_file_name": self.logging.log_file_name,
            },
        }
