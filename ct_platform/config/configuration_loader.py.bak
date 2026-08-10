"""
Platform configuration loader.

Loads and prepares the ClinicalTrialAI platform configuration.

Author: ClinicalTrialAI
"""

from __future__ import annotations

import logging
from pathlib import Path

from ct_platform.config.configuration import (
    DiscoveryConfiguration,
    LoggingConfiguration,
    PlatformConfiguration,
    ReportingConfiguration,
)
from ct_platform.config.environment import (
    Environment,
    get_environment_configuration,
)
from ct_platform.config.settings import (
    DEFAULT_IGNORED_DIRECTORIES,
    DEFAULT_LOG_DIRECTORY,
    DEFAULT_LOG_FILE,
    DEFAULT_LOG_LEVEL,
    DEFAULT_PLATFORM_NAME,
    DEFAULT_PLATFORM_VERSION,
    DEFAULT_REPORT_DIRECTORY,
    DEFAULT_SOURCE_DIRECTORY,
)

logger = logging.getLogger(__name__)


class ConfigurationLoader:
    """
    Loads platform configuration.
    """

    def load(
        self,
        project_root: Path,
        environment: Environment = Environment.DEVELOPMENT,
    ) -> PlatformConfiguration:
        """
        Load platform configuration.

        Parameters
        ----------
        project_root
            Root of the project.

        environment
            Runtime environment.

        Returns
        -------
        PlatformConfiguration
        """
        project_root = project_root.resolve()

        env = get_environment_configuration(environment)

        configuration = PlatformConfiguration(
            project_root=project_root,
            source_root=project_root / DEFAULT_SOURCE_DIRECTORY,
            platform_name=DEFAULT_PLATFORM_NAME,
            platform_version=DEFAULT_PLATFORM_VERSION,
            discovery=DiscoveryConfiguration(
                ignored_directories=set(
                    DEFAULT_IGNORED_DIRECTORIES
                ),
                follow_symlinks=env.follow_symlinks,
                include_hidden_files=(
                    env.include_hidden_files
                ),
            ),
            reporting=ReportingConfiguration(
                output_directory=(
                    project_root
                    / env.report_directory
                ),
                generate_markdown=True,
                generate_json=True,
                generate_csv=True,
            ),
            logging=LoggingConfiguration(
                level=env.log_level,
                log_to_console=(
                    env.enable_console_logging
                ),
                log_to_file=(
                    env.enable_file_logging
                ),
                log_directory=(
                    project_root
                    / DEFAULT_LOG_DIRECTORY
                ),
                log_file_name=DEFAULT_LOG_FILE,
            ),
        )

        configuration.resolve_paths()

        configuration.reporting.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        configuration.logging.log_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        logger.info(
            "Loaded %s configuration.",
            environment.value,
        )

        return configuration
