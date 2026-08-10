"""
IC-07 Test Data Intelligence Engine Configuration

Author : Meera Sastry
Project : ClinicalTrialAI
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


@dataclass
class IC07Config:
    """
    Configuration for the Test Data Intelligence Engine.
    """

    # ------------------------------------------------------------------
    # Project Information
    # ------------------------------------------------------------------

    PROJECT_NAME: str = "ClinicalTrialAI"
    COMPONENT_NAME: str = "IC-07 Test Data Intelligence Engine"
    VERSION: str = "1.0.0"

    # ------------------------------------------------------------------
    # Directories
    # ------------------------------------------------------------------

    BASE_DIR: Path = field(default_factory=lambda: Path.cwd())

    DATA_DIR: Path = field(init=False)
    REPORT_DIR: Path = field(init=False)
    LOG_DIR: Path = field(init=False)

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------

    LOG_LEVEL: str = "INFO"

    # ------------------------------------------------------------------
    # Dataset Configuration
    # ------------------------------------------------------------------

    DEFAULT_DATASET: str = "sample_test_data.csv"

    SUPPORTED_FORMATS: List[str] = field(
        default_factory=lambda: [
            "csv",
            "json",
            "xml",
            "xlsx"
        ]
    )

    # ------------------------------------------------------------------
    # Synthetic Data Generation
    # ------------------------------------------------------------------

    ENABLE_SYNTHETIC_DATA: bool = True
    DEFAULT_RECORD_COUNT: int = 100

    # ------------------------------------------------------------------
    # Data Masking
    # ------------------------------------------------------------------

    ENABLE_MASKING: bool = True

    MASKING_STRATEGIES: List[str] = field(
        default_factory=lambda: [
            "full",
            "partial",
            "hash",
            "randomize",
            "nullify"
        ]
    )

    # ------------------------------------------------------------------
    # Profiling
    # ------------------------------------------------------------------

    ENABLE_PROFILING: bool = True

    PROFILE_METRICS: List[str] = field(
        default_factory=lambda: [
            "completeness",
            "uniqueness",
            "consistency",
            "validity",
            "duplicates"
        ]
    )

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    REQUIRED_DIRECTORIES: List[str] = field(
        default_factory=lambda: [
            "models",
            "repositories",
            "services",
            "reports",
            "utils"
        ]
    )

    # ------------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------------

    def __post_init__(self):

        self.DATA_DIR = self.BASE_DIR / "data"

        self.REPORT_DIR = self.BASE_DIR / "reports"

        self.LOG_DIR = self.BASE_DIR / "logs"

    # ------------------------------------------------------------------

    def as_dict(self) -> Dict:
        """
        Return configuration as dictionary.
        """

        return self.__dict__
