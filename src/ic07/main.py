"""
IC-07 Test Data Intelligence Engine

Author : Meera Sastry
Project : ClinicalTrialAI
"""

import logging
import sys
from pathlib import Path

from src.ic07.config import IC07Config
from src.ic07.repositories.data_set_repository import DataSetRepository

from src.ic07.services.metadata_analyzer import MetadataAnalyzer
from src.ic07.services.data_profiling_service import DataProfilingService
#from src.ic07.services.data_quality_service import DataQualityService
from src.ic07.services.synthetic_data_service import SyntheticDataService

from src.ic07.models.synthetic_data_request import SyntheticDataRequest

from src.ic07.reports.synthetic_data_report import SyntheticDataReport

# ----------------------------------------------------------------------
# Configure Logging
# ----------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
)

logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------
# Banner
# ----------------------------------------------------------------------

def print_banner() -> None:
    """Display the IC-07 startup banner."""

    print("\n" + "=" * 70)
    print(" ClinicalTrialAI")
    print(" IC-07 : Test Data Intelligence Engine")
    print(" Version : 1.0.0")
    print("=" * 70 + "\n")


# ----------------------------------------------------------------------
# Directory Validation
# ----------------------------------------------------------------------

def validate_directories(config: IC07Config) -> bool:
    """
    Verify that the required project directories exist.
    """

    base_path = Path(__file__).parent

    missing = []

    for directory in config.REQUIRED_DIRECTORIES:
        path = base_path / directory

        if not path.exists():
            missing.append(directory)

    if missing:
        logger.error("Missing directories: %s", ", ".join(missing))
        return False

    logger.info("Directory validation successful.")
    return True


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main() -> int:
    """
    Main entry point for the Test Data Intelligence Engine.
    """

    try:

        print_banner()

        logger.info("Initializing IC-07...")

        config = IC07Config()

        logger.info("Project      : %s", config.PROJECT_NAME)
        logger.info("Component    : %s", config.COMPONENT_NAME)
        logger.info("Version      : %s", config.VERSION)

        if not validate_directories(config):
            return 1

        logger.info("Configuration loaded successfully.")
        logger.info("IC-07 startup completed successfully.")


        """
        # ---------------------------------------------------------
        # Execute IC-07 Pipeline
        # ---------------------------------------------------------
        logger.info("=" * 70)
        logger.info("Starting Test Data Intelligence Pipeline")
        logger.info("=" * 70)
        # 1. Load dataset
        #dataset_repository = DataSetRepository(config)
        dataset_repository = DataSetRepository()
        dataset = dataset_repository.load_dataset()
        # 2. Metadata Analysis
        metadata_service = MetadataAnalyzer()
        metadata_result = metadata_service.analyze(dataset)
        # 3. Data Profiling
        profiling_service = DataProfilingService()
        profile_result = profiling_service.profile(dataset)
        # 4. Data Quality
        #quality_service = DataQualityService()
        #quality_result = quality_service.analyze(dataset)
        # 5. Synthetic Data Generation
        request = SyntheticDataRequest(
                  rows=1000,include_nulls=True,include_duplicates=True,include_invalid_values=True,include_boundary_values=True,preserve_distribution=True,)
        synthetic_service = SyntheticDataService()
        synthetic_result = synthetic_service.generate(dataset,metadata_result,profile_result,request,)
        # 6. Report
        SyntheticDataReport().print_report(synthetic_result)
        """

        # Execute IC-07 Pipeline
        # ------------------------------------------------------------------
        logger.info("=" * 70)
        logger.info("Starting Test Data Intelligence Pipeline")
        logger.info("=" * 70)
        # -------------------------------------------------------------
        # Initialize Services
        metadata_service = MetadataAnalyzer()
        profiling_service = DataProfilingService()
        synthetic_service = SyntheticDataService()
        logger.info("All services initialized successfully.")
        # -------------------------------------------------------------
        # Repository Statistics
        repository = DataSetRepository()
        logger.info("Repository contains %d datasets.", repository.count())
        # -------------------------------------------------------------
        # Synthetic Data Request
        request = SyntheticDataRequest(
                  rows=1000,include_nulls=True,include_duplicates=True,include_invalid_values=True,include_boundary_values=True,preserve_distribution=True,)
        logger.info("Synthetic data request created.")
        # -------------------------------------------------------------
        # NOTE
        # Actual dataset loading will be integrated in Milestone 7
        # once DataSetRepository is connected to external sources.
        # At present the repository stores DataSet objects only.
        # -------------------------------------------------------------
        logger.info("IC-07 Pipeline initialized successfully.")
        logger.info("Ready for dataset execution.")

        logger.info("IC-07 Pipeline completed successfully.")
        return 0





    except Exception as ex:
        logger.exception("Fatal error during startup: %s", ex)
        return 1


# ----------------------------------------------------------------------
# Entry Point
# ----------------------------------------------------------------------

if __name__ == "__main__":
    sys.exit(main())
