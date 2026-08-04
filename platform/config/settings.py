"""
Platform default settings.

Defines the default settings used throughout the ClinicalTrialAI
Platform Foundation.

Author: ClinicalTrialAI
"""

from __future__ import annotations

DEFAULT_PLATFORM_NAME = "ClinicalTrialAI"

DEFAULT_PLATFORM_VERSION = "1.0.0"

DEFAULT_SOURCE_DIRECTORY = "src"

DEFAULT_REPORT_DIRECTORY = "reports"

DEFAULT_LOG_DIRECTORY = "logs"

DEFAULT_LOG_FILE = "clinicaltrialai.log"

DEFAULT_LOG_LEVEL = "INFO"

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

SUPPORTED_MARKDOWN_EXTENSIONS = {
    ".md",
    ".markdown",
}

SUPPORTED_JSON_EXTENSIONS = {
    ".json",
}

SUPPORTED_YAML_EXTENSIONS = {
    ".yaml",
    ".yml",
}

SUPPORTED_CONFIGURATION_EXTENSIONS = {
    ".ini",
    ".cfg",
    ".conf",
    ".toml",
}

SUPPORTED_DATA_EXTENSIONS = {
    ".csv",
}

SUPPORTED_SOURCE_EXTENSIONS = {
    ".py",
}

SUPPORTED_REPORT_FORMATS = {
    "md",
    "json",
    "csv",
}

DEFAULT_ENCODING = "utf-8"

DEFAULT_INDENT = 4

DEFAULT_TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"

DEFAULT_REPORT_FILE_PREFIX = "report"
