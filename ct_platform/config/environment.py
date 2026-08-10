"""
Platform environment definitions.

Defines supported runtime environments for the ClinicalTrialAI
Platform Foundation.

Author: ClinicalTrialAI
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class Environment(Enum):
    """
    Supported platform environments.
    """

    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"


@dataclass(slots=True)
class EnvironmentConfiguration:
    """
    Environment-specific configuration.
    """

    environment: Environment

    debug: bool

    log_level: str

    report_directory: Path

    enable_console_logging: bool

    enable_file_logging: bool

    follow_symlinks: bool

    include_hidden_files: bool


DEVELOPMENT_CONFIGURATION = EnvironmentConfiguration(
    environment=Environment.DEVELOPMENT,
    debug=True,
    log_level="DEBUG",
    report_directory=Path("reports/development"),
    enable_console_logging=True,
    enable_file_logging=False,
    follow_symlinks=False,
    include_hidden_files=False,
)

TEST_CONFIGURATION = EnvironmentConfiguration(
    environment=Environment.TESTING,
    debug=True,
    log_level="DEBUG",
    report_directory=Path("reports/testing"),
    enable_console_logging=True,
    enable_file_logging=False,
    follow_symlinks=False,
    include_hidden_files=False,
)

STAGING_CONFIGURATION = EnvironmentConfiguration(
    environment=Environment.STAGING,
    debug=False,
    log_level="INFO",
    report_directory=Path("reports/staging"),
    enable_console_logging=True,
    enable_file_logging=True,
    follow_symlinks=False,
    include_hidden_files=False,
)

PRODUCTION_CONFIGURATION = EnvironmentConfiguration(
    environment=Environment.PRODUCTION,
    debug=False,
    log_level="INFO",
    report_directory=Path("reports/production"),
    enable_console_logging=False,
    enable_file_logging=True,
    follow_symlinks=False,
    include_hidden_files=False,
)


def get_environment_configuration(
    environment: Environment,
) -> EnvironmentConfiguration:
    """
    Return the configuration for the specified environment.

    Parameters
    ----------
    environment
        Target runtime environment.

    Returns
    -------
    EnvironmentConfiguration
    """
    configurations = {
        Environment.DEVELOPMENT:
            DEVELOPMENT_CONFIGURATION,

        Environment.TESTING:
            TEST_CONFIGURATION,

        Environment.STAGING:
            STAGING_CONFIGURATION,

        Environment.PRODUCTION:
            PRODUCTION_CONFIGURATION,
    }

    return configurations[environment]
